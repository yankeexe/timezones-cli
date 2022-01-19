"""Package setup"""
import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

requirements = [
    "click",
    "tabulate",
    "rich<=7.1.0",
    "pycountry",
    "pytz",
    "simple-term-menu",
    "tzlocal",
]

# Development Requirements
requirements_dev = [
    "pytest<=4.*",
    "black<=20.8b1",
    "pre-commit",
    "mypy",
]

setuptools.setup(
    name="timezones_cli",
    version="0.2.4",
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
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
    ],
)
