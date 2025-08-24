from setuptools import find_packages,setup
hyphen_e="-e ."
def get_requirements(file_path):
    # this function willreturn the list of requirements
    requirements=[]
    with open("requirements.txt",mode="r") as prerequisites:
        #readlines will give it in the list
        requirements=prerequisites.readlines() # whenever u readlines \n will also append with pandas as pandas\n like that
        for req in requirements:
            req.replace("\n","")
        if hyphen_e in requirements:
            requirements.remove(hyphen_e)
        return requirements




setup(
    name="mlproject",
    version="0.0.1",
    author= "Ramprasad Muthurajan",
    author_email="ramprasaddk05@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt") #[it will automatically install the necessary module when the mlproject module is being installed as prerequisites]
    
)
#install_requires=["pandas","numpy","seaborn"]