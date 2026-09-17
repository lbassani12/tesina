# Build config del paper CoNaIISI 2026. Uso: `latexmk` dentro de conaiisi2026/.
use Cwd;
my $here = getcwd();
my $repo_root = "$here/..";
$ENV{'TEXMFVAR'}    = "$repo_root/.cache/texmf-var";
$ENV{'TEXMFCACHE'}  = "$repo_root/.cache/texmf-cache";
$ENV{'TEXMFCONFIG'} = "$repo_root/.cache/texmf-config";
mkdir "$repo_root/.cache"  unless -d "$repo_root/.cache";
mkdir $ENV{'TEXMFVAR'}     unless -d $ENV{'TEXMFVAR'};
mkdir $ENV{'TEXMFCACHE'}   unless -d $ENV{'TEXMFCACHE'};
mkdir $ENV{'TEXMFCONFIG'}  unless -d $ENV{'TEXMFCONFIG'};
$pdf_mode = 4;
$lualatex = 'lualatex -synctex=1 -interaction=nonstopmode -file-line-error -halt-on-error %O %S';
$bibtex_use = 2;
$bibtex     = 'bibtex %O %S';
@default_files = ('paper.tex');
$clean_ext = 'synctex.gz synctex.gz(busy) run.xml bbl bcf fdb_latexmk fls aux';
$preview_continuous_mode = 0;
