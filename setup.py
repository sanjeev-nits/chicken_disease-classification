from setuptools import setup, find_packages 
from typing import List
def get_requirements(file_path: str) -> List[str]:
    """
    This function reads a requirements file and returns a list of requirements.
    It removes any comments and empty lines.
    """
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
    
        if '-e .' in requirements:
            requirements.remove('-e .')
            
    return requirements


    




setup(
    name='chicken_disease_classification',
    version='0.1.0',
    author='sanjeev',
    author_mail='saneevkumar814155@gmail.com',
    find_packages= find_packages(),  
    install_requires=get_requirements('requirements.txt')
)