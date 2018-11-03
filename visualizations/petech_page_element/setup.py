import sys
import os
from setuptools import setup, find_packages

setup(
    name='webviz_petech_page_element',
    version='0.1.0',
    packages=find_packages("."),
    package_dir={"": "."},
    package_data={'webviz_petech_page_element': ['resources/js/*']},
    data_files=[
        (os.path.join(sys.prefix, "share/jupyter/nbextensions/webviz_petech_page_element"), [
            "webviz_petech_page_element/resources/js/webviz_petech.js",
        ]),
        (os.path.join(sys.prefix, "etc/jupyter/nbconfig/notebook.d"), [
            "jupyter-config/nbconfig/notebook.d/webviz_petech_page_element.json"
        ])
    ],
    test_suite="setup.discover_test_suite",
    install_requires=['webviz'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest', 'mock', 'pycodestyle', 'selenium'],
    entry_points={
        'webviz_page_elements': [
            'PetechPageElement = webviz_petech_page_element:PetechPageElement',
        ]
    },
    zip_safe=False
)
