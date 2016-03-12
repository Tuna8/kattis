
while True:
    toc = input()
    if toc == "0":
        break
    tocki =toc.strip()
    tocki = toc.split()
    tocki = list(map(float,tocki))
    x1 = tocki[0]
    y1 = tocki[1]
    x2 = tocki[2]
    y2 = tocki[3]
    p = tocki[4]
    print((abs(x1-x2)**p+abs(y1-y2)**p)**(1/p))