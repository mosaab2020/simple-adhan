from setuptools import setup, find_packages

setup(
    name="simple_adhan",
    version="0.2",
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
)
