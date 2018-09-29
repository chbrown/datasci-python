from setuptools import setup

setup(
    name='datasci',
    version='0.0.2',
    author='Christopher Brown',
    author_email='io@henrian.com',
    description='Data science utilities',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/chbrown/datasci-python',
    license='MIT',
    packages=['datasci'],
    python_requires='>=3.6',
    install_requires=[
        'altair>=2.2',
        'cytoolz>=0.8',
        'ipython>=6.5',
        'markdown>=2.6',
        'numpy>=1.15',
        'pandas>=0.23',
        'scipy>=1.1',
        'statsmodels>=0.9',
    ],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
        'pytest-cov',
    ],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering',
    ],
)
