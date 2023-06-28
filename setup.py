from setuptools import setup, find_packages

setup(
    name="self_aware",
    version="0.1",
    packages=find_packages() + ["code"],
    install_requires=[
        "openai"
    ],
    package_data={
        "config": ["config.json"],
    }
    # ...
)
