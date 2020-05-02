import subprocess
from sys import platform
import os
from setuptools import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()
with open("README.md","r") as f:
    long_description = f.read()

version = "0.2.0"
setup(name='chatbook',
  version=version,
  description='chatbook: Dialogue agent handling queries about a given text document',
  long_description = long_description,
  long_description_content_type='text/markdown',
  url='https://github.com/ptarau/chatbook.git',
  author='Paul Tarau',
  author_USER_EMAIL='<paul.tarau@gmail.com>',
  license='Apache',
  packages=['chatbook'],
  package_data={'examples': ['*.json']},
  include_package_data=True,
  install_requires = required,
  zip_safe=False
  )

