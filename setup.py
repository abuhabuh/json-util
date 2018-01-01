from setuptools import setup

VERSION = '0.1'


setup(
    name='json_util',
    version=VERSION,
    description='json utilities',
    url='https://github.com/abuhabuh/json-util',
    author='John Wang',
    author_email='jue@alumni.cmu.edu',
    license='MIT',
    packages=['json_util'],
    zip_safe=False,
    install_requires=[
        'nose',
    ]
)
