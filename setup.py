try:
   from setuptools import setup
except ImportError:
   from distutils.core import setup

config = {
   'description' : 'pyURHD',
   'author' : 'Andrea Pavan',
   'url' : 'https://github.com/pandvan/pyURHD',
   'download_url' : 'https://github.com/pandvan/pyURHD/archive/master.zip',
   'author_email' : 'prog.pawz at gmail dot com',
   'version' : '0.1',
   'install_requires' : ['nose'],
   'packages' : 'NAME',
   'scripts' : [],
   'name' : 'pyURHD',
}

setup(**config)

