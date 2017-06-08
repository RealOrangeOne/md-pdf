from md_pdf.consts import TEMPLATES_DIR, INTERNAL_TEMPLATES_DIR
from md_pdf.build.context import get_context
from md_pdf.build.jinja import render_content
import os
import logging

logger = logging.getLogger(__file__)


FILE_NAME_FORMAT = os.path.join(TEMPLATES_DIR, "{}.html")
TEMPLATE_FORMAT = os.path.join(INTERNAL_TEMPLATES_DIR, "{}-template.html")


def render_page(input_file, output_file, context):
    logger.debug("Rendering {}...".format(os.path.splitext(os.path.basename(output_file))[0].title()))
    with open(input_file) as f:
        content = render_content(f.read(), context)
    with open(output_file, "w") as f:
        f.write(content)
        return content


def render_templates(config, content):
    context = get_context(config, content)
    for template in [
        'cover',
        'header',
        'footer'
    ]:
        render_page(TEMPLATE_FORMAT.format(template), FILE_NAME_FORMAT.format(template), context)
    if config.get('toc', False):
        render_page(os.path.join(INTERNAL_TEMPLATES_DIR, 'toc-template.xsl'), os.path.join(TEMPLATES_DIR, 'toc.xsl'), context)
