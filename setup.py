#!/usr/bin/env python
import os
import platform
import shutil
import stat

import setuptools
from setuptools.command.install import install as install_base


with open("README.md", "r") as fh:
    long_description = fh.read()


class install(install_base):
    def run(self):
        os_type_mapping = {
            "Windows": {
                "dir": "windows",
            },
            "Darwin": {
                "dir": "macosx",
            },
            "Linux": {
                "dir": "linux",
            },
        }

        setup_path = os.path.dirname(os.path.abspath(__file__))
        bin_dir = os.path.join(setup_path, "bin")
        install_dir = os.path.join(setup_path, "phantomjs_bin", "bin")

        os_type = platform.system()
        os_bits = platform.architecture()[0]

        if os_type not in os_type_mapping:
            raise EnvironmentError("Unsupported system type: %s" % os_type)

        if os_type == 'Windows':
            installed_bin_filename = "phantomjs.exe"
        else:
            installed_bin_filename = "phantomjs"

        os_info = os_type_mapping[os_type]
        bin_path = os.path.join(bin_dir, os_info["dir"], installed_bin_filename)

        if not os.path.exists(install_dir):
            os.mkdir(install_dir)

        install_path = os.path.join(install_dir, installed_bin_filename)
        # move bin file
        shutil.copyfile(bin_path, install_path)

        # make executable
        st = os.stat(install_path)
        os.chmod(install_path, st.st_mode | stat.S_IEXEC)

        install_base.run(self)


setuptools.setup(
    name='phantomjs-binary',
    version='1.0',
    description='A pip package for installing binary files of phantomjs',
    long_description=long_description,
    author='jayjiahua',
    author_email='jayjhwu@gmail.com',
    url='https://github.com/jayjiahua/phantomjs-bin-pip',
    packages=['phantomjs_bin'],
    include_package_data=True,
    cmdclass={'install': install},
)
