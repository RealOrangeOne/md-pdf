from jinja2 import Template
from md_pdf.consts import ASSET_DIR
import os
import logging

logger = logging.getLogger(__file__)


COVER_TEMPLATE = os.path.join(ASSET_DIR, 'cover-template.html')
OUTPUT_COVER_FILE = os.path.join(ASSET_DIR, 'cover.html')


def render_cover(config):
    logger.info("Rendering Cover...")
    context = config['context'].copy()
    context['title'] = config['title']
    with open(COVER_TEMPLATE) as f:
        template = Template(f.read())
    with open(OUTPUT_COVER_FILE, "w") as f:
        cover = template.render(context)
        f.write(cover)
        return cover
