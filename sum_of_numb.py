def only_numbers(s):
    _sum = 0
    for i in s:
        i = str(i)
        if i.isnumeric():
            _sum += int(i)
    return _sum


symbols = [1, 5, 'g', '4', '123']
sum_of_num = only_numbers(symbols)
with open('sum_of_numbers', 'w+') as f:
    f.write(str(sum_of_num))
