import sys
from setuptools import setup

long_description = ''
if 'upload' in sys.argv or 'register' in sys.argv:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')

setup(
    name='django-bootstrap-daterangepicker',
    version='1.0.2',

    description='A Django form field and widget wrapper for bootstrap-daterangepicker',
    long_description=long_description,

    url='https://github.com/jckw/django-bootstrap-daterangepicker/',

    author='Yuri Malinov, Jack Weatherilt',
    author_email='yurik.m@gmail.com, jackweatherilt@outlook.com',

    license='MIT',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
        'Environment :: Web Environment',
        'Framework :: Django',
    ],

    keywords='django daterange datetime date bootstrap picker',
    packages=['bootstrap_daterangepicker'],
    install_requires=[
        'django',
        'python-dateutil'
    ],
    include_package_data=True,
)
