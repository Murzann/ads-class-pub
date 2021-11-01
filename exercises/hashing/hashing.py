#!/usr/bin/env python3
"""
`hashing` implementation and driver

@authors: Aidan Brook
@version: 2021.10
"""


def hash_remainder(key: int, size: int) -> int:
    """
    Find hash using remainder

    :param key: key to hash
    :param size: size of the map
    :returns: hash of the key
    >>> hash_remainder(160, 11)
    6
    >>> hash_remainder(160, 12)
    4
    """
    # TODO: Implement this function
    a = (key%size)
    return a
    


def hash_mid_sqr(key: int, size: int) -> int:
    """
    Find hash using mid-square method

    :param key: key to hash
    :param size: size of the map
    :returns: hash of the key
    >>> hash_mid_sqr(160, 11)
    1
    >>> hash_mid_sqr(160, 12)
    8
    """
    square = str(key * key)

    if len(square) < 4:
        square = "0"*(4-len(square))+square

    elif len(square) % 2 == 1:
        square = "0"+ square


    secondIndex = len(square)//2
    firstIndex = secondIndex-1
   
    numFinal = int(square[firstIndex] + square[secondIndex])

    return numFinal %size

    


def hash_folding(key: str, size: int) -> int:
    """
    Find hash using folding method

    :param key: key to hash
    :param size: size of the map
    :returns: hash of the key
    >>> hash_folding('2021-10-24', 11)
    9
    >>> hash_folding('10/24/2021', 12)
    3
    """
    compiled_list = ''  
    hashlist = key
    total = 0
    
    for i in hashlist:
        if i.isdigit() is True:
            compiled_list += i

        if len(compiled_list) == 2:
            hashed_item = int(compiled_list[0]+compiled_list[1])
            total = total + hashed_item
            compiled_list = ''

    if len(compiled_list)%2 == 1:        
        total = (int(hashlist[:-1])) + total
    

    return total%size


def hash_str(key: str, size: int) -> int:
    """
    Find string hash using simple sum-of-values method

    :param key: key to hash
    :param size: size of the map
    :returns: hash of the key
    >>> hash_str('Hello World', 11)
    7
    >>> hash_str('Hello World', 12)
    8
    """
    # TODO: Implement this function    
    return sum([ord(c) for c in key]) % size


def hash_str_weighted(key: str, size: int) -> int:
    """
    Find string hash using character positions as weights

    :param key: key to hash
    :param size: size of the map
    :returns: hash of the key
    >>> hash_str_weighted('Hello World', 11)
    5
    >>> hash_str_weighted('Hello World', 12)
    4
    """
    # TODO: Implement this function
    # total = 0
    
    # # for item in key:
    # #     pos = key.index(item) 
    # #     total = int(ord(item)*pos) + total
     
    # # return total%size

    position = 0
    total = 0
    for x in key:
        total = total + (ord(x)*position)
        position += 1
    return total % size

def main():
    """Main function"""
    keys_int = [10, 21, 32, 18, 17, 19, 42, 23, 99]
    keys_int_2 = [54, 26, 93, 17, 77, 31]
    keys_intstr = ["563-555-1234", "800-555-8080", "888-555-0000"]
    keys_intstr_2 = ["436-555-4601"]
    keys_str = [
        "pavel",
        "bruce",
        "talia",
        "harvey",
        "jim",
        "alfred",
        "lucius",
        "jonathan",
        "bane",
    ]
    keys_str_2 = ["algorithm", "logarithm"]

    print("Simple remainder")
    print([hash_remainder(x, 16) for x in keys_int])
    print([hash_remainder(x, 11) for x in keys_int_2])

    print("Mid-square")
    print([hash_mid_sqr(x, 16) for x in keys_int])
    print([hash_mid_sqr(x, 11) for x in keys_int_2])

    print("Folding")
    print([hash_folding(x, 16) for x in keys_intstr])
    print([hash_folding(x, 11) for x in keys_intstr_2])

    print("String hashing")
    print([hash_str(x, 16) for x in keys_str])
    print([hash_str(x, 11) for x in keys_str_2])

    print("Weighted string hashing")
    print([hash_str_weighted(x, 16) for x in keys_str])
    print([hash_str_weighted(x, 11) for x in keys_str_2])


if __name__ == "__main__":
    main()
