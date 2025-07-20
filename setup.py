from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path)->List[str]:
    """
    This function reads a requirements file and returns a list of packages.
    It ignores comments and empty lines.
    """
    requirements=[]
    with open(file_path) as file:
        requirements = file.readlines()
        [req.replace('\n','') for req in requirements]

        if '-e .' in requirements:
            requirements.remove('-e .')
            
        return requirements
setup(
    name='mlproject',
    version='0.0.1',
    author='Tilak Jilka',
    author_email='tilakjilkaus@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)