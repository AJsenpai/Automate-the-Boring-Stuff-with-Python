# Coin Flip streak        

import random
numberOfStreaks = 0
HTmapping={1: 'T' , 0: 'H'}
HTlist=[]
for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    random.randint(0,1)
    HTlist.append(HTmapping.get(random.randint(0,1)))
# print(HTlist)

if len(HTlist)<6:
    print("len of list less than 6 to make a streak")
else:

    for i in range(0,len(HTlist)-5):
        if HTlist[i]==HTlist[i+1] and HTlist[i+1]==HTlist[i+2] and HTlist[i+2]==HTlist[i+3] and HTlist[i+3]==HTlist[i+4] and HTlist[i+4]==HTlist[i+5] and len(HTlist)>6:
            numberOfStreaks+=1
    
    # Code that checks if there is a streak of 6 heads or tails in a row.
    print('Chance of streak: %s%%' % (numberOfStreaks / 100))
