import random
hardwork=[0]*1000
luck=[0]*1000
total=[0]*1000
avg_hardwork,avg_luck=0,0
for z in range(0,10000):
    for i in range(0,len(total)):
        hardwork[i]=random.randrange(0,101)
        luck[i]=random.randrange(0,6)
        total[i]=luck[i]+hardwork[i]
    winner1=total.index(max(total))
    less_luck,less_hardwork=0,0
    for i in range(0,len(total)):
        if luck[i]<luck[winner1]:
            less_luck+=1
        if hardwork[i]<hardwork[winner1]:
            less_hardwork+=1
    avg_luck+=less_luck*100/len(total)
    avg_hardwork+=less_hardwork*100/len(total)
print("The avg hardwork %ile of winner is ",avg_hardwork/10000)
print("The avg luck %ile of winner is ",avg_luck/10000)
