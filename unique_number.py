def find_unique(num_list):
    num_dict = {n: n % 2 for n in num_list}
    print(num_dict)
    n = {v: k for k, v in num_dict.items()}
    return n


print(find_unique([3, 11, 77, 101, 6, 445, 13]))
print(find_unique([12, 34, 11, 72, 10, 6, 44, 18]))
