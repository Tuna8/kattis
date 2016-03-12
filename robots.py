napisi=""
while True:
    besedilo=""
    vnesi=input()
    if vnesi=="0 0":
        break
    velik=vnesi.split()
    vx=int(velik[0])
    vy=int(velik[1])
    mx=0
    my=0
    rx=0
    ry=0
    n=int(input())
    while n>0:
        n-=1
        hodi = input()
        hodi = hodi.split()
        smer = hodi[0]
        kol = int(hodi[1])
        if smer=="u":
            my+=kol
            ry+=kol
        elif smer=="d":
            my-=kol
            ry-=kol
        elif smer=="l":
            mx-=kol
            rx-=kol
        elif smer=="r":
            mx+=kol
            rx+=kol
        if rx>vx:
            rx=vx
        elif rx<0:
            rx=0
        if ry>vy:
            ry=vy
        elif ry<0:
            ry=0
    besedilo+="Robot thinks "+ str(mx)+ " "+ str(my)+"\n"
    besedilo+= "Actually at " +str(rx)+" "+ str(ry)+"\n"+"\n"
    napisi+=besedilo
print(napisi)


