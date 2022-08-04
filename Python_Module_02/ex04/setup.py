import setuptools
import os

setuptools.setup(
    name="my-minipack",
    version="1.0.0",
    description="Howto create a package in python.",
    url="None",
    author="Sungyong Cho",
    author_email="sucho@student.42.fr",
    license="FAKE",
    Location=os.getenv("PATH"),
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Students",
        "Topic :: Education",
        "Topic :: HowTo",
        "Topic :: Package",
        "License :: FAKE",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
    ],
)
