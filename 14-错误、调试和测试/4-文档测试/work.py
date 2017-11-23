#!/home/yj/.virtualenvs/py3.5.3/bin/python3.5
# -*- coding: utf-8 -*-

def fact(n):
    '''
    >>> fact(0)
    Traceback (most recent call last):
        ...
    ValueError
    >>> fact(1)
    1
    >>> fact(2)
    2
    >>> fact(3)
    6
    >>> fact('a')
    Traceback (most recent call last):
        ...
    TypeError: unorderable types: str() < int()
    '''
    if n < 1:
        raise ValueError()
    if n == 1:
        return 1
    return n * fact(n - 1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()