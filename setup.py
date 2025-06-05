from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='csv_to_xlsx_report',
    version='0.0.3',
    packages=find_packages(include=['csv_to_xlsx_report.*']),
    install_requires=['pandas >= 2.2.3',
                      'xlsxwriter >= 3.2.3'],
)
