from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

exec(open('dmstudio/version.py').read())

version = __version__


setup(name=dmstudio,
      version=version,
      description='Python module for Datamine Studio scripting',
      url='http//github.com/...',
      author='Sean Horan',
      author_email='sean.horan@rpacan.com',
      license='GNU',
      packages=['commands', 'special', 'superprocess', 'files'],
      include_package_data=True,
      install_requires=['win32com', 'pandas', 'os', 'glob', 'numpy'],
      zip_safe=False)
