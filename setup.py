from setuptools import setup
import os

os.environ['PBR_VERSION'] = '0.3.9.twisto.2'

setup(
    setup_requires=['pbr'],
    pbr=True)
