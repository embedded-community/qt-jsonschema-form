"""A setuptools based setup module.
See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='qt-jsonschema-form',
    use_scm_version=True,
    setup_requires=["setuptools_scm"],
    description='A tool to generate Qt forms from JSON Schemas',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/jupe/qt-jsonschema-form',
    author='Jussi Vatjus-Anttila',
    author_email='jussiva@gmail.com',

    # Classifiers help users find your project by categorizing it.
    # For a list of valid classifiers, see https://pypi.org/classifiers/
    classifiers=[  # Optional
        'Development Status :: 1 - Planning',
        "Intended Audience :: Developers",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS :: MacOS X",
        "Environment :: X11 Applications :: Qt",
        "Topic :: Software Development :: Widget Sets",
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.7',
        "Programming Language :: Python :: 3 :: Only",
    ],
    packages=find_packages(exclude=['tests']),
    keywords="pyside6 json-schema schema form",
    python_requires='>=3.7, <4',
    install_requires=[
        'pyside6==6.3.1',
        "jsonschema==3.2.0"
    ],
    extras_require={
        'dev': ['nose', 'coveralls', 'pylint', 'coverage', 'mock'],
        'optional': ['pytest-metadata']
    },

    project_urls={  # Optional
        'Bug Reports': 'https://github.com/jupe/qt-jsonschema-form',
        'Source': 'https://github.com/jupe/qt-jsonschema-form/',
    }
)
