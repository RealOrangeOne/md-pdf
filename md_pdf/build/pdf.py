import pdfkit
from md_pdf.consts import PROJECT_DIR
from md_pdf.build.cover import OUTPUT_COVER_FILE
import os


STYLE_FILE = os.path.join(PROJECT_DIR, 'assets', 'style.css')
HEADER_FILE = os.path.join(PROJECT_DIR, 'assets', 'header.html')
FOOTER_FILE = os.path.join(PROJECT_DIR, 'assets', 'footer.html')
PDF_OPTIONS = {
    "quiet": "",
    "no-pdf-compression": "",

    "margin-top": '0.6in',
    "margin-bottom": '0.6in',
    "margin-left": '0.4in',
    "margin-right": '0.4in',

    "header-html": HEADER_FILE,
    "footer-html": FOOTER_FILE,
    "footer-spacing": 5,
    "header-spacing": 5,

    "title": "Title thing",
    "replace": [

    ]
}


def export_pdf(content, out_dir):
    return pdfkit.from_string(
        content,
        os.path.join(out_dir, 'output.pdf'),
        options=PDF_OPTIONS,
        css=STYLE_FILE,
        cover=OUTPUT_COVER_FILE
    )
