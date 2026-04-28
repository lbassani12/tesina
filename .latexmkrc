# Build config para latexmk (Tesina Bassani)
# Uso: `latexmk` para compilar, `latexmk -c` para limpiar auxiliares, `latexmk -C` para borrar también el PDF.

# Motor: LuaLaTeX (UTF-8 nativo, mejor para español)
$pdf_mode = 4;   # 1=pdflatex, 4=lualatex, 5=xelatex

$lualatex = 'lualatex -synctex=1 -interaction=nonstopmode -file-line-error -halt-on-error %O %S';

# Bibliografía: refs.bib es BibTeX clásico
$bibtex_use = 2;             # siempre correr bibtex aunque no haya .bcf
$bibtex     = 'bibtex %O %S';

# Índice (\makeindex / \printindex con imakeidx)
$makeindex = 'makeindex %O -o %D %S';

# Archivo principal por defecto
@default_files = ('main.tex');

# Limpieza extendida: extensiones extra que latexmk -c también borra
$clean_ext = 'synctex.gz synctex.gz(busy) run.xml bbl bcf fdb_latexmk fls aux idx ilg ind nav snm';

# Vista previa: deja que la extensión LaTeX Workshop maneje el visor
$preview_continuous_mode = 0;
