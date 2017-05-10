from jinja2 import Template
from bs4 import BeautifulSoup
import os
import logging

logger = logging.getLogger(__file__)


def fix_references_title(content, config):
    logger.debug("Adding Reference Title...")
    soup = BeautifulSoup(content, 'html.parser')
    reference_element = soup.find('div', class_='references')
    if reference_element is not None:
        title = soup.new_tag('h1')
        title.string = "References"
        reference_element.insert_before(title)
    return soup.prettify()


def add_base_tag(doc, config):
    logger.debug("Adding Base Tag...")
    soup = BeautifulSoup(doc, 'html.parser')
    base_tag = soup.new_tag('base', href=os.path.abspath(config['output_dir']))
    soup.head.insert(0, base_tag)
    return soup.prettify()


def add_body_class(doc, config):
    logger.debug("Adding Body Class...")
    soup = BeautifulSoup(doc, 'html.parser')
    soup.body['class'] = 'content'
    return soup.prettify()


def render_template(html, config):
    logger.debug("Rendering Template...")
    template = Template(html)
    return template.render(config)


def parse_template(doc, config):
    parsed_doc = doc
    for parser in [
        fix_references_title,
        add_base_tag,
        add_body_class,
    ]:
        parsed_doc = parser(parsed_doc, config)
    return render_template(parsed_doc, config)


