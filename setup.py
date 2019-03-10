import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

os.chdir(
    os.path.normpath(
        os.path.join(
            os.path.abspath(__file__),
            os.pardir)))

# TODO: grab version from docs/conf.py or both from some common place
# maybe do the paparazzi git tag dirty trick in the version name

setup(
    name='bd-teamsport',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    license='GPL3',  # example license
    description='Business Development is a team sport',
    long_description=README,
    url='https://github.com/monkeypants/bd-teamsport/',
    author='Chris Gough',
    author_email='christopher.d.gough@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.1',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GPL3',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
