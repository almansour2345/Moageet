
from setuptools import setup, find_packages

 

setup(

     name='moagit',

     version='2.0.0',

     description='Moagit al salah',


     author='Mansour A Almansour',

     author_email='almansour2345@gmail.com',

     license='MIT',

     packages=find_packages(exclude=['']),

     install_requires=['requests','tk'],
	 classifiers=[
			# How mature is this project? Common values are
			#   3 - Alpha
			#   4 - Beta
			#   5 - Production/Stable
			'Development Status :: 3 - Alpha',

			# Indicate who your project is intended for
			'Intended Audience :: Developers',
			'Topic :: Software Development :: Build Tools',

			# Pick your license as you wish (should match "license" above)
			'License :: OSI Approved :: MIT License',

			# Specify the Python versions you support here. In particular, ensure
			# that you indicate whether you support Python 2, Python 3 or both.
			'Programming Language :: Python :: 2',
			'Programming Language :: Python :: 2.7',
			'Programming Language :: Python :: 3',
			'Programming Language :: Python :: 3.3',
			'Programming Language :: Python :: 3.4',
			'Programming Language :: Python :: 3.5',
		],
		py_modules=['Tkinter','Tkconstants','sys','commands','time','datetime','requests'],
#     entry_points={
#        'gui_scripts': [
#
#             'moagit=__main__:main'
#		]
#	}

)
