import random

class public_key:
    def __init__(self, n, e):
        self.n = n
        self.e = e

class private_key:
    def __init__(self, n, d):
        self.n = n
        self.d = d

def GCD(a, b):
    if b == 0:
        return a
    else:
        return GCD(b, a%b)

def invmod(a,b): return 0 if a==0 else 1 if b%a==0 else b - invmod(b%a,a)*b//a

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
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
    return True

def generate_keys():
    p = 0
    q = 0
    n = 0
    e = 0
    phi = 0
    while True:
        p = random.randint(2**30, 2**40)
        q = random.randint(2**30, 2**40)
        n = p * q
        phi = (p - 1) * (q - 1)
        e = random.randint(2, 2**30) % phi 
        if p != q and GCD(phi, e) == 1 and isPrime(p) and isPrime(q):
            break
    d = invmod(e, phi)
    pub = public_key(n, e)
    priv = private_key(n, d)
    return pub, priv

pub, priv = generate_keys()

reading = open("message.txt","r")
message = reading.read()

encrypted = open("encrypted.txt", "w")
decrypted = open("decrypted.txt", "w")



for char in message:
    number = ord(char)
    string = str(modExp(number, pub.e, pub.n)) + " "
    encrypted.write(string)

encrypted.close()

tobeDecrypted = open("encrypted.txt", "r")


tobeDecryptedList = [int(number) for number in (tobeDecrypted.read()).split(" ")[:-1]]


for number in tobeDecryptedList:
    decrypted.write(chr(modExp(number, priv.d, priv.n)))

