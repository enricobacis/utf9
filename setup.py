from setuptools import setup

with open('README.rst') as README:
    long_description = README.read()
    long_description = long_description[long_description.index('Description'):]

setup(name='utf9',
      version='0.3.1',
      description='Encode and decode text using UTF-9.',
      long_description=long_description,
      install_requires=['bitarray'],
      url='http://github.com/enricobacis/utf9',
      author='Enrico Bacis',
      author_email='enrico.bacis@gmail.com',
      license='MIT',
      packages=['utf9'],
      keywords='utf9 encode decode rfc4042')
