def decode(message):
    message = message.lower()
    alphabet = 'abcdefghigklmnopqrstuvwxyz'
    decoded_mes = []
    for i in list(message):
        if i in alphabet:
            letter_index = alphabet.index(i)
            decoded_mes.append(alphabet[-(letter_index + 1)])
        else:
            decoded_mes.append(i)
    print(''.join(decoded_mes))


decode('svool')
decode('try to decide this')
decode('')
