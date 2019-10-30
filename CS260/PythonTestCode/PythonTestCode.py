import random
import string
import collections

def hasher(product_id, table_size):
    output = 0xFFFF
    for i in range(0, len(product_id)):
        output ^= ord(product_id[i]) << 8
        for j in range(0,8):
            if (output & 0x8000) > 0:
                output =(output << 1) ^ 0x1021
            else:
                output = output << 1
    return (output & 0xFFFF)%table_size

if __name__=="__main__":
    letters = string.ascii_uppercase
    table = []
    for x in range(1000):
        s = str(random.randint(0,9)) + random.choice(letters) + random.choice(letters) 
        s = s + str(random.randint(0,9)) + str(random.randint(0,9)) + random.choice(letters)
        hash_key = hasher(s, 1000)
        table.append(hash_key)
    table.sort()
    counted=collections.Counter(table)
    collisions=1000-len(counted.keys())
    print("Total collisions: " + str(collisions))




