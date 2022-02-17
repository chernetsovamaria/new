def merge_dict(dict1, dict2):
    f_dict = {}
    for k1, v1 in dict1.items():
        if k1 in dict2.keys():
            f_dict[k1] = [v1, dict2.get(k1)]
        else:
            f_dict[k1] = v1
    for k, v in dict2.items():
        if k not in f_dict.keys():
            f_dict[k] = v
    return f_dict


print(merge_dict({'A': 1, 'C': 4, 'B': 2}, {'A': 3, 'B': 2}))
