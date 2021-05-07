import os
import setuptools
from validate_pip_version import __version__

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="validate_pip_version",
    version=__version__,
    author="werzl",
    author_email="werzl.mail@gmail.com",
    description="CLI tool to validate the version of a local PIP package against its currently published version. Intended to be used as part of a CI build.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/werzl/validate-pip-version",
    packages=setuptools.find_packages(),
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "validate_pip_version = validate_pip_version.__main__:cli",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3.8",
    ],
    python_requires=">=3.6",
    install_requires=[
        "Click>=7.0"
    ],
)
