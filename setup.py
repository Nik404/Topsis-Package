import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="TOPSIS-Nikhal-101816034", 
    version="0.0.1",
    author="Nikhal Singh",
    description="Python Package Implementing TOPSIS (for finding ideal and anti-ideal solution)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Nik404/Topsis-Package",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)