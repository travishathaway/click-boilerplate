#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = [
    'Click>=6.0',
]

setup(
    name='cli_app',
    version='0.1.0',
    description="CLI tool boilerplate using click, please replace!",
    long_description=readme,
    author="Travis Hathaway",
    author_email='travis@example.com',
    url='https://github.com/travishathaway/click-boilerplate',
    packages=find_packages(include=['cli_app']),
    entry_points={
        # ATTENTION! ACHTUNG! ATENCIÓN!
        # 
        # The following lines determine what your CLI program is 
        # called and where it will look for it. Please edit to suit
        # your needs
        'console_scripts': [
            'cli_app=cli_app:cli'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
    keywords='cli_app',
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
    ]
)
