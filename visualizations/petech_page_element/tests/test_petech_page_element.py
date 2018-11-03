import unittest
from webviz_petech_page_element import PetechPageElement


class TestPetechPageElement(unittest.TestCase):
    def test_depends_on_webviz_petech_js(self):
        ppe = PetechPageElement()

        self.assertTrue(any(
            (('src', '{root_folder}/resources/js/webviz_petech.js')
             in e.attributes)
            for e in ppe.header_elements))

        self.assertTrue(any(
            (('href', '{root_folder}/resources/css/webviz_petech.css')
             in e.attributes)
            for e in ppe.header_elements))

if __name__ == '__main__':
    unittest.main()
