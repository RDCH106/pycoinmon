from setuptools import setup
from pycoinmon.pycoinmon import Metadata

metadata = Metadata()

setup(
    name = 'pycoinmon',
    packages = ['pycoinmon'],
    version = metadata.get_version(),
    license = 'MIT',
    description = 'Python Port Based on COINMON',
    url = 'https://github.com/RDCH106/pycoinmon',
    keywords = ['bitcoin', 'criptocurrency', 'crypto', 'ticker', 'python', 'cli', 'price-tracker', 'command-line'],
    classifiers = ['Programming Language :: Python',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3.2',
                   'Programming Language :: Python :: 3.3',
                   'Programming Language :: Python :: 3.4',
                   'Programming Language :: Python :: 3.5',
                   'Programming Language :: Python :: 3.6'],
)