from zdi import *
with open('order.txt', 'r') as file:
    for name in file.readlines():
        DynSpecI(filename='v471tau_05.ss', filename2=name.split()[1], save='dyn'+name.split()[0])
