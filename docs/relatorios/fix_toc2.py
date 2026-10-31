import io, os, re, subprocess, sys

DIR = r'C:/Users/mathe/code_space/hackaton/docs/relatorios'
RENDER = os.path.join(DIR, 'render_pdf.cjs')
NODE = r'C:/Program Files/nodejs/node.exe'
LABELS = {
    '01-horizonte-de-trabalho': 'Cheers - Horizonte de Trabalho',
    '02-nucleo-e-gaps': 'Cheers - O nucleo',
    '03-evidencia-mercado-regulacao': 'Cheers - Evidencia, mercado e regulacao',
    '04-kit-13-11-e-build': 'Cheers - Kit de 13/11 e plano de build',
}


def norm(s):
    s = s.replace('\u2014', '-').replace('\u2013', '-').replace('\u00b7', ' ')
    return re.sub(r'[^a-z0-9]', '', s.lower())


def render(name):
    html = os.path.join(DIR, name + '.html')
    pdf = os.path.join(DIR, name + '.pdf')
    r = subprocess.run([NODE, RENDER, '--in', html, '--out', pdf, '--format', 'A4',
                        '--label', LABELS[name], '--wait', '1200'],
                       capture_output=True, text=True)
    if r.returncode != 0:
        raise SystemExit('render falhou em %s: %s' % (name, r.stderr[-400:]))
    return pdf


def page_texts(pdf):
    """Uma unica chamada ao pdftotext; as paginas vem separadas por \\f."""
    r = subprocess.run(['pdftotext', '-layout', pdf, '-'],
                       capture_output=True, text=True, errors='replace')
    return [norm(p) for p in r.stdout.split('\f') if p.strip() or True][:-1]


def analyze(t):
    secs = []
    for m in re.finditer(r'<section class="page[^"]*"([^>]*)>(.*?)</section>', t, re.S):
        attrs, blk = m.group(1), m.group(2)
        sid = re.search(r'id="([^"]+)"', attrs)
        run = re.search(r'<span class="r">(.*?)</span>', blk, re.S)
        secs.append({'id': sid.group(1) if sid else None,
                     'run': re.sub(r'<[^>]+>', '', run.group(1)).strip() if run else None})
    return secs


def fix(name):
    html = os.path.join(DIR, name + '.html')
    pdf = os.path.join(DIR, name + '.pdf')
    t = io.open(html, encoding='utf-8').read()
    pgs = page_texts(pdf)
    total = len(pgs)
    secs = analyze(t)

    real = {}
    for s in secs:
        if not s['run']:
            continue
        key = norm(s['run'])
        if len(key) < 6:
            continue
        hit = next((j for j in range(2, total) if key in pgs[j]), None)
        if hit is not None:
            real[s['id']] = hit + 1

    def toc_rep(m):
        anchor, body = m.group(1), m.group(2)
        sid = anchor.lstrip('#')
        if sid in real:
            return re.sub(r'<span class="p">\d+</span>',
                          '<span class="p">%d</span>' % real[sid], body, flags=re.S) and \
                   '<a class="toc-row" href="%s">%s' % (anchor, re.sub(
                       r'<span class="p">\d+</span>', '<span class="p">%d</span>' % real[sid], body, flags=re.S))
        return m.group(0)

    t2 = re.sub(r'<a class="toc-row" href="([^"]+)">(.*?)</a>', toc_rep, t, flags=re.S)
    changed = t2 != t
    if changed:
        io.open(html, 'w', encoding='utf-8', newline='').write(t2)
        render(name)

    overflow = [(s['id'], real.get(s['id'])) for i, s in enumerate(secs)
                if s['run'] and i >= 2 and real.get(s['id']) != i + 1]
    print('%s -> %d paginas | %d secoes | TOC %s | estouros: %s' %
          (name, total, len(real), 'atualizado' if changed else 'ja correto',
           overflow or 'nenhum'))


if __name__ == '__main__':
    for n in sys.argv[1:]:
        fix(n)
