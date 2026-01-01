import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

__version__ = "0.1.0"
PACKAGE_NAME = "thesisforge"
AUTHOR = "maria2021831011"
AUTHOR_EMAIL = "ritukhan534@gmail.com"
REPO_NAME = "thesisforge"

setuptools.setup(
    name=PACKAGE_NAME,  # PyPI package name
    version=__version__,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description="A Python toolkit for thesis and academic research",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},                 
    packages=setuptools.find_packages(where="src"),  
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
)
