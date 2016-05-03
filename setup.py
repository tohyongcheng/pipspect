from distutils.core import setup
setup(
  name = 'pipspect',
  packages = ['pipspect'], # this must be the same as the name above
  version = '0.1',
  description = 'A small CLI tool to inspect your modules, especially those installed via pip',
  author = 'Yong Cheng Toh',
  author_email = 'tohyongcheng@gmail.com',
  url = 'https://github.com/tohyongcheng/pipspect', # use the URL to the github repo
  download_url = 'https://github.com/peterldowns/pipspect/tarball/0.1', # I'll explain this in a second
  keywords = ['module', 'inspect', 'pip'], # arbitrary keywords
  classifiers = [],
)