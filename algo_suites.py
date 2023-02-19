#1
def rang_n(n:int):
    return 2*n**2-n+1
#2
rang_n(5) # 46
#3 
def suite(n):
    return[2*i**2-i+1 for i in range(0,n+1)]

#--------

def rang_n(n:int):
    u=3
    for i in range(0,n):
        u = 2*i -4
    return u
#2 rang_n(4)=2

#3 la fonction mystère ca 
#4 mystere(2) = -3

#--------
#1 un = 1/3*2**n
def seuil():
    n = 0
    u = 1/3
    while u<= 10:
        n +=1
        u = 1/3*2**n
    return n
#--------
# 1 : U3 = -1
def suite(n):
    u = 1
    for i in range(0,n):
        u = -3*u + 2*i + 4
    return u
#--------
#5  1. un = -4 + n*1/2
import matplotlib.pyplot as plt.
u0 = 4
r = 1/2
n = 100
un = [u0 + k*r for k in range(n)]
plt.plot(range(n), un, 'o')
plt.title("Suite arithmétique de premier terme u0=4 et de raison 1/2")
plt.xlabel("n")
plt.ylabel("Un")
plt.show()
#3 on retrouve une fonction homographique qui admet une asymptote horizontale en y=0
#--------
#6: 1 : un = 1,5^n
import matplotlib.pyplot as plt
x = [x for n in range(20)]
y = [1,5**x for n in range(20)]
plt.scatter(x,y)
plt.show()
#3 : on conjecture, à l'aide de la représentation graphique, n=18
def seuil():
    n = 0
    u = 1
    while u <= 1000:
        n += 1 
        u = 1.5**n
    return n
#--------
# 7 : l'augmentation de la population européenne est d'environ 0,30%
def population(n):
    u = 511.8
    for i in range(n+1):
        u += 1.5
    return round(u*1000000)
#3: on multiplie les resultats par un million pour rendre l'écriture plus lisible.
population(2040-2017)
