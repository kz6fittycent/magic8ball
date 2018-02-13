#!/usr/bin/env python3

from setuptools import setup

setup(
    name="magic8ball",
    version="1.0.0",
    description="Ask the Magic 8-ball and learn your fate",
    long_description=open("README.md").read(),
    license="MIT",
    packages=["libmagic8ball"],
    scripts=["magic8ball"],
    package_data={"libmagic8ball": ["data/*"]},
)
