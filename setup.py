from setuptools import setup, find_packages

NAME = 'EmbodiedAI'
DESCRIPTION = 'A python package for implementing Multi-Agent Multi-Modal EmbodiedAI approach using Computer Vision Techniques.'
AUTHOR = 'Navneet Singh Arora'
AUTHOR_EMAIL = '0arora@informatik.uni-hamburg.de'
URL = ''
REQUIRES_PYTHON = '>=3.8.0'
VERSION = '1.0.0'
LICENSE = '(c) Copyright by Navneet Singh Arora'

with open('README.md', 'r') as readme_file:
    readme = readme_file.read()

with open('HISTORY.md', 'r') as history_file:
    history = history_file.read()

requirements = [
    "Click",
    "intake"
]

setup(
    name=NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    long_description=readme + '\n\n' + history,
    long_description_content_type='text/x-rst',
    url=URL,
    license=LICENSE,
    packages=find_packages(),
    include_package_data=True,
    python_requires=REQUIRES_PYTHON,
    install_requires=requirements,
    test_suite='tests',
    entry_points={
        'console_scripts': [
            'project = src.scripts.cli:cli',
        ],
    },
    zip_safe=False,

    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: Other/Proprietary License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Topic :: Scientific/Engineering :: Machine Learning, Data Engineering, Data Modelling, Neural Networks and AI Research',
    ],
)
