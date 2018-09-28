from setuptools import setup, find_packages

setup(
    name='webviz_history_match',
    version='0.1.0',
    packages=find_packages("."),
    package_dir={"": "."},
    package_data={
        'webviz_history_match': [
            'templates/*',
            'resources/js/*',
            'resources/css/*'
        ]},
    test_suite="setup.discover_test_suite",
    install_requires=['jinja2', 'webviz', 'numpy', 'scipy'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest', 'mock', 'pycodestyle', 'selenium'],
    entry_points={
        'webviz_page_elements': [
            'HistoryMatch = webviz_history_match:HistoryMatch',
        ]
    },
    zip_safe=False
)

