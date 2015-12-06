# -*- coding: utf-8 -*-
"""Encode and decode text using UTF-9.

On April 1st 2005, IEEE released the RFC4042 "UTF-9 and UTF-18 Efficient
Transformation Formats of Unicode" (https://www.ietf.org/rfc/rfc4042.txt)

> The current representation formats for Unicode (UTF-7, UTF-8, UTF-16)
> are not storage and computation efficient on platforms that utilize
> the 9 bit nonet as a natural storage unit instead of the 8 bit octet.

Since there are not so many architecture that use *9 bit nonets as natural
storage units* and the release date was on April Fools' Day, the *beautiful*
UTF-9 was forgotten and no python implementation is available.

This python module is here to fill this gap! ;)

Example:
    >>> import utf9
    >>> encoded = utf9.utf9encode(u'ႹЄLᒪo, 🌍ǃ')
    >>> print utf9.utf9decode(encoded)
    ႹЄLᒪo, 🌍ǃ
"""

from bitarray import bitarray as _bitarray

def utf9encode(string):
    """Takes a string and returns a utf9-encoded version."""
    bits = _bitarray()
    for char in string:
        for idx, byte in enumerate(char.encode('utf-8')):
            bits.append(idx)
            bits.extend('{0:b}'.format(ord(byte)).zfill(8))
    return bits.tobytes()

def utf9decode(data):
    """Takes utf9-encoded data and returns the corresponding string."""
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
