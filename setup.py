#!/usr/bin/env python

from os.path import join, dirname
from setuptools import find_packages, setup

with open(join(dirname(__file__), 'README.rst')) as f:
    README = f.read()

setup(
    name='django-sane-redirects',
    version='1.0.2',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    description='django.contrib.redirects without django.contrib.sites',
    long_description=README,
    url='https://github.com/feinheit/django-sane-redirects/',
    author='Matthias Kestenholz',
    author_email='mk@feinheit.ch',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
        'Framework :: Django :: 1.9',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    test_suite='testapp.runtests.runtests',
    tests_require=['Django', 'coverage'],
)
