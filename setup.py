import subprocess
from sys import platform
import os
from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()
with open("README.md","r") as f:
    long_description = f.read()

version = "0.2.4"
setup(name='chatbook',
  version=version,
  description='chatbook: Dialogue agent handling queries about a given text document',
  long_description = long_description,
  long_description_content_type='text/markdown',
  url='https://github.com/ptarau/chatbook.git',
  author='Paul Tarau',
  author_email='<paul.tarau@gmail.com>',
  license='Apache',
  packages=find_packages(),
  include_package_data=False,
  install_requires = required,
  zip_safe=False
  )

