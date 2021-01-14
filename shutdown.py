import sys,subprocess

minutes = sys.argv[1] #get minutes from user #shutdown.py 30
minutes = int(minutes) #convert 30 to integer
seconds = minutes * 60 #multiply 30 minutes by 60 to get seconds

cancel_shutdown = 'shutdown /a' #cancel shutdown as string
cancel_shutdown = cancel_shutdown.split(' ') #convert string to array

shutdown = f'shutdown /s /t {seconds}' #shutdown as string
shutdown = shutdown.split(' ') #convert string to array

subprocess.run(cancel_shutdown) #run cancel shutdown 
subprocess.run(shutdown) #run shutdown

# shutdown.py 30
# pc will shutdown in 30 minutes
# instead of writing
# shutdown /s /t 1800 
