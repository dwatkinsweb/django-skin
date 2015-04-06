#!/usr/bin/env python
# coding: utf8

from __future__ import with_statement
from setuptools import setup, find_packages


# Figure out the version; this could be done by importing the
# module, though that requires dependencies to be already installed,
# which may not be the case when processing a pip requirements
# file, for example.
def parse_version(assignee):
    import os
    import re

    here = os.path.dirname(os.path.abspath(__file__))
    version_re = re.compile(
        r'%s = (\(.*?\))' % assignee)
    with open(os.path.join(here, 'skin', '__init__.py')) as fp:
        for line in fp:
            match = version_re.search(line)
            if match:
                version = eval(match.group(1))
                return ".".join(map(str, version))
        else:
            raise Exception("cannot find version")


setup(
    name='django-skin',
    version=parse_version('__version__'),
    packages=find_packages(),
    url='https://github.com/dwatkinsweb/django-skin',
    license='MIT',
    author='David Watkins',
    author_email='dwatkinsweb@gmail.com',
    description='Add template skins to django.',
    platforms='any',
    install_requires=[
        'Django==1.6'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    test_suite='nose.collector',
    tests_require=[
        'nose',
        'mock'
    ],
)
