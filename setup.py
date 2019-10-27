#!/usr/bin/env python
from os import path

import setuptools

from garpunauth import info


def parse_requirements(filename):
    """ load requirements from a pip requirements file """
    lineiter = (line.strip() for line in open(filename))
    return [line for line in lineiter if line and not line.startswith("#")]


here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst')) as f:
    long_description = f.read()

DEPENDENCIES = parse_requirements('requirements.txt')
print(u"setuptools.find_packages() = %s" % str(setuptools.find_packages()))
setuptools.setup(
    name=info.__package_name__,
    version=info.__version__,

    description='Garpun Authentication Library',
    long_description=long_description,

    url='https://github.com/garpun/garpun-auth-library-python',

    author='Garpun Cloud',
    author_email='support@garpun.com',

    license="Apache 2.0",

    classifiers=[
        'Programming Language :: Python :: 3'
    ],
    install_requires=DEPENDENCIES,
    python_requires=">=3.6",
    packages=['garpunauth'],
    package_data={'': ['LICENSE']},
    include_package_data=True,
)
