from pprint import pprint as pp

def numberOfSetBits(i):
    i = i - ((i >> 1) & 0x55555555)
    i = (i & 0x33333333) + ((i >> 2) & 0x33333333)
    return (((i + (i >> 4) & 0xF0F0F0F) * 0x1010101) & 0xffffffff) >> 24

def int2bits(n):
    return [('{i:0>{n}b}'.format(i=i, n=n), numberOfSetBits(n)) for i in range(2**n)]

pp(int2bits(n=8))