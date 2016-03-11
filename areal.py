import math
ploscina = input()
ploscina = ploscina.strip()
if not ploscina.isdigit():
    print(0)
else:
    ploscina = float(ploscina)
    stra = 4 * math.sqrt(ploscina)
    print(stra)
