from setuptools import setup

version = '0.0.01'


namespace_packages = ['lib']

packages = ['lib.parser',
            'lib.debruijn']


scripts = ['bin/build-test-genome',
           'bin/simulate-sequencing-process',
           'bin/dbalign']


install_requires = ['networkx']


setup(name='glamp',
      version=version,
      namespace_packages=namespace_packages,
      packages=packages,
      scripts=scripts,
      license='open',
      author='Aaron Scott',
      author_email='aa5278sc-s@student.lu.se',
      install_requires=install_requires)
