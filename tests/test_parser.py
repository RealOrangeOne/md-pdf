from tests import BaseTestCase
from md_pdf.build import content
import os


class FixReferencesTitleTestCase(BaseTestCase):
    def test_adds_reference_title(self):
        html = '<div class="references"></div>'
        output = content.fix_references_title(html, self.BASE_VALID_CONFIG)
        self.assertIn('references-title', output)
        self.assertIn('References', output)

    def test_doesnt_modify_if_no_references(self):
        html = 'test text'
        output = content.fix_references_title(html, self.BASE_VALID_CONFIG)
        self.assertNotIn('references-title', output)
        self.assertNotIn('References', output)


class RelativeImageTestCase(BaseTestCase):
    def test_makes_image_relative(self):
        html = '<img src="test-files/test-image.png" />'
        output = self.parse_html(content.make_images_relative(html, self.BASE_VALID_CONFIG))
        self.assertEqual(output.find('img').attrs['src'], os.path.abspath('test-files/test-image.png'))

    def test_leaves_remote_images(self):
        html = '<img src="http://example.com/image.png" />'
        output = self.parse_html(content.make_images_relative(html, self.BASE_VALID_CONFIG))
        self.assertEqual(output.find('img').attrs['src'], 'http://example.com/image.png')


class AddBodyClassTestCase(BaseTestCase):
    def test_adds_class(self):
        html = '<body></body>'
        output = self.parse_html(content.add_body_class(html, self.BASE_VALID_CONFIG))
        self.assertEqual(output.body.attrs['class'], ['content'])

    def test_doesnt_change(self):
        html = 'test content'
        output = content.add_body_class(html, self.BASE_VALID_CONFIG)
        self.assertEqual(output, html)


class RenderTemplateTestCase(BaseTestCase):
    def test_renders_template(self):
        html = 'test {{ test }}'
        output = content.render_template(html, self.extend_config({
            'test': 'content'
        }))
        self.assertEqual(output, 'test content')

    def test_changes_nothing(self):
        html = 'test test'
        output = content.render_template(html, self.extend_config({
            'test': 'content'
        }))
        self.assertEqual(output, html)
