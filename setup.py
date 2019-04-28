import os
from setuptools import setup

setup(
  name='nearcdemo',
  version=os.environ.get('version_number'),
  description='Conda and Python demonstration for a workshop at Northeast Arc User Group (NEARC), spring 2019.',
  packages=[
    'nearcdemo'
  ],
  package_dir={'': 'src'}
)