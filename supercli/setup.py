from importlib_metadata import entry_points
from setuptools import find_packages, setup

setup(
    name='supercli',
    version='0.0.0',
    packages=find_packages(),
    install_requires=[
        'click'
    ],
    entry_points='''
    [console_scripts]
    super=supercli:supercli
    '''
)
