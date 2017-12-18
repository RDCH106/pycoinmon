from setuptools import setup
from pycoinmon.metadata import Metadata

metadata = Metadata()


def requirements():
    """Build the requirements list for this project"""
    requirements_list = []

    with open('requirements.txt') as requirements:
        for install in requirements:
            requirements_list.append(install.strip())

    return requirements_list


setup(
    name = 'pycoinmon',
    packages = ['pycoinmon'],
    install_requires = requirements(),
    version = metadata.get_version(),
    license = 'MIT',
    description = 'Python Port Based on COINMON',
    url = 'https://github.com/RDCH106/pycoinmon',
    entry_points={
        'console_scripts': ['pycoinmon=pycoinmon:main'],
    },
    keywords = ['bitcoin', 'criptocurrency', 'crypto', 'ticker', 'python', 'cli', 'price-tracker', 'command-line'],
    classifiers = ['Programming Language :: Python',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3.2',
                   'Programming Language :: Python :: 3.3',
                   'Programming Language :: Python :: 3.4',
                   'Programming Language :: Python :: 3.5',
                   'Programming Language :: Python :: 3.6'],
)