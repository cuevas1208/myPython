# !python3
""" This program takes the copy text and edit it's content 
to add a start-prefixed test"""

import time
import pyperclip

text = pyperclip.paste()
lines = text.split('\n')

for i in range(len(lines)): 
    lines[i] = '* '+ lines[i]

text = '\n'.join(lines)
pyperclip.copy(text)        

time.sleep(7)
