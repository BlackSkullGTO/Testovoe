from setuptools import setup, find_packages

requirements = 'django==2.2\nm3-django-compat==1.9.2\nm3-objectpack==2.2.47'

setup(
    name='m3_project',
    version='0.9',
    packages=find_packages(),
    author='anton_dobrolyubov',
    description="it's just the beginning",
    install_requires=requirements
)