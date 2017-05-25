from md_pdf.consts import TEMPLATES_DIR, STATIC_DIR
from word_count import word_count


EXTRA_CONTEXT = {
    'templates_dir': TEMPLATES_DIR,
    'static_dir': STATIC_DIR
}


def get_context(config, content):
    context = config['context'].copy()
    context['title'] = config['title']
    context = dict(context, **EXTRA_CONTEXT)
    context['word_count'] = word_count(content)
    return context
