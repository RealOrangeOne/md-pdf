from tests import BaseTestCase
from md_pdf import consts
from unittest import skipIf
import os
import requests
import datetime
from freezegun import freeze_time


class ConstsTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.this_dir = os.path.dirname(__file__)
        self.project_root = os.path.normpath(os.path.join(self.this_dir, '..'))

    def test_project_dir(self):
        self.assertEqual(
            consts.PROJECT_DIR,
            os.path.normpath(os.path.join(self.this_dir, '..', 'md_pdf'))
        )
        self.assertIn(consts.WORKING_DIR, consts.PROJECT_DIR)

    def test_working_dir(self):
        self.assertEqual(consts.WORKING_DIR, self.project_root)

    @skipIf('APPDATA' not in os.environ, 'not on windows')
    def test_windows_asset_dir(self):
        self.assertIn(os.environ['APPDATA'], consts.ASSETS_DIR)

    @skipIf('HOME' not in os.environ, 'not on windows')
    def test_asset_dir(self):
        self.assertEqual(consts.ASSETS_DIR, os.path.expanduser('~/.mdp'))

    def test_csl_dir(self):
        self.assertIn(consts.ASSETS_DIR, consts.CSL_DIR)
        self.assertIn('csl', consts.CSL_DIR)

    def test_templates_dir(self):
        self.assertIn(consts.ASSETS_DIR, consts.TEMPLATES_DIR)
        self.assertIn('templates', consts.TEMPLATES_DIR)

    def test_static_dir(self):
        self.assertIn(consts.ASSETS_DIR, consts.STATIC_DIR)
        self.assertIn('static', consts.STATIC_DIR)

    def test_internal_asset_dir(self):
        self.assertIn(consts.PROJECT_DIR, consts.INTERNAL_ASSETS_DIR)
        self.assertIn('assets', consts.INTERNAL_ASSETS_DIR)

    def test_internal_static_dir(self):
        self.assertIn(consts.PROJECT_DIR, consts.INTERNAL_STATIC_DIR)
        self.assertIn('static', consts.INTERNAL_STATIC_DIR)

    def test_internal_templates_dir(self):
        self.assertIn(consts.PROJECT_DIR, consts.INTERNAL_TEMPLATES_DIR)
        self.assertIn('templates', consts.INTERNAL_TEMPLATES_DIR)

    def test_config_file(self):
        self.assertIn(consts.WORKING_DIR, consts.CONFIG_FILE)
        self.assertIn('mdp.yml', consts.CONFIG_FILE)

    def test_csl_download_link(self):
        self.assertIn('https://github.com', consts.CSL_DOWNLOAD_LINK)
        self.assertTrue(consts.CSL_DOWNLOAD_LINK.endswith('master.zip'))

    def test_csl_accessible(self):
        response = requests.head(consts.CSL_DOWNLOAD_LINK)
        if response.status_code == 302:
            response = requests.head(response.headers['Location'])
        self.assertEqual(response.status_code, 200)
        headers = response.headers
        self.assertEqual(headers['Content-Type'], 'application/zip')
        self.assertEqual(headers['Content-Disposition'], 'attachment; filename=styles-master.zip')

    @freeze_time('2017-01-01')
    def test_date_format(self):
        now = datetime.datetime.now()
        self.assertEqual(
            now.strftime(consts.DATE_FORMAT),
            '01 January 2017'
        )

    @freeze_time('2017-01-01T12:34')
    def test_time_format(self):
        now = datetime.datetime.now()
        self.assertEqual(
            now.strftime(consts.TIME_FORMAT),
            '12:34'
        )

    @freeze_time('2017-01-01T12:34')
    def test_time_format(self):
        now = datetime.datetime.now()
        self.assertEqual(
            now.strftime(consts.DATETIME_FORMAT),
            '01 January 2017 12:34'
        )

    def test_dirs_existt(self):
        self.assertTrue(os.path.isdir(consts.ASSETS_DIR))
        self.assertTrue(os.path.isdir(consts.TEMPLATES_DIR))
        self.assertTrue(os.path.isdir(consts.STATIC_DIR))



