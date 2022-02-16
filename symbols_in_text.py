with open('lyrics.txt', encoding='utf8') as f:
    lyrics = f.read()
lyrics_list = []
banned = [' ', '.', ',', '!', '?', '\n', '']
lyrics_word = ''
for i in lyrics:
    if i in banned:
        if lyrics_word != '':
            lyrics_list.append(lyrics_word)
            lyrics_word = ''
    else:
        lyrics_word += i.lower()
check_dupes = {}
for i in lyrics_list:
    if i not in check_dupes:
        check_dupes[i] = lyrics_list.count(i)
max_value = {}
_values = check_dupes.values()
for i1, i2 in check_dupes.items():
    if i2 == max(_values):
        max_value[i1] = i2
print(check_dupes)
print(max_value)
