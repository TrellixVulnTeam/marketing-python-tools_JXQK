#!python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'Cython==0.21.2','console_scripts','cygdb'
__requires__ = 'Cython==0.21.2'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('Cython==0.21.2', 'console_scripts', 'cygdb')()
    )
