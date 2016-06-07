from setuptools import setup, find_packages

setup(
  name = 'pipspect',
  version = '0.3',
  entry_points={
    'console_scripts': ['pipspect=src.pipspect:main']
  },
  packages = find_packages(),
  license = "MIT",
  description = 'A small CLI tool to inspect your modules, especially those installed via pip',
  author = 'Yong Cheng Toh',
  author_email = 'tohyongcheng@gmail.com',
  url = 'https://github.com/tohyongcheng/pipspect', 
  keywords = ['module', 'inspect', 'pip', 'classes', 'builtin', 'functions', 'methods'], # arbitrary keywords
  classifiers = [
    'Development Status :: 3 - Alpha',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python',
    'Topic :: Software Development :: Testing',
    'Programming Language :: Python :: 2',
  ],
)