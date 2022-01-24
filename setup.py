import os

from setuptools import setup

current_directory = os.path.dirname(__file__)

with open(os.path.join(current_directory, "README.md")) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name="deloitte_api",
    version="0.0.1",
    packages=["deloitte_api"],
    include_package_data=True,
    license="Private License",
    maintainer="Rodrigo Maria Morgão",
    maintainer_email="rodrigo@rdorigomaria.com.br",
    long_description=README,
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "License :: Private",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: >=3",
    ],
    python_requires=">=3.9",
    install_requires=open(f"{current_directory}/requirements/requirements.txt").read(),
)
