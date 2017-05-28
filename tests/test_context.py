from tests import BaseTestCase
from md_pdf.build.context import get_context, EXTRA_CONTEXT
from md_pdf import consts
from datetime import datetime
from md_pdf import __version__
import os


class ExtraContextTestCase(BaseTestCase):
    def test_directories(self):
        self.assertEqual(EXTRA_CONTEXT['templates_dir'], consts.TEMPLATES_DIR)
        self.assertEqual(EXTRA_CONTEXT['static_dir'], consts.STATIC_DIR)
        self.assertEqual(EXTRA_CONTEXT['internal_templates_dir'], consts.INTERNAL_TEMPLATES_DIR)
        self.assertEqual(EXTRA_CONTEXT['internal_static_dir'], consts.INTERNAL_STATIC_DIR)

    def test_datetimes(self):
        now = datetime.now()
        self.assertEqual(EXTRA_CONTEXT['date'], now.strftime(consts.DATE_FORMAT))
        self.assertEqual(EXTRA_CONTEXT['time'], now.strftime(consts.TIME_FORMAT))
        self.assertEqual(EXTRA_CONTEXT['datetime'], now.strftime(consts.DATETIME_FORMAT))

    def test_version(self):
        self.assertEqual(EXTRA_CONTEXT['mdp_version'], __version__)


class ContextTestCase(BaseTestCase):
    def test_context_contains_extra(self):
        context = get_context(self.BASE_VALID_CONFIG, 'test')
        for key in EXTRA_CONTEXT.keys():
            self.assertIn(key, context)

    def test_context_contains_context(self):
        config = self.extend_config({
            'context': {
                '1': '2'
            }
        })
        context = get_context(config, 'test')
        self.assertEqual(context['1'], '2')
        self.assertNotIn('context', context)

    def test_context_contains_config(self):
        context = get_context(self.BASE_VALID_CONFIG, 'test')
        for key in self.BASE_VALID_CONFIG.keys():
            self.assertIn(key, context)

    def test_has_output_dir(self):
        context = get_context(self.BASE_VALID_CONFIG, 'test')
        self.assertEqual(context['output_dir'], os.path.abspath(self.BASE_VALID_CONFIG['output_dir']))

    def test_word_count(self):
        config = self.extend_config({
            'show_word_count': True
        })
        context = get_context(config, 'testy test test')
        self.assertEqual(context['word_count'], 3)

    def test_transparent_datetime_for_submission_date(self):
        for value in [
            datetime.now().date(),
            datetime.now().time(),
            datetime.now()
        ]:
            config = self.extend_config({
                'submission_date': value
            })
            context = get_context(config, 'test')
            self.assertEqual(context['submission_date'], value.strftime(consts.DATE_FORMAT))

    def test_date_format(self):
        config = self.extend_config({
            'submission_date': '2017-01-01'
        })
        context = get_context(config, 'test')
        self.assertEqual(context['submission_date'], '01 January 2017')


