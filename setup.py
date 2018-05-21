from setuptools import setup

test_requirements = ['pyflakes>=0.6.1']

setup(
    name = "PySPED",
    version = "1.1.0",
    author = "Aristides Caldeira",
    author_email = 'aristides.caldeira@tauga.com.br',
    test_suite='tests',
    keywords = ['nfe', 'nfse', 'cte', 'sped', 'edf', 'ecd'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
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

        'pysped.cte',
        'pysped.cte.leiaute',

        'pysped.mdfe',
        'pysped.mdfe.leiaute',

        'pysped.nfse',
        'pysped.nfse/sp-sao_paulo',

        'pysped.esocial',
        'pysped.esocial.leiaute',

        'pysped.xml_sped',
        'pysped.relato_sped',
    ],
    package_data = {
        '': ['*.txt', '*.odt', '*.xsd', '*.ttf', '*.png', '*.jpg'],
        'pysped.xml_sped': ['cadeia-certificadora/*/*'],
        'pysped.relato_sped': ['fonts/*']
    },
    url = 'https://github.com/aricaldeira/PySPED',
    license = 'LGPL-v2.1+',
    description = 'PySPED is a library to implement all requirements of the Brazilian Public System of Digital Bookkeeping',
    long_description = open('README.rst').read(),
    requires=[
        'lxml(>=3.7.3)',
        'xmlsec(>=1.0.7)',
        'Geraldo(>=0.4.16)',
        'qrcode(>=5.3)',
        'py3o.template(>=0.9.11)',
        'sh(>=1.12.9)'
    ],
    tests_require=test_requirements,
)
