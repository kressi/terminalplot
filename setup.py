from setuptools import setup

setup(
	name='terminalplot',
	version='0.2.0',
	description='Plot points in terminal',
	url='http://github.com/kressi/terminalplot',
	author='Michael Kressibucher',
	author_email='michael.kressibucher@gmail.com',
	license='AGPL',
	packages=['terminalplot'],
	zip_safe=True,
	entry_points={
		'console_scripts': ['plot = terminalplot.command:main']
	}
)
