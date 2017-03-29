import pypandoc
from bs4 import BeautifulSoup
import os.path
from md_pdf.consts import PROJECT_DIR


CSL_FILE = os.path.join(PROJECT_DIR, 'assets', 'harverd.csl')

def fix_references_title(content):
    soup = BeautifulSoup(content, 'html.parser')
    reference_element = soup.find('div', class_='references')
    if reference_element is not None:
        title = soup.new_tag('h1')
        title.string = "References"
        reference_element.insert_before(title)
    return soup.prettify()


def output_html(html, out_dir):
    with open(os.path.join(out_dir, 'output.html'), 'w') as f:
        f.write(html)


def build_document(files_content, bibliography=None):
    args = [
        '-s',
    ]
    filters = []
    if bibliography is not None:
        args += [
            '--bibliography={}'.format(bibliography),
            '--csl={}'.format(CSL_FILE)
        ]
        filters.append('pandoc-citeproc')

    html = pypandoc.convert_text(files_content, 'html', format='md',
        extra_args=args,
        filters=filters
    )

    return fix_references_title(html)
