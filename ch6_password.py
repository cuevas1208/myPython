#! python3
#Password.py stores a password and return a password to the clip board on demand
import sys
import time
import pyperclip

if len(sys.argv) < 2:
    print ('Usage: python pw.py [account] - copy account password')
    time.sleep(7)
    sys.exit()


password = {'blog':'12345',
            'gmail':'235456',
            'web':'wersdf'}

account = sys.argv[1] # first command line arg is the account name

if account in password:
    pyperclip.copy(password[account])
    print('password has been copy to the clipboard')
else:
    print('no password set for' + account)
    
print (account)
time.sleep(7)

