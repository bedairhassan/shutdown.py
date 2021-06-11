import sys,subprocess

def findRule(rule):
    if rule == 'h':
        return 3600
    elif rule == 'm':
        return 60
    elif rule=='s':
        return 1

def shutdownProcess(number):
    subprocess.run(f'shutdown /a')
    subprocess.run(f'shutdown /s /t {number}'.split(' '))

def shutdown(rule,number):
    number=int(number)*findRule(rule)  
    shutdownProcess(number)
    
if __name__=='__main__':
    shutdown(sys.argv[1],sys.argv[2])

