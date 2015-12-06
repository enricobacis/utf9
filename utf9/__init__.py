# -*- coding: utf-8 -*-

from bitarray import bitarray as _bitarray

def utf9encode(string):
    bits = _bitarray()
    for char in string:
        for idx, byte in enumerate(char.encode('utf-8')):
            bits.append(idx)
            bits.extend('{0:b}'.format(ord(byte)).zfill(8))
    return bits.tobytes()

def utf9decode(data):
    bits = _bitarray()
    bits.frombytes(data)
    chunks = (bits[x:x+9] for x in xrange(0, len(bits), 9))
    string = u''
    codepoint = ''
    for chunk in chunks:
        if len(chunk) < 9:
            break
        if chunk[0] == 0:
            codepoint, string = '', string + codepoint.decode('utf-8')
        codepoint += chr(int(chunk[1:].to01(), 2))
    return string + codepoint.decode('utf-8')
