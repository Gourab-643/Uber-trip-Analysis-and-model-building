from setuptools import find_packages,setup
from typing import List

hyphane_e="-e ."
def get_requires(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[i.replace("\n","") for i in requirements]
        if hyphane_e in requirements:
            requirements.remove(hyphane_e)
    return requirements

setup(
    name="Uber Trip Analysis and Prediction",
    version='0.0.1',
    author='Gourab',
    packages=find_packages(),
    install_requires=get_requires('requirement.txt')
)