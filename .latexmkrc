# Build config para latexmk (Tesina Bassani)
# Uso: `latexmk` para compilar, `latexmk -c` para limpiar auxiliares, `latexmk -C` para borrar también el PDF.

# Cache local de luaotfload (evita "no writeable cache path" cuando $HOME no es escribible).
# Estos dirs son ignorados por git (ver .gitignore).
use Cwd;
my $repo_root = getcwd();
$ENV{'TEXMFVAR'}    = "$repo_root/.cache/texmf-var";
$ENV{'TEXMFCACHE'}  = "$repo_root/.cache/texmf-cache";
$ENV{'TEXMFCONFIG'} = "$repo_root/.cache/texmf-config";
mkdir "$repo_root/.cache"             unless -d "$repo_root/.cache";
mkdir $ENV{'TEXMFVAR'}                unless -d $ENV{'TEXMFVAR'};
mkdir $ENV{'TEXMFCACHE'}              unless -d $ENV{'TEXMFCACHE'};
mkdir $ENV{'TEXMFCONFIG'}             unless -d $ENV{'TEXMFCONFIG'};

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
