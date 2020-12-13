#!/usr/bin/env python
# setup.py generated by flit for tools that don't yet use PEP 517

from distutils.core import setup

packages = ["pyrostarter"]

package_data = {"": ["*"]}

extras_require = {"publish": ["flit"]}

entry_points = {"console_scripts": ["pyrostarter = pyrostarter.pyrostarter:main"]}

setup(
    name="pyrostarter",
    version="0.1.0",
    description="A CLI tool for creating Pyrogram project file structure",
    author="ahmetveburak",
    url="https://github.com/ahmetveburak/pyrostarter",
    packages=packages,
    package_data=package_data,
    extras_require=extras_require,
    entry_points=entry_points,
    python_requires=">=3.7.0",
)
