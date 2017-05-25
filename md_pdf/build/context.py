from md_pdf.consts import TEMPLATES_DIR, STATIC_DIR
from word_count import word_count
from md_pdf.utils import get_plain_text


EXTRA_CONTEXT = {
    'templates_dir': TEMPLATES_DIR,
    'static_dir': STATIC_DIR
}


def get_context(config, content):
    context = config['context'].copy()
    context['title'] = config['title']
    context = dict(context, **EXTRA_CONTEXT, **{
    })
    if config.get('show_word_count'):
        context['word_count'] = word_count(get_plain_text(content))
    return context
