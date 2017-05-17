from jinja2 import Template
from md_pdf.consts import TEMPLATES_DIR, STATIC_DIR
import os
import logging

logger = logging.getLogger(__file__)

EXTRA_CONFIG = {
    'templates_dir': TEMPLATES_DIR,
    'static_dir': STATIC_DIR
}

FILE_NAME_FORMAT = os.path.join(TEMPLATES_DIR, "{}.html")
TEMPLATE_FORMAT = os.path.join(TEMPLATES_DIR, "{}-template.html")


def render_page(input_file, output_file, context):
    logger.debug("Rendering {}...")
    with open(input_file) as f:
        template = Template(f.read())
    with open(output_file, "w") as f:
        cover = template.render(context)
        f.write(cover)
        return cover


def render_templates(config):
    context = config['context'].copy()
    context['title'] = config['title']
    context = dict(context, **EXTRA_CONFIG)
    for template in [
        'cover',
        'header',
        'footer'
    ]:
        render_page(TEMPLATE_FORMAT.format(template), FILE_NAME_FORMAT.format(template), context)
    render_page(os.path.join(TEMPLATES_DIR, 'toc-template.xsl'), os.path.join(TEMPLATES_DIR, 'toc.xsl'), context)
