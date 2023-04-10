from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str) -> List[str]:
    '''
    This function will return the list of requirements
    '''
    requires = []
    with open(file_path)  as file_obj:
        requires = file_obj.readlines()
        requires = [req.replace('\n', '') for req in requires]
        if HYPEN_E_DOT in requires:
            requires.remove(HYPEN_E_DOT)
    return requires

setup(
    name="E2EML",
    version="1.0",
    author="Praveen Singh",
    author_email='praveensingh.soft@gmail.com',
    packages= find_packages(),
    install_requires = get_requirements('requirements.txt')
)