from setuptools import setup, find_packages
import sys

import test

py2 = sys.version_info[0] == 2
py3 = sys.version_info[0] == 3

#if py2:
#    requirements = ['enum34', 'wrapt', 'future']
#elif py3:
#    requirements = ['wrapt', 'future']


setup(
    
    name ='test',
        
    version = test.__version__,
    
    description = 'test',
	
    long_description = 'test',

    url = 'https://github.com/0-jun/py-test',
	download_url     = 'https://github.com/0-jun/py-test',
        
    author = 'Healthrian',
    
    license = 'Healthrian',
    install_requires = [ ],    
    classifiers = [

        'Development Status :: 0 - Alpha',

        'Intended Audience :: Developers',
        
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',

        'Topic :: System :: Algorithm',
		
        'License :: Other/Proprietary License',

        'Programming Language :: Python :: 3.4',
    ],
    
    keywords = 'band calculate algorithm',
	
    zip_safe=False,

    )
