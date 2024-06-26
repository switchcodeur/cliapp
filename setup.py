from setuptools import setup, find_packages, version

classifiers = [
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='cliapp',
    version='1.0',
    description='Helps you making simple cli applications.',
    long_description='This package helps you making simple command line applications.',
    url='',
    author='switchcodeur',
    author_email='switchcodeur@mail.com',
    license='MIT',
    classifiers=classifiers,
    keywords=['cli', 'python'],
    packages=find_packages(),
    install_requires=['']
)