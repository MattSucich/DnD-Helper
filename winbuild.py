"""
py2exe build script for MyApplication.

Usage (Windows):
    python setup.py py2exe
"""
from py2exe.build_exe import py2exe
from distutils.core import setup
setup(windows=[{"script": "DnDhelper.py"}], options={"py2exe" : {"includes" : ["sip"]}})