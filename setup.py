#!/usr/bin/env python

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='PhantomJS Binary',
    version='1.0',
    description='A pip package for installing binary files of phantomjs',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='jayjiahua',
    author_email='jayjhwu@gmail.com',
    url='https://github.com/jayjiahua/phantomjs-bin-pip',
    packages=['phantomjs_bin'],
    include_package_data=True,
)