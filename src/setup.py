"""
Usage (Mac OS X): python setup.py py2app

Usage (Windows): python setup.py py2exe
"""

import sys
from setuptools import setup

APP = ['main.py']

if sys.platform == 'darwin':
    extra_options = dict(
        setup_requires=['py2app'],
        app=APP,
    )

elif sys.platform == 'win32':
    extra_options = dict(
        setup_requires=['py2exe'],
        app=APP,
    )

else:
    extra_options = dict(
        scripts=APP,
    )

setup(
    name="VidSave",
    **extra_options,
    options={
        'iconfile': 'icon.icns',
    }
)
