# 1.UPPER
# def myupper(a):
#     A_Z = list(range(65, 91))
#     a_z = list(range(97, 123))
#     ascii_dict = dict(zip(a_z, A_Z))
#     b = ''
#     for i in range(0, len(a)):
#         c = ord(a[i])
#         if c in list(ascii_dict):
#             x = chr(ascii_dict[c])
#             b += x
#         else:
#             b += a[i]
#
#     print(b)
# myupper('lskdfjsdlkfsdk;EKJEF;SDF')


# 2.LOWER
# def mylower(a):
#     A_Z = list(range(65, 91))
#     a_z = list(range(97, 123))
#     ascii_dict = dict(zip(A_Z,a_z))
#     b = ''
#     for i in range(0, len(a)):
#         c = ord(a[i])
#         if c in list(ascii_dict):
#             x = chr(ascii_dict[c])
#             b += x
#         else:
#             b += a[i]
#     print(b)
# mylower('LDKEDLF#$}@W{ELDKFSKJS')


# 3.SPLIT
# def split(a):
#     b = []
#     spl = input('Vvedite razdelitel')
#     d = ''
#     for i in range(len(a)):
#         if a[i] != spl:
#             d += a[i]
#         else:
#             b.append(d)
#             d = ""
#     if d:
#         b.append(d)
#     return b


# 4.STRIP
# def strip(a):
#     x = 0
#     y = 0
#     for i in range(len(a)):
#         if a[i] != ' ':
#             x = i
#             break
#     for j in range(len(a)-1, -1, -1):
#         if a[j] != ' ':
#             y = j
#             break
#     b = a[i:j +1]
#     return b


# 5.COUNT
# def cnt(a):
#     b = input('Vvedite simvol')
#     count = 0
#     for x in a:
#         if x == b:
#             count += 1
#     return count


# 6.FIND
# def find(a):
#     b = input('Vvedite simvol')
#     for i in range(len(a)):
#         if a[i] == b:
#             return i


# 7.JOIN
# def join(a):
#     b = ''
#     for x in a:
#         b += str(x)
#     return b


# 8.REPLACE
# def repl(a):
#     b = input('Vvedite simvol kotoryi nyzhno zamenit')
#     e = input('Vvedite simvol na kotoryi nyzhno zamenit')
#     s = 0
#     c = ''
#     if b in a:
#         for i in range(len(a)):
#             if a[i] == b:
#                 c += a[s:i] + e
#                 s = i + 1
#         return c
#     else:
#         return a


# 9.INDEX
# def index(a):
#     b = input('Vvedite element stroki')
#     for i in range(len(a)):
#         if a[i] == b:
#             return i


# 10.ISALPHA
# def is_alf(a):
#     A_Z = list(range(65, 91))
#     a_z = list(range(97, 123))
#     answ = True
#     for x in a:
#         if ord(x) not in A_Z and ord(x) not in a_z:
#             answ = False
#     return answ



# 11.STARTWITH
# def stwth(a):
#     pref = input("Enter prefix > ")
#     if a[:len(pref)] == pref:
#         return True
#     return False