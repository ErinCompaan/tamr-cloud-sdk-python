# Python SDK for Tamr Cloud

DISCLAIMER: This is an in-development tool that is pre-release. This tool will not work outside of the Tamr network.

### Developers Guide

#### Virtual Env

The `.gitignore` and `Makefile` in this repo assume that you are working with a virtual
environment within the parent directory named `.sdk_env`.

To make it, run a command `python3.<minor version> -m venv .sdk_env` in the `tamr-cloud-sdk-python` directory. The minimum minor version supported can be checked by looking in the `setup.py` file. 

#### Linting, formatting, and type enforcement

Formatting and linting on pull requests are enforced via Github CI.

To run formatting and linting locally and fix any auto-fixable issues, run `make lintAndFormat` in the `tamr-cloud-sdk-python` directory.
To run linting without any auto-fixing, run `make lintAndFormat checkOnly=true`. 
