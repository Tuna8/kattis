slov=dict()
food=dict()
pri=""
besedilo=""
while True:
    st=int(input())
    if st==0:
        break
    else:
        while st>0:
            vrstica = input()
            vrstica=vrstica.strip()
            vrstica= vrstica.split()
            slov[vrstica[0]]=vrstica[1:]
            st-=1
    for k,i in zip(slov.keys(),slov.values()):
        for hrana in i:
            if hrana in food:
                food[hrana]=food[hrana]+[k]
            else:
                food[hrana]=[k]
    hra=sorted(food)
    for hr in hra:
        bes=""
        for c in sorted(food[hr]):
            bes+=c+" "
        besedilo+= hr+" "+bes+"\n"
    besedilo+="\n"
    pri+=besedilo
    slov=dict()
    food=dict()
    besedilo=""

print(pri)



