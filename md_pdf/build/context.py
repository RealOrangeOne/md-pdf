from md_pdf.consts import TEMPLATES_DIR, STATIC_DIR
from word_count import word_count
from md_pdf.utils import get_plain_text
from datetime import datetime


EXTRA_CONTEXT = {
    'templates_dir': TEMPLATES_DIR,
    'static_dir': STATIC_DIR,
    'date': datetime.now()
}


def get_context(config, content):
    config = config.copy()
    context = config['context'].copy()
    del config['context']
    context = dict(
        config,
        **context,
        **EXTRA_CONTEXT,
        **{

        }
    )
    if config.get('show_word_count'):
        context['word_count'] = word_count(get_plain_text(content))
    return context
