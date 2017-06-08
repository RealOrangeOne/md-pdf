from tests import BaseTestCase
from md_pdf.args import parse_args


class ArgParserTestCase(BaseTestCase):
    def test_allows_no_args(self):
        args = parse_args([])
        self.assertFalse(args.update_csl)
        self.assertEqual(args.verbose, 0)

    def test_adds_verbosity(self):
        args = parse_args(['-v'])
        self.assertEqual(args.verbose, 1)

    def test_chains_verbosity(self):
        for i in range(1, 10):
            args = parse_args(['-' + ('v' * i)])
            self.assertEqual(args.verbose, i)

    def test_csl_update(self):
        args = parse_args(['--update-csl'])
        self.assertTrue(args.update_csl)
