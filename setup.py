from setuptools import setup

setup(
    name = "PySPED",
    version = "0.1.2",
    author = "Aristides Caldeira",
    author_email = 'aristides.caldeira@tauga.com.br',
    test_suite='tests',
    keywords = ['nfe', 'nfse', 'cte', 'sped', 'edf', 'ecd'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    packages = [
        'pysped',
        'pysped.nfe',
        'pysped.nfe.leiaute',
        'pysped.nfe.danfe',
        'pysped.nfe.manual_300',
        'pysped.nfe.manual_401',
        'pysped.cte',
        'pysped.cte.leiaute',
        'pysped.cte.dacte',
        'pysped.efd',
#        'pysped.nfse',
        'pysped.xml_sped',
        'pysped.ecd',
        'pysped.nf_paulista',
        'pysped.relato_sped',
        'pysped.exemplos',
    ],
    package_data = {
        'pysped.nfe.danfe': ['fonts/*'],
        'pysped.relato_sped': ['fonts/*'],
        'pysped.nfe.leiaute': ['schema/*/*'],
        'pysped.cte.leiaute': ['schema/*/*'],
        'pysped.xml_sped': ['cadeia-certificadora/*/*']
    },
    url = 'https://github.com/aricaldeira/PySPED',
    license = 'LGPL-v2.1+',
    description = 'PySPED is a library to implement all requirements of the public system of bookkeeping digital',
    long_description = open('README.rst').read(),
    install_requires=[
        'Geraldo >= 0.4.16',
        'PyXMLSec >= 0.3.0'
    ],
    tests_require=[
        'pyflakes>=0.6.1',
    ],
)
