from pip.req import parse_requirements
from setuptools import setup, find_packages

setup(
    name='snorkel',
    description='snorkel',
    packages=find_packages(),
    install_requires=[
        "bs4",
        "future",
        "futures",
        "ipywidgets>=7.0",
        "jupyter",
        "lxml==3.6.4",
        "matplotlib",
        "nltk",
        "numba",
        "numpy>=1.11",
        "pandas",
        "requests",
        "scipy>=0.18",
        "six",
        "sqlalchemy>=1.0.14",
        "tensorflow>=1.0",
        "tika",
        "spacy==1.10.0",
        "psycopg2",
        "py4j",
    ],
    dependency_links=[
        "git+https://github.com/HazyResearch/numbskull@5219238",
        "git+https://github.com/HazyResearch/treedlib@b893c5b",
    ]
)
