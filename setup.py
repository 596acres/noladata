from setuptools import setup, find_packages
import os

import noladata


CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development',
]

setup(
    author='Eric Brelsford',
    author_email='eric@596acres.org',
    name='noladata',
    version=noladata.__version__,
    description=("Scripts and notes for working with data in the City of New "
                 "Orleans, mostly for 596 Acres' Living Lots NOLA, but "
                 "potentially useful for others, too."),
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
    url='https://github.com/596acres/noladata/',
    license='GNU Affero General Public License v3 or later (AGPLv3+)',
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    install_requires=[
        'Django>=1.5.1',
    ],
    packages=find_packages(),
    include_package_data=True,
)
