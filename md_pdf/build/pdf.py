import pdfkit
from md_pdf.consts import TEMPLATES_DIR, STATIC_DIR
from md_pdf.build.cover import OUTPUT_COVER_FILE
import os
import logging

logger = logging.getLogger(__file__)


DEFAULT_MARGIN_VERTICAL = '1.5cm'
DEFAULT_MARGIN_HORIZONTAL = '2.5cm'

STYLE_FILE = os.path.join(STATIC_DIR, 'style.css')
HEADER_FILE = os.path.join(TEMPLATES_DIR, 'header.html')
FOOTER_FILE = os.path.join(TEMPLATES_DIR, 'footer.html')
PDF_OPTIONS = {
    "quiet": "",
    "no-pdf-compression": "",
    "enable-internal-links": "",

    "header-html": HEADER_FILE,
    "footer-html": FOOTER_FILE,
    "footer-spacing": 5,
    "header-spacing": 5,

    "user-style-sheet": STYLE_FILE
}


def export_pdf(content, config):
    PDF_OPTIONS['title'] = config.get('title', 'Output')
    PDF_OPTIONS['replace'] = [(key, str(value)) for key, value in config['context'].items()]

    PDF_OPTIONS['margin-top'] = config['context'].get('margin_vertical', DEFAULT_MARGIN_VERTICAL)
    PDF_OPTIONS['margin-bottom'] = config['context'].get('margin_vertical', DEFAULT_MARGIN_VERTICAL)
    PDF_OPTIONS['margin-left'] = config['context'].get('margin_horizontal', DEFAULT_MARGIN_HORIZONTAL)
    PDF_OPTIONS['margin-right'] = config['context'].get('margin_horizontal', DEFAULT_MARGIN_HORIZONTAL)

    logger.info("Rendering PDF...")
    return pdfkit.from_string(
        content,
        os.path.join(os.path.abspath(config['output_dir']), 'output.pdf'),
        options=PDF_OPTIONS,
        cover=OUTPUT_COVER_FILE
    )
