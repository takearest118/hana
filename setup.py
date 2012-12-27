from distutils.core import setup

import re

def find_version(filename):
	for line in open(filename).readlines():
		m = re.search("__version__\s*=\s*\"([^\"]+)\"", line)
		if m:
			return m.group(1)
	return None

VERSION = find_version('src/hana.py')

setup(
	name='hana',
	version=VERSION,
	description='Hangeul morphological analyzer.',
	long_description='Hangeul morphological analyzer.',
	url='https://github.com/takearest118/hana',
	author='Kevin Cho',
	author_email='takearest118@gmail.com',
	license='Free',
	platforms=['Mac OSX', 'Linux'],
	packages=['hana'],
	package_dir={'hana': 'src'},
	package_data={'hana': ['test/*.txt', 'dic/*.dic', 'unittest/*.py']},
)
