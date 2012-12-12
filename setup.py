from distutils.core import setup

setup(
	name='hana',
	version='0.5',
	description='Hangeul morphological analyzer.',
	long_description='Hangeul morphological analyzer.',
	url='https://github.com/takearest118/hana',
	author='Kevin Cho',
	author_email='takearest118@gmail.com',
	license='Free',
	platforms=['Mac OSX', 'Linux'],
	packages=['hana'],
	package_dir={'hana': 'src'},
	package_data={'hana': ['test/*.txt', 'dic/*.dic']},
)
