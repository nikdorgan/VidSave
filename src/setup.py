from setuptools import setup

APP = ['./src/main.py']
OPTIONS = {
    'iconfile':'./img/icon.png',
}

setup(
    app=APP,
    name='VidSave',
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)