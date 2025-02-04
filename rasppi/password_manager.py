import sys
import csv

import pyperclip
from lib.Argument import Argument
from utils.Add import addEntry
from utils.Remove import removeEntry
from utils.Retrieve import retrieveEntries
from utils.Verifymp import verifyMasterPassword
from utils.GeneratePassword import generate_password
from utils.Config import config
from getpass import getpass

from rich import print as printc

masterPassword = getpass()
parser = Argument()
args = sys.argv

parser.parse_args(args)

if parser.option == ['--help']:
    parser.print_help()
    sys.exit(0)

if parser.option == ['--config']:
  config()
  sys.exit(0)

if '--operation' in parser.option:
    try:
        operation = parser.optionValues['--operation']
    except KeyError:
        print("Missing --operation argument, use --help for help")
        sys.exit(0)
else:
    print("Missing --operation argument, use --help for help")
    sys.exit(0)

if operation=="store":
    if '--operation' not in parser.option or '--service' not in parser.option or '--password' not in parser.option or '--user' not in parser.option or '--notes' not in parser.option:
        print("Usage: python3 password_manager.py --operation store --service <service> --user <user> --password <password> --notes <notes>")
        sys.exit(0)
    #masterPassword = parser.optionValues['--master-password']
    service = parser.optionValues['--service']
    user = parser.optionValues['--user']
    password = parser.optionValues['--password']
    notes = parser.optionValues['--notes']
    if (verifyMasterPassword(masterPassword)==True):
        addEntry(masterPassword, service, password, user, notes)
        sys.exit(0)
    else:
        printc("[red][-] Master password is incorrect, try again![/red]")

if operation=="storeFile":
    if '--operation' not in parser.option or '--csvFile' not in parser.option:
        print("Usage: python3 password_manager.py --operation storeFile --csvFile <filePath .csv>")
        sys.exit(0)
    #masterPassword = parser.optionValues['--master-password']
    csvPath = parser.optionValues['--csvFile']
    if (verifyMasterPassword(masterPassword)==True):
        with open(csvPath, mode ='r')as file:
            csvFile = csv.reader(file)
            for lines in csvFile:
                printc(lines)
                addEntry(masterPassword, lines[0], lines[2],lines[1],lines[3])
        sys.exit(0)
    else:
        printc("[red][-] Master password is incorrect, try again![/red]")

if operation=="delete":
    if '--operation' not in parser.option or '--service' not in parser.option:
        print("Usage: python3 password_manager.py --operation delete --service <service>")
        sys.exit(0)
    #masterPassword = parser.optionValues['--master-password']
    service = parser.optionValues['--service']
    if (verifyMasterPassword(masterPassword)==True):
        removeEntry(masterPassword, service)
        sys.exit(0)
    else:
        printc("[red][-] Master password is incorrect, try again![/red]")

if operation=="retrieve":
    if '--operation' not in parser.option or '--search' not in parser.option:
        print("Usage: python3 password_manager.py --operation retrieve --search <search> --expCsv <path>")
        sys.exit(0)
    #masterPassword = parser.optionValues['--master-password']
    search = parser.optionValues['--search']
    if (verifyMasterPassword(masterPassword)):
        if '--expCsv' not in parser.option:
            retrieveEntries(masterPassword, search=search, expPath= None)
        else:
            retrieveEntries(masterPassword, search=search, expPath= parser.optionValues['--expCsv'])
        sys.exit(0)
    else:
        printc("[red][-] Master password is incorrect, try again![/red]")

if operation=="generate":
    if '--length' in parser.option:
        try:
            try:
                if parser.optionValues['--length'].isdigit:
                    length = parser.optionValues['--length']
                    gpasswd = generate_password(int(length))
                    pyperclip.copy(gpasswd)
                    print('----------------------------------')
                    printc("[green][+][/green] This is your generated password: " + gpasswd)
                    printc("[green][+][/green] Password copied to clipboard")
                    print('----------------------------------')
                    sys.exit(0)
            except ValueError:
                printc("[red][-] Length must be an integer [/red]")
        except KeyError:
            printc("[red][-] Length value is missing [/red]")
    else:
        print("Usage: python3 password_manager.py --operation generate --length <length>")


