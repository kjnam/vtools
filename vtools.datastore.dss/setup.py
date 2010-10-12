
"""vtools setup file"""

import ez_setup
ez_setup.use_setuptools()
from setuptools import setup,find_packages

# Metadata
PACKAGE_NAME = "vtools.datastore.dss"
PACKAGE_VERSION = "0.1.6"
PACKAGES = ['vtools','vtools.datastore']

setup(
    name=PACKAGE_NAME,
    version=PACKAGE_VERSION,
    url = "http://bdo.water.ca.gov",
    description='module handling dss file',
    author="Eli Ateljevich, Qiang Shu",
    author_email="eli@water.ca.gov",
    license="PSF or ZPL",
    install_requires = ['setuptools','Traits>3.3','vtools'],
    packages = find_packages(),
    namespace_packages=['vtools','vtools.datastore'],
    package_data={
                  "vtools.datastore.dss.test":["backup_dssfile/*.dss"],
                  "vtools.datastore.dss":["examples/*.py"]
                 },
    exclude_package_data = { '': ['*.pyc','*.pyo'] },
    test_suite = "nose.collector",
    tests_require = "nose",       
    entry_points="""
            [vtools.datastore]
            DssService=vtools.datastore.dss.api:DssService
            [vtools.datastore.plugin.resource]
            DssResourceType=vtools.datastore.dss.api:DssResourceType
        """

)

print find_packages()