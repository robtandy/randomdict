#!/usr/bin/env python

from setuptools import setup
import randomdict

V = randomdict.__version__

setup(name='randomdict',
      version=V,
      author='Rob Tandy',
      author_email='rob.tandy@gmail.com',
      url='https://github.com/robtandy/randomdict',
      long_description="""""",
      py_modules=['randomdict'],
      setup_requires=['nose>=1.0'],
)
