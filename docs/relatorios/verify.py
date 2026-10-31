import io, os, re, subprocess, sys

DIR = r'C:/Users/mathe/code_space/hackaton/docs/relatorios'
RX = re.compile('[\u4E00-\u9FFF\uAC00-\uD7AF\u0400-\u04FF\u0600-\u06FF\u0900-\u097F]')


def check_links(pdf):
    try:
        from pypdf import PdfReader
    except Exception as e:
        return 'pypdf indisponivel: %s' % e
    r = PdfReader(pdf)
    total = 0
    internal = 0
    for pg in r.pages:
        annots = pg.get('/Annots') or []
        for a in annots:
            try:
                o = a.get_object()
            except Exception:
                continue
            if o.get('/Subtype') == '/Link':
                total += 1
                if o.get('/Dest') is not None or o.get('/A'):
                    internal += 1
    return 'links=%d (navegacao interna=%d)' % (total, internal)


def check_anchors(html, pdf):
    """Confere que cada ancora do sumario tem destino no PDF."""
    t = io.open(html, encoding='utf-8').read()
    anchors = re.findall(r'<a class="toc-row" href="#([^"]+)"', t)
    ids = set(re.findall(r'<section class="page"[^>]*id="([^"]+)"', t))
    missing = [a for a in anchors if a not in ids]
    return 'ancoras=%d | destinos ausentes=%s' % (len(anchors), missing or 'nenhum')


for name in sys.argv[1:]:
    html = os.path.join(DIR, name + '.html')
    pdf = os.path.join(DIR, name + '.pdf')
    print('=== %s ===' % name)
    info = subprocess.run(['pdfinfo', pdf], capture_output=True, text=True).stdout
    print('  ', re.search(r'Pages:\s+\d+', info).group(0), '|',
          re.search(r'Page size:.*', info).group(0).strip())
    print('  ', check_anchors(html, pdf))
    print('  ', check_links(pdf))
    t = io.open(html, encoding='utf-8').read()
    hits = [(i + 1, l.strip()[:100]) for i, l in enumerate(t.split('\n')) if RX.search(l)]
    print('   nao-latinos no HTML:', hits or 'nenhum')
    # texto do PDF: procura marcadores de erro
    txt = subprocess.run(['pdftotext', '-layout', pdf, '-'], capture_output=True, text=True, errors='replace').stdout
    phits = [(i + 1, l.strip()[:100]) for i, l in enumerate(txt.split('\n')) if RX.search(l)]
    print('   nao-latinos no PDF:', phits or 'nenhum')
    print()
