import subprocess

with open('order.txt', 'r') as file:
    for name in file.readlines():
        complete = subprocess.run(['sh','./zdiunspotted', name.split()[0], name.split()[1][0:-3]+'u'], stdout=subprocess.PIPE)
