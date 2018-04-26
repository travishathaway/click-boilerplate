#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

# This is how you will invoke the command via the command line 
# No spaces allowed, please only used letters or "-" and "_"
command_name = 'click_cli'

requirements = [
    'Click>=6.0',
]

setup(
    name=command_name,
    version='0.1.0',
    description="CLI tool boilerplate using click, please replace!",
    long_description=readme + '\n\n' + history,
    author="Travis Hathaway",
    author_email='travis@example.com',
    url='https://github.com/travishathaway/click-boilerplate',
    packages=find_packages(include=['cli_app']),
    entry_points={
        'console_scripts': [
            'click_cli=cli_app:cli'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
    keywords='click_cli',
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
    ]
)
