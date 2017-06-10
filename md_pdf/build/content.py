from bs4 import BeautifulSoup
import os
import logging
from md_pdf.build.context import get_context
from md_pdf.build.jinja import render_content

logger = logging.getLogger(__file__)


def fix_references_title(content, config):
    logger.debug("Adding Reference Title...")
    soup = BeautifulSoup(content, 'html.parser')
    reference_element = soup.find('div', class_='references')
    if reference_element is not None:
        title = soup.new_tag('h1')
        title['class'] = 'references-title'
        title.string = "References"
        reference_element.insert_before(title)
    return soup.prettify()


def make_images_relative(doc, config):
    logger.debug("Adding Base Tag...")
    soup = BeautifulSoup(doc, 'html.parser')
    for img in soup.findAll('img'):
        abs_path = os.path.abspath(img['src'])
        if os.path.isfile(abs_path):
            img['src'] = abs_path
    return soup.prettify()


def add_body_class(doc, config):
    logger.debug("Adding Body Class...")
    soup = BeautifulSoup(doc, 'html.parser')
    if not soup.body:
        return doc
    soup.body['class'] = 'content'
    return soup.prettify()


def render_template(html, config):
    logger.debug("Rendering Template...")
    context = get_context(config, html)
    return render_content(html, context)


def parse_template(doc, config):
    parsed_doc = doc
    for parser in [
        fix_references_title,
        make_images_relative,
        add_body_class,
    ]:
        parsed_doc = parser(parsed_doc, config)
    return render_template(parsed_doc, config)
