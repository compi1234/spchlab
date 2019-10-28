from setuptools import setup, find_packages

setup(
    name="spchlab",
    version="0.0.1",
    url="https://github.com/compi1234/spchlab",

    author="Dirk Van Compernolle",
    author_email="compi@esat.kuleuven.be",

    description="A collection of Speech Recognition Exercises in Python",
    license = "free",
    
    packages = ['spchlab'],
    py_modules = [],
    # a dictionary refering to required data not in .py files
    package_data = {},
    
    install_requires=['numpy','pandas'],

    classifiers=['Development Status: Pre-Alpha, Unstable',
                 'Programming Language :: Python :: 3.5',
                 'Programming Language :: Python :: 3.6'],
                 
    include_package_data=True

)