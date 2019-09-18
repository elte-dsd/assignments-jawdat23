import numpy as np


def get_hash_functions():
    def hash_fun1(key):
        index = key % 11
        return index

    def hash_fun2(key):
        index = (key + 1) % 11
        return index

    def hash_fun3(key):
        index = (key + 3) % 11
        return index

    def hash_fun4(key):
        index = (key + 5) % 11
        return index

    def hash_fun5(key):
        index = (key + 7) % 11
        return index

    hash_functions = [hash_fun1, hash_fun2, hash_fun3, hash_fun4, hash_fun5]
    return hash_functions, 11


def pass_stream(stream, hash_functions, hash_functions_range):
    num_hashes = len(hash_functions)
    hashes_matrix = np.zeros((num_hashes, hash_functions_range))
    for num in stream:
        for i in range(num_hashes):
            res = hash_functions[i](num)
            hashes_matrix[i][res] += 1
    return hashes_matrix


def get_count_min(hash_matrix, num, hashs_functions):
    mc = 100000000000000
    num_hash = len(hashs_functions)
    for i in range(num_hash):
        ind = hashs_functions[i](num)
        res = hash_matrix[i][ind]
        mc = min(mc, res)
    return mc


def main():
    stream = [1, 4, 7, 8, 4, 54, 76, 3, 1, 3, 5, 456, 3, 6, 7, 4, 9, 7, 0]
    hash_functions, hash_functions_range = get_hash_functions()
    hashes_matrix = pass_stream(stream, hash_functions, hash_functions_range)
    num_to_count = 0
    r = get_count_min(hashes_matrix, num_to_count, hash_functions)
    print("number ", num_to_count, " has passed ", int(r), "times approximately")


main()
