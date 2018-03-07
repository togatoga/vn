#!/usr/bin/env python
# -*- coding: utf-8 -*-

from shutil import copyfile

from setuptools import setup, find_packages
from setuptools.command.develop import develop
from setuptools.command.install import install

install_requires = open('requirements.txt').read().split('\n')
readme_content = open('README.md').read()


copyfile('./cmd.py', './bin/vn')


class PostInstallCommand(install):
    def run(self):
        install.run(self)
        import nltk
        nltk.download('wordnet')


setup(
    name='vn',
    version='0.0.1',
    description='vn is terminal tool to help people learn English',
    long_description=readme_content,
    author='togatoga',
    author_email='',
    license='MIT',
    keywords=['vn', 'translation'],
    url='https://github.com/togatoga/vn',
    packages=find_packages(),
    scripts=['bin/vn'],
    install_requires=install_requires,
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ],

    cmdclass={
        'install': PostInstallCommand,
    },
)
