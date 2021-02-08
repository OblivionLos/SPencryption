def before_print(string):
    result = ""
    temp = ""
    for i in range(1, len(string) + 1):
        temp += string[i - 1]
        if (i % 16 == 0):
            result += bin_to_hex(temp)
            temp = ""
    return result

def divide(string):
    result = []
    temp = ""
    for i in range(1, len(string) + 1):
        temp += string[i - 1]
        if (i % 16 == 0):
            result.append(temp)
            temp = ""
    return result

def bin_to_dec(string):
    return str(int(string, 2))

def bin_to_hex(s):
    return str(hex(int(s, 2)).zfill(6).replace("0x", ""))

def dec_to_bin(string):
    return bin(string).zfill(6).replace("0b", "")

def hex_to_bin(s):
    temp = ""
    res = ""
    for i in range(1, len(s) + 1):
        temp += s[i - 1]
        if i % 4 == 0:
            res += bin(int(temp, 16)).zfill(18).replace("0b", "")
            temp = ""
    return res

def hex_to_norm(s):
    result = ""
    for i in range(0, len(s), 4):
        result += chr(int(s[i: i + 4], 16))
    return result

def norm_to_hex(s):
    result = []
    for i in s:
        result.append(str(hex(ord(i)).zfill(6).replace("0x", "")))
    return "".join(result)