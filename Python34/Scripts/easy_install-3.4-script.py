#!python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'setuptools==14.3.1','console_scripts','easy_install-3.4'
__requires__ = 'setuptools==14.3.1'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('setuptools==14.3.1', 'console_scripts', 'easy_install-3.4')()
    )
