from setuptools import setup

setup(name='utf9',
      version='0.2',
      description='Encode and decode text with UTF-9 (IEEE RFC4042)',
      install_requires=['bitarray'],
      url='http://github.com/enricobacis/utf9',
      author='Enrico Bacis',
      author_email='enrico.bacis@gmail.com',
      license='MIT',
      packages=['utf9'],
      keywords='utf9 encode decode rfc4042')
