import subprocess
from pathlib import Path

import pytask
import latex_dependency_scanner
from config import ROOT_NAME, ROOT_TEX, ROOT_PDF
from docs.template.symbols import generate_symbols_tex

LATEX_OPTS = ("--interaction=nonstopmode", "--synctex=1")


@pytask.mark.depends_on("template/symbols.bib")
@pytask.mark.produces("template/symbols.tex")
def task_template_symbols(depends_on: Path, produces: Path):
    produces.write_text(
        generate_symbols_tex(
            depends_on.read_text(),
            True
        )
    )


@pytask.mark.depends_on(latex_dependency_scanner.scanner.scan(ROOT_TEX))
@pytask.mark.depends_on(ROOT_TEX)
@pytask.mark.produces(ROOT_PDF)
@pytask.mark.try_last
def task_compile():
    subprocess.run(("pdflatex", *LATEX_OPTS, ROOT_TEX), check=True)
    subprocess.run(("biber", ROOT_NAME), check=True)
    subprocess.run(("bib2gls", ROOT_NAME), check=True)
    subprocess.run(("pdflatex", *LATEX_OPTS, ROOT_TEX), check=True)
    subprocess.run(("pdflatex", *LATEX_OPTS, ROOT_TEX), check=True)
