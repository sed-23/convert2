from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    README = readme_file.read()

with open('HISTORY.rst') as history_file:
    HISTORY = history_file.read()

setup_args = dict(
    name='convert2',
    version='0.0.1',
    description='Useful tools to convert various units in Python',
    long_description_content_type="text/markdown",
    long_description=README + '\n\n' + HISTORY,
    license='MIT',
    packages=find_packages(),
    author='Sukumar Reddy',
    author_email='sukumarreddy.v5@gmail.com',
    keywords=['Converter', 'Convertit', 'CurrencyConverter', 'FileConverter'],
    url='https://github.com/sed-23/convert2',
    download_url='https://pypi.org/project/convert2/'
)

install_requires = [
    'json'
]

if __name__ == '__main__':
    setup(**setup_args, install_requires=install_requires)
