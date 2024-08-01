"""This file is used to create our ML application as a package. We can upload this project on PyPI, where people can download and use our project."""

from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT= '-e .'
def get_requirements(file_path: str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements= []

    with open(file_path) as file_obj:
        requirements= file_obj.readlines()
        requirements= [req.replace('\n', '') for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements



setup(
    name= 'MLDeployementProject',
    version= '0.0.1',
    author= 'Shyam',
    author_email= 'shyamchatterjee2013@gmail.com',
    packages= find_packages(),
    install_requires= get_requirements('requirements.txt')
)