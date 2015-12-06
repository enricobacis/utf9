# utf9

*Encode and decode text with UTF-9.*

## description

On April 1st 2005, IEEE released the [RFC4042][0]
"*UTF-9 and UTF-18 Efficient Transformation Formats of Unicode*"
:

> The current representation formats for Unicode (UTF-7, UTF-8, UTF-16)
> are not storage and computation efficient on platforms that utilize
> the 9 bit nonet as a natural storage unit instead of the 8 bit octet.

Since there are not so many architecture that use *9 bit nonets as natural
storage units* and the release date was on April Fools' Day, the *beautiful*
UTF-9 was forgotten and no python implementation is available.

This python module is here to fill this gap! ;)

## usage

There are only two functions:

* `utf9encode(string)`: takes a string and returns a utf9-encoded version.
* `utf9decode(data)`: takes utf9-encoded data and returns the corresponding string.

## example

    >>> import utf9
    >>> encoded = utf9.utf9encode(u'ႹЄLᒪo, 🌍ǃ')
    >>> print repr(encoded)
    'p\xe0\xb7-\x0c!1\xc3\x92\xd5\x1b\xc5\x82\x07n\x83x\xed\xdecX\xf80'
    >>> print utf9.utf9decode(encoded)
    ႹЄLᒪo, 🌍ǃ

[0]: https://www.ietf.org/rfc/rfc4042.txt
