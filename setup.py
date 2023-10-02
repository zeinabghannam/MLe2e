from setuptools import find_namespace_packages, setup
from typing import List



HYPTHEN_E_DOT = '-e .'

def get_requirements(file_path:str)-> List[str]:
    '''
    this fnction returns the list of requirement
    '''
    requirements = []

    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        [req.replace("\n", " ") for req in requirements]

        if HYPTHEN_E_DOT in requirements:
            requirements.remove(HYPTHEN_E_DOT)
    
    



setup(
    name="MLe2e",
    author="Zeinab Ghannam",
    version="0.0.1",
    packages=find_namespace_packages(),
    install_requires = get_requirements("requirements.txt"),

)