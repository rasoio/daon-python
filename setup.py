from setuptools import setup, find_packages
import os

setup(name='daon',
      version='0.1',
      description='Daon Korean Analyzer',
      url='http://github.com/rasoio/daon-python',
      author='rasoio',
      author_email='rasoio@naver.com',
      license='MIT',
      install_require=['py4j'],
      packages=find_packages(exclude=['contrib', 'docs', 'tests']),
      zip_safe=False)
