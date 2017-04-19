from setuptools import setup
import sys, os

with open('README.rst', 'r') as f:
    long_description = f.read()

setup(
    name='FileToPics',
    version='0.0.6',

    description='This Python package can turn file(ppt/pptx/doc/docx/wps/pdf..) into pictures',
    long_description=long_description,
    url='https://github.com/cmzhuzhu/FilesToPics',
    author='Cao Mingzhu',
    author_email='cmzhuzhu123@gmail.com',
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3 :: Only',
    ],

    keywords='Python file ppt doc images',

    packages=['tests'],
    py_modules=['FileToPics'],
    test_suite='tests',
)