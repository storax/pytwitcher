#!/usr/bin/env python

from __future__ import print_function

import io
import os
import sys

from setuptools import find_packages, setup
from setuptools.command.test import test as TestCommand

here = os.path.abspath(os.path.dirname(__file__))


ispy2 = sys.version_info[0] == 2


def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)


class Tox(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import tox
        errcode = tox.cmdline(self.test_args)
        sys.exit(errcode)


long_description = read('README.rst', 'HISTORY.rst')
install_requires = ['pytwitcherapi', 'livestreamer', 'pyside', 'easymodel']
if ispy2:
    install_requires.append('futures')
tests_require = ['tox']


setup(
    name='pytwitcher',
    version='0.1.0',
    description='Python application for watching twitch.tv',
    long_description=long_description,
    author='David Zuber',
    author_email='zuber.david@gmx.de',
    url='https://github.com/Pytwitcher/pytwitcher',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    package_data={'pytwitcherapi': ['data/icons/*.png']},
    include_package_data=True,
    tests_require=tests_require,
    install_requires=install_requires,
    entry_points={
        'console_scripts': ['pytwitcher = pytwitcher.app:exec_app'],
        'gui_scripts': ['pytwitcher = pytwitcher.app:exec_app']},
    cmdclass={'test': Tox},
    license='BSD',
    zip_safe=False,
    keywords='pytwitcher',
    test_suite='pytwitcher.test.pytwitcher',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Operating System :: OS Independent',
    ],
)
