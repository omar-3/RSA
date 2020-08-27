import random
import math
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

def inverseMod(x, y): return 0 if x==0 else 1 if y%x==0 else y - inverseMod(y%x ,x)*y//x

def modExp(a, e, m):
    a = a % m
    if e == 0: return 1
    if e == 1: return a
    if e & 1: return a * modExp(a, e - 1, m) % m
    else: return modExp(a * a, e >> 1, m) % m

def isPrime(n) :   
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
    if (n % 2 == 0 or n % 3 == 0): 
        return False
    for i in range(4,int(math.sqrt(n))):
        k = i
        while(k * k <= n) : 
            if (n % k == 0) : 
                return False
            k = k + i
    return True

def generate_keys():
    p = 0
    q = 0
    n = 0
    e = 0
    phi = 0
    while True:
        p = random.randint(2**10, 2**20)
        q = random.randint(2**10, 2**20)
        n = p * q
        phi = (p - 1) * (q - 1)
        e = random.randint(2, 2**20) % phi 
        if p != q and GCD(phi, e) == 1 and isPrime(p) and isPrime(q):
            break
    d = inverseMod(e, phi)
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

