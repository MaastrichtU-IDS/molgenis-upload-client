#!/usr/bin/env python

# -*- coding: utf-8 -*-

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from setuptools import setup, find_packages

setup(
    version='0.0.1',
    name='molgenis_upload_client',
    license='MIT License',
    description='Molgenis upload client for the BReIN project',
    author='Tim Hendriks',
    author_email='t.hendriks@maastrichtuniversity.nl',
    url='https://github.com/MaastrichtU-IDS/molgenis-upload-client',
    packages=find_packages(include=['molgenis_upload_client']),
    package_dir={'molgenis_upload_client': 'molgenis_upload_client'},
    entry_points={
        'console_scripts': [
            'molgenis_upload_client=molgenis_upload_client.__main__:main',
        ],
    },

    python_requires='>=3.6.0',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    include_package_data=True,
    install_requires=open("requirements.txt", "r").readlines(),
    tests_require=['pytest==5.2.0'],
    setup_requires=['pytest-runner'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ]
)
