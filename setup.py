from setuptools import find_namespace_packages,setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    try:
        with open(file_path, "r") as file_obj:
            requirements = file_obj.readlines()
            requirements = [req.strip() for req in requirements if req.strip() and not req.startswith("#")]
        return requirements
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        return []

setup(
    name='Diamond_Price_Prediction',
    version='0.0.1',
    author='Azeembo',
    author_email='bambam@gmail.com',
    description='A package for predicting diamond prices.',
    url='https://github.com/your-repo-url',
    install_requires=get_requirements('requirements.txt'),
    packages=find_namespace_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
