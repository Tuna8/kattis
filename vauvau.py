import sys
def psi(psi, postar):
    laja1 = int(psi[0])
    spi1 = int(psi[1])
    ali = postar % (laja1+spi1)
    if 0 < ali <= laja1:
        return True
    else:

        return False
vnesi=""
n=2
while n > 0:
    vrstica = input() + "\n"
    vnesi += vrstica
    n -= 1
vnesi=vnesi.split()
lajajo = vnesi[:4]
postar = vnesi[4:]
pes1 = lajajo[:2]
pes2 = lajajo[2:]
sez = []
n = 0
while n <= 2:
    st=0
    if psi(pes1, int(postar[n])):
        st+=1
    if psi(pes2,int(postar[n])):
        st+=1
    sez.append(st)
    n += 1
besedilo=""
for dolzina in sez:
    if dolzina == 0:
        besedilo+= "none"+"\n"
    elif dolzina == 1:
        besedilo+="one" +"\n"
    else:
        besedilo+="both"+ "\n"
print(besedilo)