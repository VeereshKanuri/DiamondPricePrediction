from setuptools import find_packages,setup
from typing import List

hypen_dot_e='-e .'


def get_requiremnts(file_path:str)-> List[str]:
    
    with open(file_path) as file:
        requirements= file.readlines()
        requirements=[req.replace('\n','') for req in requirements]
        
        if hypen_dot_e in requirements:
            requirements.remove(hypen_dot_e)
        return requirements


setup(
    
    name='DiamondPricePrediction',
    version='0.0.1',
    author='veeresh',
    author_email='veeresh2809@gmail.com',
    install_requires=get_requiremnts('requirements.txt'),
    pacakges = find_packages()
    
    
    
)