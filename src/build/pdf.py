import pdfkit

pdf_options = {
    "quiet": "",
    "no-pdf-compression": "",

    "margin-top": '0.6in',
    "margin-bottom": '0.6in',
    "margin-left": '0.4in',
    "margin-right": '0.4in',

    "header-html": "header.html",
    "footer-html": "footer.html",
    "footer-spacing": 5,
    "header-spacing": 5,

    "title": "Title thing",
    "replace": [

    ]
}


def export_pdf(content):
    return pdfkit.from_string(
        content,
        'out.pdf',
        options=pdf_options,
        css="style.css",
        cover="cover.html"
    )
