from setuptools import setup

from os import path
from codecs import open

here = path.abspath( path.dirname( __file__ ) )

with open( path.join( here, 'README.md' ), encoding='utf-8' ) as file :
    long_description = file.read()

for line in open( path.join( 'meteostat', '__init__.py' ) ) :
    if line.startswith( '__version__' ) :
        exec( line )
        break

setup(
    name = 'meteostat2',
    versio = __version__,
    description = 'Meteostat alternative API for python',
    long_description = long_description,
    url = 'https://dev.meteostat.net/',
    license = 'MIT',
    Classifiers = [
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: MIT License',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10'
    ],
    keywords = 'meteo meteostat meteostat2 weather weatherAPI meteorology',
    install_requires = [ 'requests' ],
    entry_points = {
        'console_scripts' : [
            'meteostat2 = meteostat.__main__:main',
            'meteo2 = meteostat.__main__:main'
        ]
    },
    py_modules = [ 'meteostat.meteostat2' , 'meteostat.__main__' ],
    test_require = [
        'pytest'
    ]
)