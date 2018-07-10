
from setuptools import setup, find_packages

 

setup(

     name='moageet',

     version='7.2.0',

     description='Moageet al salah',


     author='Mansour A Almansour',

     author_email='almansour2345@gmail.com',

     license='MIT',
     packages=find_packages(),
     #packages=find_packages(exclude=['']),
     scripts=['main.py'],
     install_requires=['requests>=2.18.4','pygobject>=3.26.1'],
#     entry_points={
#        'gui_scripts': [
#
#             'moagit=__main__:main'
#		]
#	}

)
