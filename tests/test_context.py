from tests import BaseTestCase
from md_pdf.build.context import get_context, EXTRA_CONTEXT
from md_pdf import consts
from datetime import datetime
from md_pdf import __version__


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
