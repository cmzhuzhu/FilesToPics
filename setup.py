from setuptools import setup

setup(
    name='FileToPics',
    version='0.0.1',

    description='This Python package can turn file(ppt/pptx/doc/pdf..) into pictures',
    long_description=open('README.md').read(),
    url='https://github.com/cmzhuzhu/FilesToPics',
    author='Ren Peng',
    author_email='cmzhuzhu123@gmail@gmail.com',
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