from Crypto.Cipher import *
from Crypto.Hash import SHA256
import bcrypt
from random import *
import string

def hashPrint(one, two):
    hash = SHA256.new()
    hash.update(one.encode())
    hashOne = hash.hexdigest()
    hash = SHA256.new()
    hash.update(two.encode())
    hashTwo = hash.hexdigest()
    print("\nFirst String:")
    print(one, "->", hashOne)
    print("\nSecond String:")
    print(two, "->", hashTwo)


def main():
    availOptions = string.ascii_letters + string.digits
    one = ""
    two = ""
    for _ in range(0, 8):
        one += choice(availOptions)
        two += choice(availOptions)

    hashPrint(one, two)

    # hello world! : 01101000 01100101 01101100 01101100 01101111 00100000 01110111 01101111 01110010 01101100 01100100 00100001
    # hello worl$! : 01101000 01100101 01101100 01101100 01101111 00100000 01110111 01101111 01110010 01101100 00100100 00100001
    test1, test2 = "hello world!", "hello worl$!"
    print("\nString 1:", test1)
    print("String 2:", test2)
    print("Hamming Distance:", sum(c1 != c2 for c1, c2 in zip(test1, test2)))

    # computer science: 01100011 01101111 01101101 01110000 01110101 01110100 01100101 01110010 00100000 01110011
    # 01100011 01101001 01100101 01101110 01100011 01100101
    # co}puter science: 01100011 01101111 01111101 01110000 01110101 01110100 01100101 01110010 00100000 01110011
    # 01100011 01101001 01100101 01101110 01100011 01100101
    test3, test4 = "computer science", "co}puter science"
    print("\nString 1:", test3)
    print("String 2:", test4)
    print("Hamming Distance:", sum(c1 != c2 for c1, c2 in zip(test3, test4)))

    print()
    
    storage = {}
    sizeList = [num for num in range(8, 51, 2)]

    for bit_size in sizeList:
        count = 0
        for x in range(10000):
            test = SHA256.new()
            a = ''.join([choice(availOptions) for _ in range(10)])
            test.update(a.encode())

            bnum = bin(int.from_bytes(test.digest(), byteorder='big'))[2:(2+bit_size)]
            if bnum in storage.keys():
                storage[bnum].append(a)
                count += 1
            else:
                storage[bnum] = [a]


        print(len(storage.keys()) == len(set(storage.keys())))
        print(count)

if __name__ == "__main__":
    main()