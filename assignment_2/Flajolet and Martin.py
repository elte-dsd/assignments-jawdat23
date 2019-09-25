import numpy as np


def lssbp(x):
    """
    :param x:
    :return: least significant set bit position
    """
    if x == 0:
        return 0
    else:
        return (x & -x).bit_length() - 1


def get_hash_function():
    hash_range = 11

    def hash_fun(key):
        code = 0
        if isinstance(key, str):
            for char in key:
                code += ord(char)
        elif isinstance(key, int):
            code = key

        index = code % hash_range
        return index

    return hash_fun, hash_range


def pass_stream(stream, hash_function, hash_function_range):
    bitmap = np.zeros(hash_function_range)
    for num in stream:
        i = lssbp(hash_function(num))
        bitmap[i] = 1
    return bitmap


def get_cardinality(bitmap):
    r = 0
    for i in range(len(bitmap)):
        if bitmap[i] == 1:
            r = i
    return 2 ** r / 0.77351


def main():
    '''
    input: stream
    ouput: cardinality
    dependencies: numpy
    '''
    stream = [54, 4, 7, 8, 4, 4, 7, 3, 1, 3, 5, 9, 3, 6, 7, 4, 9, 7, 'a', 'abc']
    hash_fun, hash_range = get_hash_function()
    bitmap = pass_stream(stream, hash_fun, hash_range)
    cardinality = get_cardinality(bitmap)
    print("there are approximately ", cardinality, " unique numbers have passed.")


main()