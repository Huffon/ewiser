from setuptools import setup, find_packages

setup(
    name='ewiser',
    version='0.1',
    packages=['ewiser'],
    url='',
    license='',
    author='Michele Bevilacqua',
    packages=find_packages(include=["ewiser", "ewiser.*"]),
    author_email='bevilacqua@di.uniroma1.it',
    description='Enhanced WSD Integrating Synset Embeddings and Relations'
)
