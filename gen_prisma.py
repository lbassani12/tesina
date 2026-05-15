"""Genera diagrama PRISMA como SVG y lo convierte a PNG."""

W, H = 1680, 1900

# ── Constantes de layout ─────────────────────────────────
LX, LW = 28, 215          # columna label
MX, MW = 258, 730         # columna principal
MCX    = MX + MW // 2     # = 623
EX, EW = 1030, 622        # columna exclusión
QCX    = W // 2           # centro del query box = 840

# ── Paleta: un solo color teal ───────────────────────────
TEAL    = '#2A7F7F'
QBG     = '#EBF3FB'; QBD = '#2471A3'
MBG     = '#F8F9FA'; MBD = '#999999'
XBG     = '#FEF9E7'; XBD = '#CA8A04'; XTX = '#7D6608'
ARR     = '#444444'
TXT     = '#1A1A1A'

def esc(s):
    return s.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')

def rect(x, y, w, h, fill, stroke, sw=1.8, rx=10):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>\n'

def t(x, y, s, sz, fill=TXT, fw='normal', anchor='middle', baseline='middle'):
    return (f'<text x="{x}" y="{y}" text-anchor="{anchor}" '
            f'dominant-baseline="{baseline}" '
            f'font-family="Arial,Helvetica,sans-serif" '
            f'font-size="{sz}" fill="{fill}" font-weight="{fw}">'
            f'{esc(s)}</text>\n')

def tlines(cx, y0, lines, sz, fill=TXT, fw='normal', lh=None, anchor='middle'):
    lh = lh or int(sz * 1.38)
    return ''.join(t(cx, y0 + i*lh, ln, sz, fill, fw, anchor=anchor) for i, ln in enumerate(lines))

def arr_v(x, y1, y2):
    return f'<line x1="{x}" y1="{y1}" x2="{x}" y2="{y2}" stroke="{ARR}" stroke-width="3.5" marker-end="url(#ah)"/>\n'

def arr_h(x1, x2, y):
    return f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="{ARR}" stroke-width="2.8" marker-end="url(#ah)"/>\n'

# ── Fases: (y_top, height, label_lines) ─────────────────
PHASES = [
    (370,  300, ['Identificación']),
    (754,  300, ['Cribado', '(Screening)']),
    (1138, 300, ['Elegibilidad']),
    (1522, 300, ['Inclusión']),
]

EXCL = {
    1: {
        'title': 'Excluidos  (n = 150)',
        'lines': [
            'Duplicados eliminados (n = 20)',
            'Excluidos por baja relevancia',
            'en título / resumen (n = 130)',
        ]
    },
    2: {
        'title': 'Excluidos  (n = 54)',
        'lines': [
            'Informes no recuperados',
            '(sin acceso al texto completo)',
        ]
    },
    3: {
        'title': 'Excluidos  (n = 41)',
        'lines': [
            'Fuera del tema principal (n = 20)',
            'Sin metodología replicable (n = 12)',
            'Idioma no admitido (n = 9)',
        ]
    },
}

MAIN_INFO = [
    (['Registros identificados en 6 bases de', 'datos académicas'],                        'n = 254', TEAL),
    (['Registros cribados tras lectura', 'de título y resumen'],                           'n = 104', TEAL),
    (['Artículos evaluados mediante', 'lectura de texto completo'],                        'n = 50',  TEAL),
    (['Estudios incluidos en la síntesis', 'crítica del estado del arte'],                 'n = 9',   TEAL),
]

# ── Construcción SVG ─────────────────────────────────────
svg = []
svg.append(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}">')
svg.append('''<defs>
  <marker id="ah" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
    <polygon points="0 0, 10 3.5, 0 7" fill="#444444"/>
  </marker>
</defs>''')
svg.append(f'<rect width="{W}" height="{H}" fill="white"/>')

# ── Título ───────────────────────────────────────────────
svg.append(t(W//2, 40, 'Diagrama de Selección Bibliográfica  —  Protocolo PRISMA',
             48, TXT, 'bold'))

# ── Query box ────────────────────────────────────────────
QY, QH = 68, 278
svg.append(rect(LX, QY, W-LX*2, QH, QBG, QBD, sw=2.2))
svg.append(t(QCX, QY+38, 'ESTRATEGIA DE BÚSQUEDA', 36, QBD, 'bold'))
query_lines = [
    '("generative AI"  OR  "LLM"  OR  "large language model")  AND  ("web scraping"  OR  "news extraction"  OR  "crawling")',
    'AND  ("NLP"  OR  "embeddings"  OR  "text analysis")  AND  ("agenda-setting"  OR  "media analysis"  OR  "news")',
    '',
    'Fuentes: Google Scholar · ArXiv                    Aplicada sobre: título, resumen y palabras clave',
]
svg.append(tlines(QCX, QY+82, query_lines, 30, TXT, lh=36))

# Flecha query → Ident
svg.append(arr_v(MCX, QY+QH+6, PHASES[0][0]-8))

# ── Fases ────────────────────────────────────────────────
for idx, (py, ph, label_lines) in enumerate(PHASES):
    pmid = py + ph // 2

    # Label box (teal único)
    svg.append(rect(LX, py, LW, ph, TEAL, TEAL, sw=0))
    label_y0 = pmid - (len(label_lines)-1)*24
    for li, ln in enumerate(label_lines):
        svg.append(t(LX+LW//2, label_y0+li*48, ln, 28, 'white', 'bold'))

    # Main box
    svg.append(rect(MX, py, MW, ph, MBG, MBD))
    hdr_lines, nstr, ncol = MAIN_INFO[idx]
    hdr_y = pmid - 44 - (len(hdr_lines)-1)*26
    for li, ln in enumerate(hdr_lines):
        svg.append(t(MCX, hdr_y+li*50, ln, 32, TXT, 'bold'))
    svg.append(t(MCX, pmid+54, nstr, 50, ncol, 'bold'))

    # Exclusion box
    ELX = EX + 22   # margen izquierdo dentro del box
    if idx in EXCL:
        edata = EXCL[idx]
        svg.append(rect(EX, py, EW, ph, XBG, XBD, sw=1.8))
        svg.append(t(ELX, py+38, edata['title'], 36, XTX, 'bold', anchor='start'))
        svg.append(tlines(ELX, py+80, edata['lines'], 28, TXT, lh=38, anchor='start'))
        svg.append(arr_h(MX+MW+6, EX-6, pmid))

    # Flecha hacia la siguiente fase
    if idx < len(PHASES)-1:
        next_py = PHASES[idx+1][0]
        svg.append(arr_v(MCX, py+ph+6, next_py-8))

svg.append('</svg>')

svg_path = '/home/lucio/personal/tesina/Tesina_Bassani_Lucio/prisma_diagram.svg'
with open(svg_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(svg))

print(f"SVG guardado: {svg_path}")
