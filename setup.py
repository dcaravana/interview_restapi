# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='SKUSentimentAPI',
    version='0.1',
    description='Simple Restful API that takes and stores comments identified by an SKU, applying sentiment analysis on them.',
    long_description=readme,
    author='Diego Caravana',
    author_email='diego@caravana.to',
    url='https://diego.caravana.to/',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
