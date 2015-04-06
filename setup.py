#!/usr/bin/env python
# coding: utf8

from setuptools import setup

setup(
    name='django-skin',
    version='0.1dev',
    packages=['skin', ],
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
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    test_suite='nose.collector',
    tests_require=[
        'nose',
        'mock'
    ],
)
