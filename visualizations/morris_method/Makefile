all: build


.PHONY: build install
build:
	python setup.py build

dev-install:
	pip install -e .

install: build
	python setup.py install

test:
	py.test --cov=webviz_morris_method --cov-fail-under=94 tests/

lint:
	pycodestyle webviz_morris_method examples tests
