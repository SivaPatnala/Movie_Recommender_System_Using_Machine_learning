from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

AUTHOR_NAME = 'SIVA'
SRC_REPO = 'SRC'
LIST_OF_REQUIREMENTS = ['streamlit']

setup(
    name=SRC_REPO,
    version='0.0.1',
    author=AUTHOR_NAME,
    author_email='subbupatnala98@gmail.com',
    description='A small example package for movie recommendation',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=[SRC_REPO],  # Fixed the 'packages' argument
    python_requires='>=3.6',  # Updated Python version requirement
    install_requires=LIST_OF_REQUIREMENTS,
)
