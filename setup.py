from distutils.core import setup

setup(
    name = "PySPED",
    version = "0.9.0",
    author = "Aristides Caldeira",
    author_email = 'aristides.caldeira@tauga.com.br',
    test_suite = 'tests',
    keywords = ['nfe', 'nfse', 'cte', 'sped', 'edf', 'ecd'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    packages = [
        'pysped', 'pysped.cte', 'pysped.efd', 'pysped.nfe',
        'pysped.nfe.leiaute', 'pysped.nfe.danfe', 'pysped.nfe.manual_300',
        'pysped.nfe.manual_401', 'pysped.nfse', 'pysped.xml_sped',
        'pysped.ecd', 'pysped.exemplos', 'pysped.nf_paulista',
        'pysped.relato_sped',
    ],
    package_data = {
        'pysped.nfe.danfe': ['fonts/*'],
        'pysped.nfe.leiaute': ['schema/*/*'],
        'pysped.relato_sped': ['fonts/*'],
    },
    url = 'https://github.com/aricaldeira/PySPED',
    license = 'AGPL-v3',
    description = 'PySPED is a library to implement all requirements of the public system of bookkeeping digital',
    long_description = open('README.rst').read(),
    install_requires=[
        'Geraldo >= 0.4.16',
        'PyXMLSec >= 0.3.0'
    ],
)
