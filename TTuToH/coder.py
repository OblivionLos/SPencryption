from TTuToH.data_converter import *
from TTuToH.constants import *

def convert(dic):
    res = {}
    for key in dic:
        res[dic.get(key)] = key
    return dict(sorted(res.items()))

def permutation(string, d):
    result = ""
    for i in range(0, len(string)):
        result += string[d[i]]
    return result

def substitution(string, d):
    result = ""
    temp = ""
    index = 0
    for i in range(1, len(string) + 1):
        temp += string[i - 1]
        if (i % 4 == 0):
            result += dec_to_bin(d[index].get(int(bin_to_dec(temp))))
            index += 1
            temp = ""
    return result
    
def encode(string):
    result = ""
    string = divide(hex_to_bin(string))
    for i in string:
        i = substitution(i, [S1, S2, S3, S4])
        i = permutation(i, P1)
        i = substitution(i, [S5, S6, S7, S8])
        i = permutation(i, P2)
        i = substitution(i, [S9, S10, S11, S12])
        i = permutation(i, P3)
        result += i
    return before_print(result)

def decode(string):
    result = ""
    string = divide(hex_to_bin(string))
    for i in string:
        i = permutation(i, convert(P3))
        i = substitution(i, [convert(d) for d in ([S9, S10, S11, S12])])
        i = permutation(i, convert(P2))
        i = substitution(i, [convert(d) for d in ([S5, S6, S7, S8])])
        i = permutation(i, convert(P1))
        i = substitution(i, [convert(d) for d in ([S1, S2, S3, S4])])
        result += i
    
    result = before_print(result)
    
    return result,hex_to_norm(result)




