import random

class public_key:
    def __init__(self, mod, exp):
        self.mod = mod
        self.exp = exp

class private_key:
    def __init__(self, mod, exp):
        self.mod = mod
        self.exp = exp

def GCD(a, b):
    if b == 0:
        return a
    else:
        return GCD(b, a%b)

def modInverse(a, b):
    b0 = b
    y = 0
    x = 1
    if b == 1:
        return 0
    while a > 1:
        q = a // b
        t = b
        b = a % b
        a = t
        t = y
        y = x - q * y
        x = y
    if x < 0:
        x += b0
    return x

def modExp(a, e, m):
    a = a % m
    if e == 0: return 1
    if e == 1: return a
    if e & 1: return a * modExp(a, e - 1, m) % m
    else: return modExp(a * a, e >> 1, m) % m

def mulmod(a, b, m):
    x = 0
    y = a % m
    while b > 0:
        if b % 2 == 1:
            x = (x + y) % m
        y = (y * 2) % m
        b //= 2
    return x % m

def isPrime(n) : 
  
    # Corner cases 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
  
    # This is checked so that we can skip  
    # middle five numbers in below loop 
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
  
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
  
    return True

p = 0
q = 0
e = 0
n = 0
phi = 0
while True:
    p = random.randint(2, 2**30)
    q = random.randint(2, 2**30)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = random.randint(2, 2**30) % phi + 1
    if p != q\
        and\
       GCD(phi, e) == 1\
        and\
       isPrime(p)\
        and\
       isPrime(q):
       break

print(p)
print(q)
print(e)
print(n)
print(phi)  

