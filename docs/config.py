from pathlib import Path

ROOT_DIR = Path(__file__).parent.resolve()
ROOT_NAME = "docs"
ROOT_TEX = ROOT_DIR / f"{ROOT_NAME}.tex"
ROOT_PDF = ROOT_DIR / f"{ROOT_NAME}.pdf"

IMG_DIR = ROOT_DIR / "img"
TBL_DIR = ROOT_DIR / "tbl"
BIB_DIR = ROOT_DIR / "bib"

IMG_FORMATS = ["svg", "pdf", "png"]


def img_format_file_names(stem):
    return {f: f"{stem}.{f}" for f in IMG_FORMATS}
