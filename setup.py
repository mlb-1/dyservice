# Copyright (c) 2013 Hewlett-Packard Development Company, L.P.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# THIS FILE IS MANAGED BY THE GLOBAL REQUIREMENTS REPO - DO NOT EDIT
import setuptools

# In python < 2.7.4, a lazy loading of package `pbr` will break
# setuptools if some other modules registered functions in `atexit`.
# solution from: http://bugs.python.org/issue15881#msg170215
try:
    import multiprocessing  # noqa
except ImportError:
    pass

setuptools.setup(
    setup_requires=['pbr>=1.8'],
    pbr=True)

'''
from setuptools import setup, find_packages
setup(
    name='monasca-api',
    version='1.1.0',
    url='http://172.21.129.39:8088/openstack/monasca-api.git',
    description='Monitor as service',
    long_description=open('README.md').read(),
    author='ruijie',
    maintainer='ruijie',
    maintainer_email='malibin@ruijie.com.cn',
    license='BSD',
    packages=find_packages(exclude=('tests', 'tests.*')),
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'console_scripts': ['monasca-api = monasca_api.api.server:launch']
    },
    classifiers=[
        'Environment :: OpenStack',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
    ],
    install_requires=[
        'tooz>=1.58.0',
        'keystoneauth1>=3.1.0',
        'falcon>=1.2.0',
        'setuptools',
        'gunicorn',
        'gevent',
        'futurist',
        'pymysql',
        'APScheduler>=3.3.1',
        'simplejson==3.11.1',
        'httplib2>=0.10.3',
        'SQLAlchemy==1.0.19',
        'futures==3.1.1',
        'python_keystoneclient>=3.1.0',
        'oslo.config!=4.3.0,!=4.4.0,>=4.0.0',
        'oslo.db>=4.24.0',
        'oslo.log>=3.22.0',
        'oslo.concurrency>=3.22.0',
        'PasteScript>=2.0.2',
        'eventlet!=0.18.3,!=0.20.1,<0.21.0,>=0.18.2'
    ],
    extras_require={},
)
'''