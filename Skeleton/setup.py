try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


config = {
    'description': 'ex47',
    'author': 'Anayat Chowdhury',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'Anayatc@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)