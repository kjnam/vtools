
"""vtools setup file"""

import ez_setup
ez_setup.use_setuptools()
from setuptools import setup,find_packages

# Metadata
PACKAGE_NAME = "vtools"
PACKAGE_VERSION = "1.0"
PACKAGES = ['datastore','data','examples','functions','datastore.dss']

setup(
    name=PACKAGE_NAME,
    version=PACKAGE_VERSION,
    url = "http://bdo.water.ca.gov",
    description='time series manipulation tools',
    #long_description = get_description(),
    author="Eli Ateljevich, Qiang Shu", 
    author_email="eli@water.ca.gov",
    license="PSF or ZPL",
    install_requires = ['setuptools'],
    packages=find_packages(),
    namespace_packages=['vtools','vtools.datastore','vtools.datastore.dss'],
    package_data={"vtools.datastore.dss":["doc/*.*","doc/html/*.*","*.pyd","*test/backup_dssfile/testfile.dss"],
	              "":["doc/*.*","doc/html/*.*","*.pyd"]},
    exclude_package_data = {'': ['*.pyc','*.pyo']},
    entry_points = {
        'console_scripts': [
            'transfer = vtools.datastore.transfer:main'
        ]},
      test_suite = "nose.collector",
      tests_require = "nose"        
        
)

print find_packages()