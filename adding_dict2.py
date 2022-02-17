import copy


def merge_dict(dict1, dict2):
    f_dict = copy.copy(dict1)
    f_dict.update(dict2)
# f_dict = все пары из dict2 + пары только из dict1
    for k, v in dict1.items():
        if k in f_dict.keys():
            f_dict[k] = [v, f_dict.get(k)]
    return f_dict


print(merge_dict({'A': 1, 'C': 4, 'B': 2}, {'A': 3, 'B': 2}))
