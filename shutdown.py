def convert(rule,number):

    number = int(number)

    if rule == 'h':
        number=number*3600
    elif rule == 'm':
        number=number*60
    
    import subprocess
    subprocess.run(f'shutdown /a')
    subprocess.run(f'shutdown /s /t {number}'.split(' '))
    
        

import sys
convert(sys.argv[1],sys.argv[2])

