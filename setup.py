"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['main.py']
APP_NAME = "Asteroid Evader"
DATA_FILES = [('', ['assets']),('', ['fonts']),('', ['fx']),('', ['music']),('', ['screens'])]
OPTIONS = {
    'argv_emulation': True,
    'iconfile': 'icon.icns'
}
setup(
    app=APP,
    name=APP_NAME,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
