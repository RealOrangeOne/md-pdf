import pypandoc
from bs4 import BeautifulSoup
import os.path
from md_pdf.utils import PROJECT_DIR


CSL_FILE = os.path.join(PROJECT_DIR, 'assets', 'harverd.csl')

def fix_references_title(content):
    soup = BeautifulSoup(content, 'html.parser')
    reference_element = soup.find('div', class_='references')
    if reference_element is not None:
        title = soup.new_tag('h1')
        title.string = "References"
        reference_element.insert_before(title)
    return soup.prettify()


def build_document(files_content, bibliography):
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
