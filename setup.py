"""
Copyright 2019, All rights reserved.
Author : SangJae Kang
Mail : rocketgrowthsj@gmail.com
"""
import io
from setuptools import find_packages, setup


def long_description():
    with io.open("README.md", 'r', encoding='utf-8') as f:
        readme = f.read()
    return readme


setup(name="publicai",
      version='0.1',
      description='quiz and practice for learning ai',
      long_description=long_description(),
      license='MIT',
      author="rocketgrowthsj",
      author_email='rocketgrowthsj@publicai.co.kr',
      url="https://github.com/public-ai/publicai-learntools",
      install_requires=[
          "pandas>=0.25",
          "numpy>=1.16",
          "requests>=2.22"],
      packages=find_packages(),
      classifiers=[
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.6'],
      zip_safe=False)