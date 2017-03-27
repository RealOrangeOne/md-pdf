import pypandoc
from bs4 import BeautifulSoup


def fix_references_title(content):
    soup = BeautifulSoup(content, 'html.parser')
    title = soup.new_tag('h1')
    title.string = "References"
    soup.find('div', class_="references").insert_before(title)
    return soup.prettify()


def build_document(files_content):
    html = pypandoc.convert_text(files_content, 'html', format='md',
        extra_args=[
            '-s',
            '--bibliography=bib.yml',
            '--csl=harvard.csl'
        ],
        filters=[
            'pandoc-citeproc'
        ]
    )

    return fix_references_title(html)
