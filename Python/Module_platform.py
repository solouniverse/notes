#Srimatrenamaha
'''
NAME
    platform

DESCRIPTION
    This module tries to retrieve as much platform-identifying data as
    possible. It makes this information available via function APIs.

    If called from the command line, it prints the platform
    information concatenated as single string to stdout. The output
    format is useable as part of a filename.
'''

'''
	architecture(executable='C:\\Users\\v-srm\\AppData\\Local\\Continuum\\Anaconda3\\python.exe', bits='', linkage='')
        Queries the given executable (defaults to the Python interpreter
        binary) for various architecture information.

        Returns a tuple (bits, linkage) which contains information about
        the bit architecture and the linkage format used for the
        executable. Both values are returned as strings.
'''
In [24]: platform.architecture()
Out[24]: ('64bit', 'WindowsPE')

'''
	dist(distname='', version='', id='', supported_dists=('SuSE', 'debian', 'fedora', 'redhat', 'centos', 'mandrake', 'mandriva', 'rocks', 'slackware', 'yellowdog', 'gentoo', 'UnitedLinux', 'turbolinux', 'arch', 'mageia'))
        Tries to determine the name of the Linux OS distribution name.
'''
In [25]: platform.dist()
Out[25]: ('', '', '')

'''
	linux_distribution(distname='', version='', id='', supported_dists=('SuSE', 'debian', 'fedora', 'redhat', 'centos', 'mandrake', 'mandriva', 'rocks', 'slackware', 'yellowdog', 'gentoo', 'UnitedLinux', 'turbolinux', 'arch', 'mageia'), full_distribution_name=1)
'''
In [29]: platform.linux_distribution()
Out[29]: ('', '', '') #On a windows PC
'''
	machine()
        Returns the machine type, e.g. 'i386'
'''
In [26]: platform.machine()
Out[26]: 'AMD64'

'''
    node()
        Returns the computer's network name (which may not be fully
        qualified)        
'''
In [27]: platform.node()
Out[27]: 'MININT-ALIBJKF'

'''
    platform(aliased=0, terse=0)
        Returns a single string identifying the underlying platform
        with as much useful information as possible (but no more :).

'''
In [28]: platform.platform()
Out[28]: 'Windows-10-10.0.15063-SP0'

'''
    processor()
        Returns the (true) processor name, e.g. 'amdk6'
'''
In [30]: platform.processor()
Out[30]: 'Intel64 Family 6 Model 45 Stepping 7, GenuineIntel'

'''
    python_build()
        Returns a tuple (buildno, builddate) stating the Python
        build number and date as strings.
'''
In [43]: platform.python_build()
Out[43]: ('default', 'May 11 2017 13:25:24')

'''
    python_compiler()
        Returns a string identifying the compiler used for compiling
        Python.
'''
In [33]: platform.python_compiler()
Out[33]: 'MSC v.1900 64 bit (AMD64)'

'''
    python_implementation()
        Returns a string identifying the Python implementation.
'''
In [34]: platform.python_implementation()
Out[34]: 'CPython'
	
'''
    python_version()
        Returns the Python version as string 'major.minor.patchlevel'

        Note that unlike the Python sys.version, the returned value
        will always include the patchlevel (it defaults to 0).

    python_version_tuple()
        Returns the Python version as tuple (major, minor, patchlevel)
        of strings.

        Note that unlike the Python sys.version, the returned value
        will always include the patchlevel (it defaults to 0).
'''
In [36]: platform.python_version()
Out[36]: '3.6.1'

In [37]: platform.python_version_tuple()
Out[37]: ('3', '6', '1')

'''
    release()
        Returns the system's release, e.g. '2.2.0' or 'NT'
'''
In [38]: platform.release()
Out[38]: '10'  #On Windows 10

'''
    system()
        Returns the system/OS name, e.g. 'Linux', 'Windows' or 'Java'.
'''
In [39]: platform.system()
Out[39]: 'Windows'
	
'''
    uname()
        Fairly portable uname interface. Returns a tuple
        of strings (system, node, release, version, machine, processor)
        identifying the underlying platform.
'''
In [41]: platform.uname() # on Windows 10
Out[41]: uname_result(system='Windows', node='MININT-ALIBJKF', release='10', version='10.0.15063', machine='AMD64', processor='Intel64 Family 6 Model 45 Stepping 7, GenuineIntel')

'''
    version()
        Returns the system's release version, e.g. '#3 on degas'
'''
In [42]: platform.version()
Out[42]: '10.0.15063'
