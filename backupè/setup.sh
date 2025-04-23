#!/bin/bash
git remote remove origin
git remote add origin https://github.com/davidecantoro/test_documentation
pip install Sphinx
pip install sphinx sphinx_rtd_theme
touch Docs
cd Docs
sphinx-quickstart
