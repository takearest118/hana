from distutils.core import setup

setup(
	name='korean_analyzer',
	version='0.5',
	description='Korean morphological analyzer.',
	long_description='Korean morphological analyzer.',
	url='https://github.com/takearest118/korean_analyzer',
	author='Kevin Cho',
	author_email='takearest118@gmail.com',
	license='Free',
	platforms=['Mac OSX', 'Linux'],
	packages=['korean_analyzer'],
	package_dir={'korean_analyzer': 'src'},
	package_data={'korean_analyzer': ['test/*.txt', 'dic/*.dic']},
)
