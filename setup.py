#!/usr/bin/env python
import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name='phantomjs-binary',
    version='2.1.3',
    description='A pip package for installing binary files of phantomjs',
    long_description=long_description,
    author='jayjiahua',
    author_email='jayjhwu@gmail.com',
    url='https://github.com/jayjiahua/phantomjs-bin-pip',
    packages=['phantomjs_bin'],
    include_package_data=True,
)
