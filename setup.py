import os
from setuptools import setup, find_packages
from git_auto_export import __version__

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='edx-git-auto-export',
    version=__version__,
    packages=find_packages(),
    include_package_data=True,
    license='GNU AFFERO GENERAL PUBLIC LICENSE',
    description='A task that auto save course OLX to git when author publish it',
    url='https://github.com/mitodl/edx-git-auto-export.git',
    install_requires=[
        'edx-opaque-keys',
        'celery',
    ],
)
