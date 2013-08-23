#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
    setup.py
    ~~~~~~~~

"""


import os
import sys
from setuptools import Command, setup, find_packages


dioc = __import__('dioc')
readme = os.path.abspath(os.path.join(os.path.dirname(__file__), 'README.rst'))

try:
   long_description = open(readme).read()
except IOError as e:
   sys.stderr.write("File not found for long description: {}".format(readme))
   sys.exit(1)

install_requires = [
    'cliff',
    'python-digitalocean',
]


class CleanSDist(Command):
    description = "Remove traces of setup.py sdist"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import glob
        import shutil
        shutil.rmtree('dist', True)
        for each_dir in glob.glob(os.path.join('.', '*egg*info*')):
            shutil.rmtree(each_dir, True)


setup(
    name='dioc',
    version=dioc.version(),
    url='https://github.com/dustinrc/dioc',
    author='Dustin Chapman',
    author_email='dustin.r.chapman@gmail.com',
    description=dioc.__doc__,
    long_description=long_description,
    zip_safe=False,
    packages=find_packages(),
    scripts=[],
    test_suite='',
    install_requires=install_requires,
    provides=['dioc'],
    platforms=['Any'],
    include_package_data=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Intended Audience :: Developers',
        'Environment :: Console',
    ],
    entry_points={},
    cmdclass={'clean_sdist': CleanSDist}
)
