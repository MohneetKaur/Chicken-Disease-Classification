import setuptools # package development library used for packaging and distribution of Python projects


# This line opens the file named "README.md" in read mode ("r") with the specified encoding ("utf-8"). It uses a context manager (with) to ensure proper file handling and automatically close the file after reading.
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read() # reads the contents of the "README.md" file and assigns it to the long_description variable.


__version__ = "0.0.0"

REPO_NAME = "Chicken-Disease-Classification"
AUTHOR_USER_NAME = "MohneetKaur"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "mohneetkaursandhu@gmail.com"


# starts the setup configuration for the project/package using the setup() function from setuptools
setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app",
    long_description=long_description,
    long_description_content="text/markdown", # specifies the type of the long description content, which is Markdown text.
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues", # specifies additional project URLs, such as the bug tracker, which is set to the issues page of the project's repository
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)