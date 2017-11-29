from distutils.core import setup, Extension

dht11_module = Extension('dht11',
                    define_macros = [('MAJOR_VERSION', '1'),
                    ('MINOR_VERSION', '0')],
                    include_dirs = ['/usr/include/python2.7'],
                    libraries = ['wiringPi', 'python2.7'],
                    library_dirs = ['/usr/local/lib'],
                    sources = ['dht11py.c'])

setup (name = 'dht11reader',
       version = '1.0',
       description = 'reads dht11 data',
       ext_modules = [dht11_module])
