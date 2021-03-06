"""Setup module for building Peyton."""

from setuptools import find_packages, setup

setup(
    name="peyton",
    version="0.1.9",
    packages=find_packages(exclude=["test*", "performance*"]),
    license="MIT",
    long_description=open("README.md").read(),
    author="M. Moon",
    description="A lightweight framework for AWS Lambda for building Rest APIs",
    author_email="moon.maxwell@gmail.com",
)
