# def change_char(str1):
#     char = str1[0]
#     str1 = str1.replace(char,'$')
#     # str1 = char + str1[1:]
#     print(str1[1:])
#     return str1
# print(change_char('restart'))

# def chars_mix_up(a,b):
#     new_a = b[:2] + a[2:]
#     new_b = a[:2] + b[2:]

#     return new_a + " " + new_b
# print(chars_mix_up('abcdefgh','xyzfghj'))

def add_string(str1):
    lenght = len(str1)

    if lenght > 2:
        if str1[-3:]=='ing':
            str1 += 'ly'
        else:
            str1 += 'ing'
    return str1
print(add_string('ad'))
print(add_string("abc"))
print(add_string("string"))