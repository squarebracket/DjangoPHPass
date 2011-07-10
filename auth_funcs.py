# This file implements PHPass-style authentication
from hashlib import md5
from django.utils.encoding import smart_str
itoa64 = "./0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def encode64(input, count):
    global itoa64
    output = ''
    i = 0
    while i <= count:
        value = ord(input[i])
        i = i + 1
        output += itoa64[value & 0x3f]
        if i < count:
            value |= ord(input[i]) << 8
        output += itoa64[(value >> 6) & 0x3f]
        if i >= count:
            break
        i = i+1
        if i < count:
            value |= ord(input[i]) << 16
        output += itoa64[(value >> 12) & 0x3f]
        if i >= count:
            break
        i = i+1
        output += itoa64[(value >> 18) & 0x3f]
    return output

def hash(password, existing_hash):
    global itoa64
    password = smart_str(password)
    countlog2 = itoa64.index(existing_hash[3])
    count = 1 << countlog2
    salt = existing_hash[4:12]
    
    hash = md5(salt + password).digest()
    while count > 0:
        hash = md5(hash + password).digest()
        count -= 1
    output = existing_hash[0:12]
    output += encode64(hash, 16)
    return output
