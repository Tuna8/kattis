besedilo=""
while True
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
        hodi = input()
        hodi = hodi.split()
        smer = hodi[0]
        kol = int(hodi[1])
        if rx>vx