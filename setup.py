import re
from codecs import open
from os import path

from setuptools import find_packages, setup

PACKAGE_NAME = "zarena_translate"
HERE = path.abspath(path.dirname(__file__))

with open("README.md", "r", encoding="UTF-8") as f:
    README = f.read()
with open(path.join(HERE, PACKAGE_NAME, "const.py"), encoding="utf-8") as fp:
    VERSION = re.search('__version__ = "([^"]+)"', fp.read()).group(1)

setup(
    name="zarena-translate",
    version=VERSION,
    author="itsbravestone",
    author_email="imbravestone@zarena.ga",
    description="A translator for google translator.",
    install_requires=["requests", "six"],
    license="MIT License",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/itsbravestone/zarena-translate",
    packages=find_packages(),
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Libraries",
        "Topic :: Utilities",
    ],
)
{"mode":"full","isActive":false}
