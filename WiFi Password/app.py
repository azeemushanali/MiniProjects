import subprocess

cmd = subprocess.check_output(['netsh','wlan','show','profiles']).decode('utf-8').split('\n')
wifis = [line.split(':')[1][1:-1] for line in cmd if "All User Profile" in line]
print(wifis)

for wifi in wifis:
    cmd2 = subprocess.check_output(['netsh','wlan','show','profiles',wifi,'key=clear']).decode('utf-8').split('\n')
    lines = [line.split(':')[1][1:-1] for line in cmd2 if "Key Content" in line]
    try:
        print(f"Name - {wifi} PWD - {lines[0]}")
    except IndexError:
        print(f"Name - {wifi} PWD - None")
