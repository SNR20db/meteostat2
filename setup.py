from setuptools import setup

from os import name, path
from codecs import open

here=path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as file:
    long_description=file.read()

for line in open(path.join('','__init__.py')):
    if line.startswith('__version__'):
        exec(line)
        break

setup(
    name='meteostat',
    version=__version__,
    description='Meteo stat API for python',
    long_description=long_description,
    url='https://dev.meteostat.net/',
    license='MIT',
    Classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: MIT License',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10'
    ],
    keywords='meteo meteostat weather weatherAPI meteorology',
    install_requires=['requests'],
    entry_points={
        'console_scripts':[
            'meteostat=meteostat.__main__:main',
            'meteo=meteostat.__main__:main'
        ]
    },
    py_modules=['meteostat.meteostat2','meteostat.__main__'],
    test_require=[
        'pytest'
    ]
)