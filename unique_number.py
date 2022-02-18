def find_unique(num_list):
    rem = 0
    num_dict = {d: d % 2 for d in num_list}
    for i in num_dict.values():
        rem += i
    if rem == 1:
        for k, v in num_dict.items():
            if v == 1:
                return k
    elif rem > 1:
        for k, v in num_dict.items():
            if v == 0:
                return k


print(find_unique([4, 6, 21, 8, 10]))
print(find_unique([3, 7, 24, 3, 11]))
