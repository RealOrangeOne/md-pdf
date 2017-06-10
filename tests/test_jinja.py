from tests import BaseTestCase
from md_pdf.build.jinja import render_content


class ContentRendererTestCase(BaseTestCase):
    def test_renders_template(self):
        html = 'test {{ test }}'
        output = render_content(html, self.extend_config({
            'test': 'content'
        }))
        self.assertEqual(output, 'test content')

    def test_changes_nothing(self):
        html = 'test test'
        output = render_content(html, self.extend_config({
            'test': 'content'
        }))
        self.assertEqual(output, html)

    def test_with_block(self):
        html = """
        {% with test = 'test' %}
            {{ test }} thing
        {% endwith %}
        """
        output = render_content(html, self.BASE_VALID_CONFIG)
        self.assertIn('test thing', output)
