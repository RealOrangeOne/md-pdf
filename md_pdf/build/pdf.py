import pdfkit
from md_pdf.consts import TEMPLATES_DIR, STATIC_DIR
from md_pdf.build.templates import FILE_NAME_FORMAT
from md_pdf.exceptions import PDFRenderException
import os
import logging


logger = logging.getLogger(__file__)


DEFAULT_MARGIN_VERTICAL = '1.5cm'
DEFAULT_MARGIN_HORIZONTAL = '2.5cm'

STYLE_FILE = os.path.join(STATIC_DIR, 'style.css')
HEADER_FILE = os.path.join(TEMPLATES_DIR, 'header.html')
FOOTER_FILE = os.path.join(TEMPLATES_DIR, 'footer.html')

TOC_OPTIONS = {
    'xsl-style-sheet': os.path.join(TEMPLATES_DIR, 'toc.xsl')
}

PDF_OPTIONS = {
    "no-pdf-compression": "",
    "enable-internal-links": "",

    "header-html": HEADER_FILE,
    "footer-html": FOOTER_FILE,
    "footer-spacing": 5,
    "header-spacing": 5,

    "user-style-sheet": STYLE_FILE
}


def export_pdf(content, config):
    if logger.getEffectiveLevel() > logging.DEBUG:
        PDF_OPTIONS['quiet'] = ""
    PDF_OPTIONS['title'] = config.get('title', 'Output')
    PDF_OPTIONS['replace'] = [(key, str(value)) for key, value in config['context'].items()]

    PDF_OPTIONS['margin-top'] = config['context'].get('margin_vertical', DEFAULT_MARGIN_VERTICAL)
    PDF_OPTIONS['margin-bottom'] = config['context'].get('margin_vertical', DEFAULT_MARGIN_VERTICAL)
    PDF_OPTIONS['margin-left'] = config['context'].get('margin_horizontal', DEFAULT_MARGIN_HORIZONTAL)
    PDF_OPTIONS['margin-right'] = config['context'].get('margin_horizontal', DEFAULT_MARGIN_HORIZONTAL)

    logger.info("Rendering PDF...")
    render_ok = pdfkit.from_string(
        content,
        os.path.join(os.path.abspath(config['output_dir']), 'output.pdf'),
        options=PDF_OPTIONS,
        cover=FILE_NAME_FORMAT.format('cover'),
        toc=TOC_OPTIONS if config.get('toc') else {},
        cover_first=True
    )
    if not render_ok:
        raise PDFRenderException('Failed to render PDF. ' + render_ok)
    return PDF_OPTIONS  # mostly for testing

