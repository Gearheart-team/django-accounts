from setuptools import setup, find_packages

setup(
    name='izeni-django-accounts',
    version='1.0-dev',
    namespace_packages=['izeni.django'],
    packages=find_packages(),
    author='Izeni, Inc.',
    author_email='django-accounts@izeni.com',
    description=open('README.md').read(),
    url='https://dev.izeni.net/izeni/django-accounts',
    install_requires=[
        'Django<1.10,>=1.9',
        'djangorestframework<3.4',
        'python-social-auth==0.2.13',
        'requests==2.8.1',
        'izeni-django-common',
    ],
    dependency_links=[
        'https://dev.izeni.net/izeni/django-common/repository/archive.zip?ref=1.0-dev#egg=izeni_django_common-1.0_dev',
    ]
)