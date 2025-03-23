from setuptools import setup, find_packages

setup(
    name="audio-controller",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pygame",
    ],
    author="Harshitha",
    author_email="harshitha.atra1306@gmail.com",
    description="A simple Python library to play, pause, and stop audio.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Harshitha-atra/audio-control-lib.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
