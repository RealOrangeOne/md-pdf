from md_pdf.consts import TEMPLATES_DIR, STATIC_DIR, DATE_FORMAT, TIME_FORMAT, DATETIME_FORMAT
from word_count import word_count
from md_pdf.utils import get_plain_text
from md_pdf import __version__
from dateutil import parser
import datetime
import os


EXTRA_CONTEXT = {
    'templates_dir': TEMPLATES_DIR,
    'static_dir': STATIC_DIR,
    'date': datetime.datetime.now().strftime(DATE_FORMAT),
    'time': datetime.datetime.now().strftime(TIME_FORMAT),
    'datetime': datetime.datetime.now().strftime(DATETIME_FORMAT),
    'mdp_version': __version__
}


def get_context(config, content):
    config = config.copy()
    context = config['context'].copy()
    del config['context']
    context = dict(
        config,
        **EXTRA_CONTEXT,
        **context,
        **{
            'output_dir': os.path.abspath(config['output_dir']),
        }
    )
    if config.get('show_word_count'):
        context['word_count'] = word_count(get_plain_text(content))
    if config.get('submission_date'):
        if type(config['submission_date']) in [datetime.date, datetime.datetime, datetime.time]:
            submission_date = config['submission_date']
        else:
            submission_date = parser.parse(config['submission_date'])
        context['submission_date'] = submission_date.strftime(DATE_FORMAT)
    return context
