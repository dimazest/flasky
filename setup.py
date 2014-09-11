from setuptools import setup, find_packages


with open('README.rst') as f:
    long_description = f.read()


setup(
    name='flasky_theme',
    version=0.1,
    url='https://github.com/dimazest/flasky_theme',
    author='F. Javier Alba',
    maintainer="Dmitrijs Milajevs",
    maintainer_email="dimazest@gmail.com",
    description='A modified flasky theme by F. Javier Alba',
    long_description=long_description,
    # license='MIT',
    packages=find_packages(),
    package_data={'': [
        # 'LICENSE',
        'README.rst',
        'static/*',
        'templates/*',
    ]
    },
    # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Topic :: Internet :: WWW/HTTP',
    ],
    zip_safe=False,
    install_requires=[
        'pelican',
    ],
)
