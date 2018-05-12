from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

exec(open('dmstudio/version.py').read())

version = __version__


setup(name='dmstudio',
      version=version,
      description='Python module for Datamine Studio scripting',
      url='http//github.com/...',
      author='Sean Horan',
      author_email='sean.horan@rpacan.com',
      license='GNU',
      packages=['dmstudio'],
      include_package_data=True,
      package_data={'':['LICENCES.txt']},
      # install_requires=['win32com', 'pandas', 'os', 'numpy'],
      zip_safe=False)
