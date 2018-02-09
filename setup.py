tag = '0.0.1.3'
from distutils.core import setup
setup(
  name = 'RTool',
  packages = ['RTool'], # this must be the same as the name above
  version = '%d'%tag,
  description = 'A random test lib',
  author = 'Ron Nofar',
  author_email = 'ronnofar2@gmail.com',
  url = 'https://github.com/RonNofar/TextOnScreen', # use the URL to the github repo
  download_url = 'https://github.com/RonNofar/RToolPackage/archive/%d.tar.gz'%tag, # I'll explain this in a second
  keywords = ['testing', 'logging', 'example'], # arbitrary keywords
  classifiers = [],
)
