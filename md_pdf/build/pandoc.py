import pypandoc
import os
from md_pdf.consts import CSL_DIR
import logging

logger = logging.getLogger(__file__)


def output_html(html: str, out_dir: str):
    logger.info("Outputting HTML...")
    with open(os.path.join(out_dir, 'output.html'), 'w') as f:
        f.write(html)


def build_document(files_content: str, bibliography: dict) -> str:
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
    return pypandoc.convert_text(
        files_content,
        'html',
        format='md',
        extra_args=args,
        filters=filters
    )
