from setuptools import setup
import os

__version__ = "0.1"
__author__ = "Atsushi Odagiri"
__email__ = 'aodagx@gmail.com'

requires = [
    "pyramid",
]

tests_require = [
    "pytest",
    "pytest-cov",
    "testfixtures",
]


def read(name):
    with open(os.path.join(os.path.dirname(__file__), name)) as f:
        return f.read()


setup(
    name="rebecca.odata",
    packages=["rebecca.odata"],
    namespace_packages=["rebecca"],
    version=__version__,
    author=__author__,
    author_email=__email__,
    description="an implementation for odata: http://www.odata.org",
    long_description=read('README.rst'),
    url='https://github.com/rebeccaframework/rebecca.odata',
    license='MIT',
    install_requires=requires,
    tests_require=tests_require,
)
