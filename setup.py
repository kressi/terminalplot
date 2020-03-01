import setuptools
import os

here = os.path.abspath(os.path.dirname(__file__))

version_path = os.path.join(here, 'terminalplot', 'version.py')
with open(version_path, encoding='utf-8') as f:
    exec(f.read())

readme_path = os.path.join(here, 'README.rst')
with open(readme_path, encoding='utf-8') as f:
    readme = f.read()


def version():
    if os.getenv('TRAVIS_BUILD_STAGE_NAME', '') == 'Deploy test':
        return __version__ + '.' + os.getenv('TRAVIS_BUILD_NUMBER', '')
    else:
        return __version__

setuptools.setup(
    name='terminalplot',
    version=version(),
    description='Plot points in terminal',
    long_description=readme,
    url='https://github.com/kressi/terminalplot',
    download_url='https://github.com/kressi/terminalplot/tarball/v' + __version__,
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
    }
)
