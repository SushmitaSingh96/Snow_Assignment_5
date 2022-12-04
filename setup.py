#from setuptools import setup
from setuptools import find_packages
from distutils.core import setup

setup(
    name='snowflake',
    version='1.0',
    packages=['snowflake'],
    url='',
    license='',
    package = find_packages(),
    author='sushmitasingh',
    author_email='sushmitasingh1996@gmail.com',
    install_requires=["numpy","turtles"],
    description='setup.py for Snowflake '
)
