import unittest
import shutil
import os
import tempfile
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from webviz_dynamic_tree import DynamicTree


class TestMorrisMethod(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        thisdir = os.path.abspath(os.path.dirname(__file__))

        cls.tempdir = tempfile.mkdtemp()
        os.chdir(cls.tempdir)

        command = 'python {}/../examples/dynamic_tree_example.py'\
                  .format(thisdir)
        cls.ret = os.system(command)

        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-gpu")
        cls.driver = webdriver.Chrome(options=options)

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.tempdir)
        cls.driver.close()

    def setUp(self):
        address = 'file://{}/webviz_example/index.html'.format(self.tempdir)
        self.driver.get(address)

    def test_return_value(self):
        self.assertEqual(self.ret, 0)

    def test_depends_on_morris_method(self):

        dt = DynamicTree({})

        self.assertTrue(any(
            (('src', '{root_folder}/resources/js/dynamic_tree.js')
             in e.attributes) for e in dt.header_elements))


if __name__ == '__main__':
    unittest.main()
