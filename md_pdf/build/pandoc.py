import pypandoc
from bs4 import BeautifulSoup
import os
from md_pdf.consts import CSL_DIR
from jinja2 import Template
import logging

logger = logging.getLogger(__file__)


def fix_references_title(content):
    logger.debug("Adding Reference Title...")
    soup = BeautifulSoup(content, 'html.parser')
    reference_element = soup.find('div', class_='references')
    if reference_element is not None:
        title = soup.new_tag('h1')
        title.string = "References"
        reference_element.insert_before(title)
    return soup.prettify()


def output_html(html, out_dir):
    logger.info("Outputting HTML...")
    with open(os.path.join(out_dir, 'output.html'), 'w') as f:
        f.write(html)


def parse_template(html, context):
    logger.debug("Rendering Template...")
    template = Template(html)
    return template.render(context)


def build_document(files_content, bibliography, context):
    args = [
        '-s',
    ]
    filters = []
    if bibliography is not None:
        args += [
            '--bibliography={}'.format(os.path.abspath(bibliography['references'])),
            '--csl={}'.format(os.path.join(CSL_DIR, "{}.csl".format(bibliography['csl'])))
        ]
        filters.append('pandoc-citeproc')
    logger.info("Rendering Document...")
    html = fix_references_title(pypandoc.convert_text(
        files_content,
        'html',
        format='md',
        extra_args=args,
        filters=filters
    ))

    return parse_template(html, context)
