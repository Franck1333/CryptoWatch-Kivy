#!/usr/bin/env python
# -*- coding: UTF-8 -*-


#HOW INSTALL AND USE THIS PROJECT:
#in the console : sudo python setup.py install
#And all the depencies will be installed with the Project

from setuptools import setup, find_packages

setup(
    name='CryptoWatch-Kivy',
    version="1.13",
    author='Franck Rochat',
    author_email='rochat.franck@gmail.com',
    description='This Software allow you to get financials informations about cryptocurrencies by using Python3.',
    url='https://github.com/Franck1333/CryptoWatch-Kivy',
    license='lgpl',
    packages=find_packages(),
    include_package_data=False,
    install_requires=["cbpro","cmc","pandas","numpy","matplotlib","pydub","Cython","kivy"], #Get the Dependencies from Pypi (pip install)
    #dependency_links=[''], #Get the Dependencies via HTTP(s)
)
