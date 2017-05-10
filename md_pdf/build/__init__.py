from md_pdf.build.md import read_files
from md_pdf.build.pandoc import build_document, output_html
from md_pdf.build.cover import render_cover
from md_pdf.build.css import render_css
from md_pdf.build.pdf import export_pdf
from md_pdf.build.template import parse_template
import os
import logging

logger = logging.getLogger(__file__)


def build(config):
    logger.debug("Starting Build...")
    data = read_files(os.path.abspath(config['input']))
    doc = build_document(data, config.get('bibliography'), config.get('context'))
    parsed_template = parse_template(doc, config)
    if 'html' in config['output_formats']:
        output_html(parsed_template, os.path.abspath(config['output_dir']))
    if 'pdf' in config['output_formats']:
        render_cover(config)
        render_css()
        export_pdf(parsed_template, config)
