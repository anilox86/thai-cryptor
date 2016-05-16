# Thai Cryptor
Thai Cryptor - English-Thai character replacer based on keyboard layout written in Python 3

### Features
- decrypt: replace thai character from english strings
- encrypt: replace english character from thai strings

### Requirements
- Python3

### Usage
- add text you want to decrypt to in.txt
- run this script (depend on your system, see below)
- check your output in out.txt

**Windows**
- decrypt: right-click on decrypt.ps1 and click 'Run with PowerShell'
- encrypt: right-click on encrypt.ps1 and click 'Run with PowerShell'
- if python.exe is not in C:\\Python34 you need to edit to correct path yourself

**Linux**
- `./thai-cryptor.py <command> [<file>] ...`
- 2 commands: `decrypt` or `encrypt`
- you can also specify file(s) yourself like `./thai-cryptor.py decrypt mytext1.txt`

### Todo
- test on Windows
