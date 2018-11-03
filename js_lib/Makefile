all: build


build:
	npm install && npm run build:js

dev-install: build
	cp build/webviz_petech.js ../visualizations/petech_page_element/webviz_petech_page_element/resources/js/
	cp src/webviz_petech.css ../visualizations/petech_page_element/webviz_petech_page_element/resources/css/

install: build
	cp build/webviz_petech.js ../visualizations/petech_page_element/webviz_petech_page_element/resources/js/
	cp src/webviz_petech.css ../visualizations/petech_page_element/webviz_petech_page_element/resources/css/

test:
	npm run test

lint:
	npm run lint
