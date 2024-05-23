from setuptools import setup, find_packages

setup(
    name="deepdiggin",
    version="0.1",
    author="Juan Valero",
    packages=find_packages(),
    install_requires=[
        "transformers>=4.41.1",
        "transformers[torch]"
        ],
)