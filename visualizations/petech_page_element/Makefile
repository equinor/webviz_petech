all: build


.PHONY: build install
build:
	python setup.py build

dev-install:
	pip install -e .

install: build
	python setup.py install

test:
	py.test --cov=webviz_petech_page_element --cov-fail-under=60 tests/

lint:
	pycodestyle webviz_petech_page_element tests
