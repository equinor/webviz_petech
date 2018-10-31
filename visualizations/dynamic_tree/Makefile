all: build


.PHONY: build install
build:
	python setup.py build

dev-install:
	pip install -e .

install: build
	python setup.py install

test:
	py.test --cov=webviz_dynamic_tree --cov-fail-under=90 tests/

lint:
	pycodestyle webviz_dynamic_tree examples tests
