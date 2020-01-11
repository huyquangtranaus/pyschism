#!/usr/bin/env python
import pathlib
import setuptools
parent = pathlib.Path(__file__).parent.absolute()
conf = setuptools.config.read_configuration(parent / 'setup.cfg')
meta = conf['metadata']
setuptools.setup(
    name=meta['name'],
    version=meta['version'],
    author=meta['author'],
    author_email=meta['author_email'],
    description=meta['description'],
    long_description=meta['long_description'],
    long_description_content_type="text/markdown",
    url=meta['url'],
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    setup_requires=['wheel', 'numpy'],
    install_requires=[
        'matplotlib',
        'netCDF4',
        'pyproj',
        'shapely',
        'fiona',
        'f90nml',
        'ordered_set',
        'psutil',
        'paramiko'
    ],
    entry_points={
        'console_scripts': [
            'tidal_run = pyschism.cmd.tidal_run:main',
        ]
    }
)
