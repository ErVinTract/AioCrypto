#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from os import path
from setuptools import setup, find_packages

this_directory = path.abspath(path.dirname(__file__))

setup(
    name='AioCrypto',
    description='Async Crypto API for humans',
    version='1.0',
    url='https://github.com/ErVinTract/AioCrypto',
    author='ErVinTract',
    author_email='ErVinTrac@gmail.com',
    license='Apache2',
    classifiers=[
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3'
    ],
    packages=find_packages(include=['aiocrypto']),
    install_requires=[
        'aiohttp',
    ],
    python_requires=">=3.8",
)
