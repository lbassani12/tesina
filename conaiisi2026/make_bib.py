"""Genera refs-paper.bib a partir de ../refs.bib para el paper CoNaIISI.

No toca ../refs.bib (compartido con la tesina). Ajustes que aplica, sólo para
la bibliografía del paper con el estilo `unsrt`:
  - quita los campos `note` con anotaciones internas de trabajo;
  - da un venue a raimondo:2024 (queda sin `note` al quitar la anotación);
  - protege con llaves la capitalización de los títulos de las entradas que
    `unsrt` pasa a minúscula (nombres propios y siglas);
  - normaliza el título en versales de mazon:2023.
Ejecutar antes de `latexmk`.
"""
import re, pathlib

SIN_NOTE = {"raimondo:2024", "behbahanian", "prompt-eng:2024", "provdm:2013"}
NOTE_NUEVA = {"raimondo:2024": "Cap{\\'i}tulo de libro, Simposio de Ciencias Sociales Computacionales 2024"}
TITULO_NUEVO = {"mazon:2023": "{Color of Corruption. Visual evidence of agenda-setting in a complex mass media ecosystem}"}
PROTEGER_TITULO = {"zamfirescu2023", "haider2025", "raimondo:2024", "couldry:2017", "neupane2025",
                   "milbauer2023", "pavlyshenko2024", "behbahanian", "lewis:2020", "garlanshaw:1994",
                   "cristia:2025", "gindin:2018", "carlon:2020", "cuevasvicenttin:2012"}

src = pathlib.Path(__file__).with_name("..") / "refs.bib"
dst = pathlib.Path(__file__).with_name("refs-paper.bib")
texto = src.read_text(encoding="utf-8")

def limpiar(m):
    cuerpo, clave = m.group(0), m.group(2)
    if clave in SIN_NOTE:
        cuerpo = re.sub(r"\n\s*note\s*=\s*\{[^{}]*(\{[^{}]*\}[^{}]*)*\},?", "", cuerpo)
    if clave in NOTE_NUEVA:
        cuerpo = cuerpo.rstrip()[:-1].rstrip().rstrip(",") + ",\n  note = {" + NOTE_NUEVA[clave] + "}\n}"
    if clave in TITULO_NUEVO:
        cuerpo = re.sub(r"(\n\s*title\s*=\s*)\{[^\n]*\}", lambda mm: mm.group(1) + "{" + TITULO_NUEVO[clave] + "}", cuerpo, count=1)
    elif clave in PROTEGER_TITULO:
        cuerpo = re.sub(r"(\n\s*title\s*=\s*)\{(.*)\}(,?)\n", lambda mm: mm.group(1) + "{{" + mm.group(2) + "}}" + mm.group(3) + "\n", cuerpo, count=1)
    return cuerpo

salida = re.sub(r"@(\w+)\{([^,]+),(.*?)\n\}", limpiar, texto, flags=re.S)
dst.write_text("% Generado por make_bib.py a partir de ../refs.bib. No editar a mano.\n" + salida, encoding="utf-8")
print("ok", dst)
