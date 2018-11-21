#!/Users/leisen/anaconda3/bin/python3
# -*- coding: UTF-8 -*-

# ********************************************************
# * Author        : LEI Sen
# * Email         : sen.lei@outlook.com
# * Create time   : 2018-11-21 15:48
# * Last modified : 2018-11-21 15:48
# * Filename      : setup.py
# * Description   : 
# *********************************************************

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dplearn",
    version="1.0",
    author="Sen LEI",
    author_email="sen.lei@outlook.com",
    description="An useful package for data analysis. ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/...",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
