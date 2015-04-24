"""Setup script."""
from setuptools import setup, find_packages


setup(
    name="tgif",
    packages=find_packages(),

    author="Ahbong Chang",
    author_email="cwahbong@gmail.com",
    description="Friday boardgame implementation.",
    license="MIT",
    url="https://github.com/cwahbong/tgif-py",

    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Topic :: Games/Entertainment :: Board Games",
    ],
)
