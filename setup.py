#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='django-bones',
    version='.'.join(map(str, __import__('bones').__version__)),
    author='Garet McKinley',
    author_email='garetmckinley@me.com',
    url='https://github.com/mediachicken/django-bones',
    description='A bare bones blogging app for Django',
    packages=find_packages(),
    zip_safe=False,
    install_requires=[],
    include_package_data=True,
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)
