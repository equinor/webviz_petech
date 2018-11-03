from setuptools import setup, find_packages

setup(
    name='webviz_petech_page_element',
    version='0.1.0',
    packages=find_packages("."),
    package_dir={"": "."},
    package_data={
        'webviz_petech_page_element': [
            'resources/js/*',
            'resources/css/*'
        ]},
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