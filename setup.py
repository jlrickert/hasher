import os
import sys

from setuptools import setup
from setuptools.command.test import test as TestCommand

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.rst')) as f:
    readme = f.read()
with open(os.path.join(here, 'LICENSE')) as f:
    license = f.read()

setup(
    name='hasher',
    version='0.0.0',
    url='https://github.com/jlrickert/hasher',
    license=license,
    author='Jared Rickert',
    author_email='jaredrickert52@gmail.com',
    description='calculates hashes for a file',
    long_description=readme,
    entry_points={
        'console_scripts': [
            'hasher = hasher.__main__:main'
        ]
    },
    platforms='any',
    packages=['hasher'],
    install_requires=[],
    classifiers=[
        'Natural Language :: English',
        'Environment :: Console',
        'Intended Audience :: System Administrators',
        'Programming Language :: Python',
    ],
)
