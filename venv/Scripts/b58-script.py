#!C:\Users\githe\PycharmProjects\NP_Fall2019_FinalProject_Blockchain\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'pycoin==0.90.20190728','console_scripts','b58'
__requires__ = 'pycoin==0.90.20190728'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('pycoin==0.90.20190728', 'console_scripts', 'b58')()
    )
