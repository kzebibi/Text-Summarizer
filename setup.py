from setuptools import find_packages, setup
from typing import List

# Read the contents of the README file for the long description
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# Define a constant for a specific requirement
HYPHEN_E_DOT = '-e .'

def get_requirements(file_path):
    """
    Retrieve the list of requirements from a file.
    
    Args:
        file_path (str): Path to the requirements file.
    
    Returns:
        list: List of requirements.
    """
    requirements = []
    with open(file_path, encoding='utf-8') as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements

# Setup configuration for the package
setup(
    name='Text-Summarizer',
    version='0.0.1',
    author='Khaled Zebibi',
    author_email='khaledzebibi@gmail.com',
    description='A text summarization tool.',
    long_description=long_description,
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    url='https://github.com/kzebibi/Text-Summarizer.git'
)