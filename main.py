'''
3. Feladat
A program generáljon 10 darab véletlenszámot [0;50] intervallumon, de csak a 4-gyel oszthatóakat rögzítse egy listában. A végén jelenítse meg a listát a képernyőn, és írja ki azt is, hány elemből áll a lista.
'''

from random import randint

lista = []
for i in range(10):
    szam = randint(0,50)
    if szam % 4 == 0:
        lista.append(szam)

print(lista)

print(len(lista))