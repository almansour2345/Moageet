
from setuptools import setup, find_packages

 

setup(

     name='moageet',

     version='7.0.0',

     description='Moageet al salah',


     author='Mansour A Almansour',

     author_email='almansour2345@gmail.com',

     license='MIT',

     packages=find_packages(exclude=['']),

     install_requires=['requests'],
 
#     entry_points={
#        'gui_scripts': [
#
#             'moagit=__main__:main'
#		]
#	}

)
