#!/usr/bin/env python
import os
import sys
from codecs import open
from setuptools import setup
from garpunauth import info

if sys.version_info < (3, 6, 0):
    print("Python 3.6+ is required")
    exit(1)

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, "README.rst")) as f:
    long_description = f.read()

DEPENDENCIES = ["oauth2client"]

setup(
    name=info.__package_name__,
    version=info.__version__,
    description="Garpun Authentication Library",
    long_description=long_description,
    url="https://github.com/garpun/garpun-auth-library-python",
    author="Garpun Cloud",
    author_email="support@garpun.com",
    license="Apache 2.0",
    zip_safe=False,
    classifiers=[
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3 :: Only",
    ],
    install_requires=DEPENDENCIES,
    python_requires=">=3.5",
    packages=["garpunauth"],
    package_data={"": ["LICENSE"]},
    include_package_data=True,
)
