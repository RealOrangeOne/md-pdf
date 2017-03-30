import pdfkit
from md_pdf.consts import ASSET_DIR
from md_pdf.build.cover import OUTPUT_COVER_FILE
import os


STYLE_FILE = os.path.join(ASSET_DIR, 'style.css')
HEADER_FILE = os.path.join(ASSET_DIR, 'header.html')
FOOTER_FILE = os.path.join(ASSET_DIR, 'footer.html')
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
}


def export_pdf(content, config):
    PDF_OPTIONS['title'] = getattr(config, 'title', 'output')
    PDF_OPTIONS['replace'] = list(config.context.items())

    return pdfkit.from_string(
        content,
        os.path.join(os.path.abspath(config.output_dir), 'output.pdf'),
        options=PDF_OPTIONS,
        css=STYLE_FILE,
        cover=OUTPUT_COVER_FILE
    )
