import os
from setuptools import setup

setup(
  name='keenepyt',
  version=os.environ.get('version_number'),
  description='Conda and Python demonstration for a workshop at Northeast Arc User Group (NEARC), spring 2019.',
  packages=[
    'keenepyt',
    'keenepyt.core',
    'keenepyt.tools'
  ],
  package_dir={'': 'src'}
)