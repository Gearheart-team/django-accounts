from setuptools import setup, find_packages

setup(
    name='izeni-django-accounts',
    version='1.1.2a',
    namespace_packages=['izeni', 'izeni.django'],
    packages=find_packages(),
    include_package_data=True,
    author='Izeni, Inc.',
    author_email='django-accounts@izeni.com',
    description=open('README.md').read(),
    url='https://dev.izeni.net/izeni/django-accounts',
    install_requires=[
        'Django==1.11.7',
        'djangorestframework>3.4',
        #'python-social-auth==0.2.13',
        'social-auth-app-django',
        'requests==2.8.1',
    ],
    dependency_links=[
        'https://github.com/izeni-team/python-social-auth.git@v0.2.21-google-fix#egg=python-social-auth-0',
    ]
)
