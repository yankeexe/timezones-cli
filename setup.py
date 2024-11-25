"""Package setup"""

import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

requirements = [
    "click==8.1.5",
    "tabulate==0.9.0",
    "rich<=7.1.0",
    "pycountry==22.3.5",
    "pytz",
    "simple-term-menu==1.6.1",
    "tzlocal==2.1",
    "thefuzz[speedup]",
]

# Development Requirements
requirements_dev = [
    "pytest>=6.2.5",
    "black<=20.8b1",
    "pre-commit",
    "mypy",
    "freezegun",
    "flake8",
    # types
    "types-pytz",
    "types-tzlocal",
    "types-tabulate",
]

setuptools.setup(
    name="timezones_cli",
    version="0.3.3",
    author="Yankee Maharjan",
    url="https://github.com/yankeexe/timezones-cli",
    description="Get local datetime from multiple timezones!",
    license="MIT",
    packages=setuptools.find_packages(exclude=["dist", "build", "*.egg-info", "tests"]),
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=requirements,
    extras_require={"dev": requirements_dev},
    entry_points={"console_scripts": ["tz = timezones_cli.main:cli"]},
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable"
        "License :: OSI Approved :: MIT License",
    ],
)
