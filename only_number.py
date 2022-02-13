def only_numbers(s):
    _sum = 0
    for i in s:
        try:
            _sum += int(i)
        except ValueError:
            pass

    return _sum


symbols = [1, 5, 9, 100, '100', 5, '80', 'd', '100']
sum_of_num = only_numbers(symbols)
with open('fo', 'w+') as f:
    f.write(str(sum_of_num))
