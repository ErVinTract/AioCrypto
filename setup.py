#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import sys
import pathlib
from setuptools import setup, find_packages

WORK_DIR = pathlib.Path(__file__).parent

# Check python version
MINIMAL_PY_VERSION = (3, 8)
if sys.version_info < MINIMAL_PY_VERSION:
    raise RuntimeError(
        'AioCrypto works only with Python {}+'.format('.'.join(map(str, MINIMAL_PY_VERSION))))


def get_version() -> str:
    """
    Read version
    :return: str
    """
    txt = (WORK_DIR / 'aiocrypto' / '__init__.py').read_text('utf-8')
    try:
        return re.findall(r"^__version__ = '([^']+)'\r?$", txt, re.M)[0]
    except IndexError:
        raise RuntimeError('Unable to determine version.')


def get_description() -> str:
    """
    Read full description from 'README.rst'
    :return: description
    :rtype: str
    """
    with open('README.rst', 'r', encoding='utf-8') as f:
        return f.read()


setup(
    name='AioCrypto',
    version=get_version(),
    packages=find_packages(exclude=[
        'tests', 'tests.*', 'examples.*', 'docs']),
    url='https://github.com/ErVinTract/AioCrypto',
    license='Apache2',
    author='ErVinTract',
    author_email='ErVinTract@gmail.com',
    description='Async Crypto API for humans',
    long_description=get_description(),
    long_description_content_type="text/x-rst",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Framework :: AsyncIO',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    install_requires=[
        'aiohttp>=3.8.0,<3.9.0',
    ],
    python_requires=">=3.8",
)
