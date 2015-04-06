#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='assertionchain',
    description='Utility for chaining commands and incrementally checking the results',
    version='0.1.0',
    author='Justin Iso',
    author_email='justin+assertionchain@justiniso.com',
    url='https://github.com/justiniso/assertionchain',
    download_url='https://github.com/justiniso/assertionchain/tarball/0.1.0',
    packages=find_packages(),
    install_requires=[],
    tests_require=[],
    test_suite='tests',
    setup_requires=[]
)