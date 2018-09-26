from setuptools import setup

setup(
    name='datasci',
    version='0.0.1',
    author='Christopher Brown',
    author_email='io@henrian.com',
    url='https://github.com/chbrown/datasci-python',
    license='MIT',
    packages=['datasci'],
    install_requires=open('requirements.txt').readlines(),
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
        'Topic :: Sociology',
        'Topic :: Text Processing',
    ],
)
