# Makefile six

PIP=$(VIRTUAL_ENV)/bin/pip 
PY=$(VIRTUAL_ENV)/bin/python

.PHONY: clean-pyc clean-build docs pack clean clean-others

help:
	@echo "clean - remove all build, test, coverage and Python artifacts"


clean: clean-build clean-others clean-pyc clean-test clean-runtime
distclean: clean-build clean-others clean-pyc clean-test clean-runtime clean-database

clean-database:
	rm -fr database/backups/*
	rm -fr database/fixtrues/*

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	rm -rf '*.tgz'
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +
	find . -name '*.log' -exec rm -f {} +
	find . -name '*.sql' -exec rm -f {} +

clean-others:
	find . -name 'Thumbs.db' -exec rm -f {} \;

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	rm -rf .tox/
	rm -rf .coverage
	rm -rf htmlcov/

clean-runtime:
	rm -fr .runtime/**/**

# DO NOT DELETE
