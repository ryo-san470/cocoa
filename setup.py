from setuptools import setup


def _read_readme():
    with open('./README.md', 'r') as f:
        return f.read()


def _load_requires_from_file(filepath):
    return [pkg_name.rstrip('\r\n') for pkg_name in open(filepath).readlines()]


def _install_requires():
    return _load_requires_from_file('requirements.txt')


setup(
    name='cocoa',
    version='0.0.1',
    description='Cocoa is the CTF toolkit',
    long_description=_read_readme(),
    url='https://github.com/ryosan-470/cocoa',
    author='Ryosuke SATO',
    author_email='rskjtwp@gmail.com',
    install_requires=_install_requires(),
    tests_require=['pytest'],
    setup_requires=['pytest-runner'],
    license='MIT',
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: MIT License",
        "Topic :: Utilities",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3 :: Only",
    ],
)
