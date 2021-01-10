import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pasteAPI-NickDay04", # Replace with your own username
    version="0.0.1",
    author="Nicholas Day",
    author_email="nicholas.day2004.nd@gmail.com",
    description="A package to simplify interacting with the Pastebin API",
    long_description=None,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)