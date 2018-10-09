# Webviz petroleum technology plugins [![Build Status](https://travis-ci.com/Statoil/webviz_petech.svg?branch=master)](https://travis-ci.com/Statoil/webviz_petech)

This repository contains [webviz](https://github.com/Statoil/webviz) plugins
relevant for petroleum technology. Specific plugins might at some later
point in time be transferred from this repository to the main
[webviz repository](https://github.com/Statoil/webviz).

From a user point of view, plugins are imported similarly regardless of it
being one from the main repository or "pure plugin repositories" like this one.
After installation, e.g. the history match visualization from this repository
can be imported as
```python
from webviz.page_elements import HistoryMatch
```
To compare, the `Map` visualization from the main repository is imported as
```python
from webviz.page_elements import Map
```

## Installation

python dependencies can be installed with

    pip install -r requirements.txt

In addition, you will need to have [webviz](https://github.com/Statoil/webviz)
itself installed.

After dependencies are installed you can do

    make build && make install

## Develop

In order to run the tests of the project, it is necessary to install
some additional requirements:

    pip install -r dev-requirements.txt

This involves also installing the
[selenium chrome driver](https://github.com/SeleniumHQ/selenium/wiki/ChromeDriver).

Packages can be installed in-place which speeds up your feedback loop:

    make dev-install

Or you can pass in whatever argument you would like by using this format

    make install ARGS=argument
