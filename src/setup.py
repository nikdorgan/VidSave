# To install, type "python ./src/setup.py py2app"
# You will find the app in the dist folder

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