#!/usr/bin/env python

from os.path import join, dirname
from setuptools import find_packages, setup

with open(join(dirname(__file__), "README.rst")) as f:
    README = f.read()

setup(
    name="django-sane-redirects",
    version=__import__("sane_redirects").__version__,
    packages=find_packages(exclude=["tests", "testapp"]),
    include_package_data=True,
    license="MIT License",
    description="django.contrib.redirects without django.contrib.sites",
    long_description=README,
    url="https://github.com/feinheit/django-sane-redirects/",
    author="Matthias Kestenholz",
    author_email="mk@feinheit.ch",
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
)
