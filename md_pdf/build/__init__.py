from md_pdf.build.md import read_files
from md_pdf.build.pandoc import build_document, output_html
from md_pdf.build.templates import render_templates
from md_pdf.build.css import render_css
from md_pdf.build.pdf import export_pdf
from md_pdf.build.content import parse_template
import os
import logging
import time

logger = logging.getLogger(__file__)


def build(config):
    logger.debug("Starting Build...")
    start_time = time.time()
    data = read_files(os.path.abspath(config['input']))
    doc = build_document(data, config.get('bibliography'))
    parsed_template = parse_template(doc, config)
    if 'html' in config['output_formats']:
        output_html(parsed_template, os.path.abspath(config['output_dir']))
    if 'pdf' in config['output_formats']:
        render_templates(config, parsed_template)
        render_css()
        export_pdf(parsed_template, config)
    logger.info('Output completed in {:.2f} seconds.'.format(time.time() - start_time))
