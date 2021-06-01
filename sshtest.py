import paramiko
import sys
from idpw import *



sys.stdout = open('C:\\Users\\HJ\\Desktop\\lastlog_app.txt', 'w')

# CommandLine = 'last -10 | grep -v 121 | grep -v wtmp | grep -v reboot'
CommandLine = 'mount -l | grep 216'

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# client.connect( hostname = app2Ip , port=50022 , username=appId, password=app2Pw)
# stdin, stdout2, stderr = client.exec_command(CommandLine)

for i in range(1,14):
    if (i==1) or (i==5) or (i==10):
        print("")
    else:
        client.connect( hostname = globals()['app{}Ip'.format(i)] , port=50022 , username=appId, password=globals()['app{}Pw'.format(i)])
        stdin, globals()['stdout{}'.format(i)], stderr = client.exec_command(CommandLine)

        print("===== app"+str(i)+"서버 =====")
        for line in globals()['stdout{}'.format(i)]:
            print(line)

sys.stdout.close()