from math import pi, sin
from sys import stdin

config = list()
dic={}
eleman=list()
count=0

for line in stdin:
   config.append(line.splitlines())

eleman.append("amplitude")
eleman.append("frequency")
eleman.append("time")

"""
======= VERIFICATION CONFIG FILE, ASSIGNING VARIABLES =======
"""
try:
    for i in range(len(config)):
        if config[i].split('=')[0].strip().lower() == eleman[i]: 
            dic[eleman[i]]=int(config[i].split('=')[1].strip())
            count+=1
        else:
            print('Expected: {}. Recieved : {}'.format(eleman[i],config[i].split('=')[0].strip()))
    
    #dic[eleman[i]]= [int(config[i].split('=')[1].strip()) , count+=1 if config[i].split('=')[0].strip().lower() == eleman[i] else print('Expected: {}. Recieved : {}'.format(eleman[i],config[i].split('=')[0].strip())) for i in range(len(config))]

    if count!= len(config):
        print('There is some error in config file, please correct it.')
        print("Expected Variables:" , len(config) ,  ", got :", count)
        exit() 

    FREQUENCY =dic['frequency'] 
    TIME =dic['time']
    AMPLITUDE =dic['amplitude']
    print('FREQUENCY=', FREQUENCY)
    print('TIME=',TIME)
    print('AMPLITUDE=',AMPLITUDE)

except Exception as e:
    print(e)
