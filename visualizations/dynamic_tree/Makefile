all: build


.PHONY: build install
build:
	npm install && npm run build && python setup.py build

dev-install:
	pip install -e .

install: build
	python setup.py install

test:
    python ./examples/dynamic_tree_example.py
	py.test --cov=webviz_dynamic_tree --cov-fail-under=90 tests/
	npm run test

lint:
	pycodestyle webviz_dynamic_tree examples tests
	npm run lint

