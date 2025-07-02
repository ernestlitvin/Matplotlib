import random

import matplotlib.pyplot as plt
import numpy as np


# langas, grafikas = plt.subplots()
# plt.show()

# langas, grafikas = plt.subplots(2,2)
# plt.show()

# x = [5,15,20,25]
# y = [14,26,5,44]
# mer,per = plt.subplots()
# per.plot(x,y,marker='8', linestyle=':', color='#c875c4', markersize=12)
# plt.show()

# def f(t):
#     return np.exp(-t) * np.cos(2*np.pi*t)
# t1 = np.arange(0.0, 5.0, 0.1)
# fig, ax = plt.subplots()
# ax.plot(t1, f(t1), color='red', marker='d', ms=12, lw=3.0, label='$e^{-x}\cdot\cos(2\pi x)$')
# ax.set_ylabel('Y ašies pavadinimas')
# ax.set_xlabel('X ašies pavadinimas')
# ax.set_title('Grafiko pavadinimas')
# ax.legend(loc=9) # 0 - 9
# plt.show()

###--- UZD A --- ###

# A) Duotas sąrašas x=[1,2,3,4,5,6,7,8,9]
# Viename lange, skirtinguose grafikuose atvaizduokite 𝑥2, 𝑥 ⋅ 3,
# 𝑥 ⋅ 𝑎, čia a - įvedamas vartotojo.
# Panaudokite skirtingas spalvas, linijų tipus.

# x=[1,2,3,4,5,6,7,8,9]
#
# langas, grafikas = plt.subplots(3)
#
# a = int(input("Iveskite skaiciu a: "))
#
# y1 = [i**2 for i in x]
# y2 = [i*3 for i in x]
# y3 = [i*a for i in x]
#
# grafikas[0].plot(x,y1, marker='8', linestyle=':', color='#c875c4', markersize=12)
# grafikas[1].plot(x,y2, marker='s', linestyle='--', color='red', markersize=10)
# grafikas[2].plot(x,y3, marker='d', linestyle='-', color='blue', markersize=8)
#
# grafikas[0].set_title("x^2")
# grafikas[1].set_title("x*3")
# grafikas[2].set_title(f"x*{a}")
#
# plt.show()


###--- UZD B --- ###

# Duoti sąrašai
# x = [1,2,3,4,5],
# y1= [2,2,0,0,2],
# y2) = [4,3,2,1,-1],
# y3) = [2,4,9,16,25],
# y4) = [-1,1,-1,1,-1]
#
# Atvaizduokite viename lange, skirtinguose grafikuose x~y1, x~y2, x~y3, x~y4 grafikus.
# Pirmasis grafikas - linijinis, antrasis - taškinis,
# trečiasis - linija su duomenų taškais,
# ketvirtasis - brūkšninis.
# Spalvos visų turi būti skirtingos. Grafikai, ašys turi turėti pavadinimus.

'''x = [1,2,3,4,5]
y1= [2,2,0,0,2]
y2 = [4,3,2,1,-1]
y3 = [2,4,9,16,25]
y4 = [-1,1,-1,1,-1]

langas, grafikas = plt.subplots(4,1, figsize=(4,8))

grafikas[0].plot(x,y1, marker='o', color='red', markersize=12)
grafikas[1].scatter(x,y2, marker='s', color='#c875c4')
grafikas[2].plot(x,y3, marker='d', linestyle='-.', color='blue', markersize=12)
grafikas[3].bar(x,y4, color='purple')

grafikas[0].set_title('Grafika 1')
grafikas[1].set_title('Grafika 2')
grafikas[2].set_title('Grafika 3')
grafikas[3].set_title('Grafika 4')

grafikas[0].set_xlabel('X asis')
grafikas[1].set_xlabel('X asis')
grafikas[2].set_xlabel('X asis')
grafikas[3].set_xlabel('X asis')

grafikas[0].set_ylabel('Y asis')
grafikas[1].set_ylabel('Y asis')
grafikas[2].set_ylabel('Y asis')
grafikas[3].set_ylabel('Y asis')

plt.tight_layout()
plt.show()
'''

###--- UZD C --- ###

# Sugeneruoti sąrašą 𝑥, turintį 101 elementą (nuo 0 iki 100).
# Sukurti antrą sąrašą, kuriame būtų skaičiai, pakelti kvadratu, iš pirmojo sąrašo (𝑥2)
# Sukurti trečiąjį sąrašą, kuriame skaičiai būtų pakelti kvadratu ir padauginti iš atsitiktinai sugeneruoto skaičiaus (𝑥2 ⋅ 𝑎).
# Sugeneruoti 100-to elementų ilgio sąrašą iš atsitiktinių skaičių.
# Visus šiuos sąrašus atvaizduoti grafike.
# Grafikas turi turėti pavadinimą, pavadintos ašys, pakeisti šriftų dydžiai.

# x1 = list(range(101))
# x2 = [i**2 for i in x1]
# a = random.randint(1,100)
# x3 = [i * a for i in x2]
# x4 = [random.randint(1,100) for _ in range(100)]
#
# mer,per = plt.subplots()
# per.plot(x1,x1,marker='o', linestyle=':', color='#c875c4', markersize=1, label = "x1")
# per.plot(x1,x2, marker = 'd', linestyle='-.', color='red', markersize=5, label = "x1^2")
# per.plot(x1,x3, marker = 's', linestyle='-.', color='blue', markersize=3, label = "x^2*a")
# per.scatter(range(len(x4)), x4, color='green', label='Random values', s=64)
#
# per.set_yscale('log')
# per.set_title('Grafikas visu asiu')
# per.set_xlabel('X asis', fontsize=8)
# per.set_ylabel('Y asis', fontsize=10)
#
# plt.tight_layout()
# per.legend()
# plt.show()







