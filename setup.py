from setuptools import setup, find_packages

with open("requirements.txt") as file:
    requirements = file.read().splitlines()

setup(
    name="ANIME_RECOMMENDER",
    version="v0.1",
    author="Venkata Sai",
    packages=find_packages(),
    install_requires=requirements
)