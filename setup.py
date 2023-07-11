import os

from setuptools import find_packages
from setuptools import setup


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()


long_description = (
    read('README.rst')
    + '\n' +
    read('CHANGES.rst')
)


tests_require = [
    'grokcore.content',
    'grokcore.view [test]',
    'zope.app.appsetup',
    'zope.app.wsgi',
    'zope.login',
    'zope.principalregistry',
    'zope.securitypolicy',
    'zope.testbrowser',
    'zope.testing',
]


setup(
    name='grokcore.traverser',
    version='4.0',
    author='Grok Team',
    author_email='zope-dev@zope.dev',
    url='https://github.com/zopefoundation/grokcore.traverser',
    description='Traverser for the Grok Framework',
    long_description=long_description,
    license='ZPL',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Zope Public License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Framework :: Zope :: 3',
    ],
    packages=find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['grokcore'],
    include_package_data=True,
    zip_safe=False,
    python_requires='>=3.7',
    install_requires=[
        'grokcore.component >= 2.5',
        'grokcore.security',
        'grokcore.view',
        'martian',
        'setuptools',
        'zope.component',
        'zope.interface',
        'zope.publisher',
    ],
    tests_require=tests_require,
    extras_require={'test': tests_require},
)
