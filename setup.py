from setuptools import setup, find_packages

with open("README.md", "r") as f:
    description = f.read()

setup(
    name="simple-adhan",
    version="0.3",
    packages=find_packages(),
    install_requires=[
        "requests",
        "requests-cache",
    ],
    entry_points={
        "console_scripts": [
            "simple-adhan = simple_adhan:simple_adhan_init",
        ],
    },
    long_description=description,
    long_description_content_type="text/markdown",
)
