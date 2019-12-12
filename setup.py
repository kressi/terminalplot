import setuptools
import os
import sys

here = os.path.abspath(os.path.dirname(__file__))
version_path = os.path.join(here, 'terminalplot', 'version.py')
readme_path = os.path.join(here, 'README.rst')

with open(version_path, encoding='utf-8') as f:
    exec(f.read())

with open(readme_path, encoding='utf-8') as f:
    readme = f.read()

setuptools.setup(
    name='terminalplot',
    version=__version__ + '.dev' + os.getenv('TRAVIS_BUILD_NUMBER', ''),
    description='Plot points in terminal',
    long_description=readme,
    url='https://github.com/kressi/terminalplot',
    download_url='https://github.com/kressi/terminalplot/tarball/v'+__version__,
    author='Michael Kressibucher',
    author_email='michael.kressibucher@gmail.com',
    license='GPL',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Environment :: Console',
        'Operating System :: POSIX',
        'Topic :: Scientific/Engineering :: Visualization'
    ],
    keywords=['plot', 'terminal', 'graph', 'console'],
    packages=['terminalplot'],
    zip_safe=True,
    entry_points={
        'console_scripts': ['plot = terminalplot.command:main']
    },
    test_suite='nose.collector',
    tests_require=['nose']
)
