"""Setup script for package installation."""

from setuptools import setup

setup(
    name="tamr-cloud-sdk",
    python_requires=">3.8",
    version="0.1.0",
    description="Package for interacting with Tamr Cloud APIs",
    author="Tamr",
    author_email="colin.reynolds@tamr.com",
    packages=["tamr_sdk", "tamr", "protoc_gen_openapiv2"],
)
