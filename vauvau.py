import sys
def psi(psi, postar):
    psi.strip()
    laja = psi.split()
    laja1 = int(laja[0])
    spi1 = int(laja[1])
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
vnesi.split("\n")
lajajo = vnesi[:8]
postar = vnesi[8:]
postar = postar.split()
pes1 = lajajo[:3]
pes2 = lajajo[3:]
sez = []
n = 0
while n <= 2:
    lajajo=[]
    if psi(pes1, int(postar[n])):
        lajajo.append(True)
    if psi(pes2,int(postar[n])):
        lajajo.append(True)
    sez.append(lajajo)
    n += 1

for dolzina in sez:
    if len(dolzina) == 0:
        print("none")
    elif len(dolzina) == 1:
        print("one")
    else:
        print("both")
