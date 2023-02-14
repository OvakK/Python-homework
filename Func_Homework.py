# 1.Գրել ֆունկցիա որը կվերդարձնի ստացած արգումենտներից թվերի գումարը։
#
# def f(*args):
#     summ = 0
#     for x in args:
#         if type(x) == int or type(x) == float:
#             summ += x
#     return summ
#
# print(f(3, 5, 7, "asd", 0, 5.7))

# 2.Գրել ֆունկցիա որը կվերդարձնի ստացած արգումենտներից տողերի քանակը։
#
# def f(*args):
#     count = 0
#     for x in args:
#         if type(x) == str:
#             count += 1
#     return count
#
# print(f(1, 2, 3, 'asd', 6, 'fds'))

# 3.Գրել ֆունկցիա որը կվերադարձնի ստասած արգումենտների միջին թվաբանականը։
#
# def f(*args):
#     return sum(args) / len(args)
#
# print(f(1, 2, 3))

# 4.Գրել ֆունկցիա որը կստանա արգումենտ և կվերադարձնի այդ
# արգումենտերի հետ կատարած մաթեմատիկական գործողությունների արդյունքները։
#
# def f(*args, a):
#     x = args[0]
#     if a == '-':
#         for i in range(1, len(args)):
#             x -= args[i]
#     if a == '+':
#         for i in range(1, len(args)):
#             x += args[i]
#     if a == '*':
#         for i in range(1, len(args)):
#             x *= args[i]
#     if a == '/':
#         for i in range(1, len(args)):
#             x /= args[i]
#     return x
#
# print(f(1, 2, 3, 4, a='*'))

# 5.Գրել ֆունկցիա որը որպես արգումենտ կստանա տողը և կվերադարձնի
# այն դարձված ամբողջությամբ մեծատառ ֆունկցիան օգտագործել չի (upperկարելի ։)
#
# def f(mstr):
#     A_Z = list(range(65, 91))
#     a_z = list(range(97, 123))
#     ascii_dict = dict(zip(a_z, A_Z))
#     b = ''
#     for i in range(0, len(mstr)):
#         c = ord(mstr[i])
#         if c in list(ascii_dict):
#             x = chr(ascii_dict[c])
#             b += x
#         else:
#             b += mstr[i]
#
#     return b
#
# print(f('ABSabc,.'))

# 6.Գրել ֆունկցիա որը որպես արգումենտ կստանա տողը և կվերադարձնի
# այն դարձված ամբողջությամբ փոքրատառ ֆունկցիան օգտագործել չի (lower կարելի ։)
#
# def f(mstr):
#     A_Z = list(range(65, 91))
#     a_z = list(range(97, 123))
#     ascii_dict = dict(zip(A_Z, a_z))
#     b = ''
#     for i in range(0, len(mstr)):
#         c = ord(mstr[i])
#         if c in list(ascii_dict):
#             x = chr(ascii_dict[c])
#             b += x
#         else:
#             b += mstr[i]
#     return b
#
# print(f('ABCabc,./'))

# 7.Գրել ֆունկցիա որը որպես արգումենտ կստանա տողը և կվերադարձնի
# այն դարձված բոլոր բառերի առաջին տառերը մեծատառ ֆունկցիան (title օգտագործել չի կարելի ։ )
#
# def f(mstr):
#     A_Z = list(range(65, 91))
#     a_z = list(range(97, 123))
#     ascii_dict = dict(zip(a_z, A_Z))
#     lst = mstr.split()
#     c = ''
#     for x in lst:
#             y = ord(x[0])
#             if y in ascii_dict:
#                 c = c + chr(ascii_dict[y]) + x[1:]
#             else:
#                 c += x
#             c += ' '
#     return c
#
# print(f('hello my friend .'))

# 8.Գրել ֆունկցիա որը որպես արգումենտ կստանա տողը և կվերադարձնի
# այն դարձված հակառակ։
#
# def f(mstr):
#     my_mstr = ''
#     for x in mstr:
#         my_mstr = x + my_mstr
#     return my_mstr
#
# print(f('Hello world'))

# 9.Գրել ֆունկցիա որը որպես արգումենտ կստանա տող և թիվ։ Այն պետք է
# վերադարձնի տրված թվերի արանքում եղած ենթատողը։
#
# def f(a, b, c):
#     mstr = a[b : c +1]
#     return mstr
#
# print(f('python', 2, 4))

# 10.Գրել ֆունկցիա որը կվերադարձնի նախադասության ամենաերկար բառը։
#
# def f(mstr):
#     lst = mstr.split()
#     word = mstr[0]
#     for x in lst:
#         if len(x) > len(word):
#             word = x
#     return word
#
# print(f("Process finished with exit code 0"))

# 11.Գրել ֆունկցիա որը կվերադարձնի նախադասության ամենա շատ օգտագործված տառը։
#
# def f(mstr):
#     d = dict()
#     for x in mstr:
#         if x.isalpha():
#             if x in d:
#                 d[x] += 1
#             else:
#                 d[x] = 1
#     lst = [(value, key) for key, value in d.items()]
#     return max(lst)[1]
#
# print(f('Process finished with exit code 0'))

# 12.Գրել ֆունկցիա որը կվերադարձնի նախադասության ամենա երկար բառում ամենաշատ օգտագործված տառը։

# def f(mstr):
#     lst = mstr.split()
#     longes_word = lst[0]
#     for x in lst:
#         if len(x) > len(longes_word):
#             longes_word = x
#
#     d = dict()
#     for x in longes_word:
#         if x.isalpha():
#             if x in d:
#                 d[x] += 1
#             else:
#                 d[x] = 1
#     lst = [(value, key) for key, value in d.items()]
#     return max(lst)[1]
#
# print(f("Process finished with exit code"))

# 13.Գրել ֆունկցիա որը որպես արգումենտ կստանա տող և թիվ։
# Կվերադարձնի այդ թվին համապատասխն ինդեքսում եղած էլէմենտները՝ սկզբից և վերջից։
#
# def f(mstr, a):
#     return mstr[a], mstr[-a]
#
# print(f("Process finished with exit code", 5))

# 15.Գրել ֆունկցիա որը որպես արգումենտ կստանա թիվ և կստուգի պոլինդրոմ է այն թե ոչ։

# def f(x):
#     mstr = str(x)
#     if mstr == mstr[::-1]:
#         return True
#     return False

# def f(x):
#     lst = []
#     while x != 0:
#         a = x % 10
#         lst.append(a)
#         x = x // 10
#     if lst == lst[::-1]:
#         return True
#     return False
#
#
# print(f(101))

# 16․Գրել ֆունկցիա որը որպես արգումենտ կստանա թիվ և կվերադարձնի իրեն ամենամոտ պոլինդրոմ թիվը։
#
# def f(x):
#     if str(x) == str(x)[::-1]:
#         return x
#     up_x = x + 1
#     down_x = x - 1
#     while True:
#         if str(up_x) == str(up_x)[::-1]:
#             return up_x
#         elif str(down_x) == str(down_x)[::-1]:
#             return down_x
#         up_x += 1
#         down_x -= 1
#
# print(f(5687))

# 17.Գրել ֆունկցիա որը որպես արգումենտ կստանա թիվ և կվերադարձնի իր
# առաջին և վերջին թվանշանների արտադրյալը։
#
# def f(x):
#     lst = []
#     while x != 0:
#         a = x % 10
#         lst.append(a)
#         x = x // 10
#     return lst[0] * lst[-1]
#
# print(f(505))

# 18.Գրել ֆունկցիա որը որպես արգումենտ կստանա լիստ և կվերադարձնի
# լիստում եղած տողերի քանակությունը։
#
# def f(lst):
#     count = 0
#     for x in lst:
#         if type(x) == str:
#             count += 1
#     return count
#
# print(f([1, 3, 45, 'asd', 6, 'd']))

# 19․Գրել ֆունկցիա որը որպես արգումենտ կստանա լիստ և կվերադարձնի
# լիստում առկա թվերից առավելագույնը։
#
# def f(lst):
#     maximum = 0
#     for x in lst:
#         if type(x) == int and x > maximum:
#             maximum = x
#     return maximum
#
# print(f([1, 3, 'afaf', (1, 2, 3,)]))

# 20․Գրել ֆունկցիա որը որպես արգումենտ կստանա լիստ և կվերադարձնի
# այդ լիստում առկա երկնիշ զույգ թվերը։
#
# def f(lst):
#     maximum = 0
#     for x in lst:
#         if 0 < x // 10 < 10  and x > maximum:
#             maximum = x
#     return maximum
#
# print(f([1, 2, 38, 94, 130, 86, 984]))

# 21.Գրել ֆունկցիա որը որպես արգումենտ կստանա լիստ և կվերադարձնի
# այդ լիստում առկա թվերի միջին թվաբանականը։
#
# def f(lst):
#     max_1 = 0
#     max_2 = 0
#     for x in lst:
#         if x > max_1:
#             max_2 = max_1
#             max_1 = x
#     return (max_1 + max_2) / 2
#
# print(f([1, 2, 3, 4, 5, 10]))

# 22.Գրել ֆունկցիա որը որպես առգումենտ կստանա տողերի լիստ և
# կվերադարձնի այդ տողերի երկարությունները պարունակող լիստ։
#
# def f(lst):
#     mylst = []
#     for x in lst:
#         mylst.append(len(x))
#     return mylst
#
# print(f(['Process', 'finished', 'with', 'exit', 'code', '0']))

# 23.Գրել ֆունկցիա որը որպես արգումենտ կստանա լիստ և կվերադարձնի
# լիստում առկա թվերը դասավորված նվազման կարգով։
#
# def f(lst):
#     for i in range(len(lst)):
#         for j in range(len(lst) - 1):
#             if lst[j] < lst[j+1]:
#                 lst[j], lst[j+1] = lst[j+1], lst[j]
#     return lst
#
# print(f([5, 3, 8, 10, 94, 74, 38]))

# 24.Գրել ֆունկցիա որը որպես արգումենտ կստանա լիստ և կվերադարձնի
# լիստում առկա տողերը դասավորված երկարությունների նվազման կարգով։
#
# def f(lst):
#     for i in range(len(lst)):
#         for j in range(len(lst) - 1):
#             if len(lst[j]) < len(lst[j+1]):
#                 lst[j], lst[j+1] = lst[j+1], lst[j]
#     return lst
#
# print(f(['Process', 'finished', 'with', 'exit', 'code', '0', 'hello', 'world']))

# 25.Գրել ֆունկցիա որը որպես արգումենտ կընդունի տողերի լիստ
# և կվերադարձնի այն բառը որը կպարունակի ամենաշատ ձայնավորները։
#
# def f(lst):
#     a_A_lst = ['A', 'a', 'E', 'e', 'I', 'i', 'U', 'u', 'Y', 'y', 'O', 'o']
#     count = 0
#     word = lst[0]
#     for i in range(len(lst)):
#         cnt = 0
#         for x in lst[i]:
#             if x in a_A_lst:
#                 cnt += 1
#         if cnt > count:
#             word = lst[i]
#             count = cnt
#     return word
#
# print(f(['Process', 'finished', 'with', 'exit', 'code', '0', 'hello', 'world']))

# 26.Գրել ֆունկցիա որը որպես արգումենտ կընդունի նախադասությունների
# լիստ և կվերադարձնի այն նախադասությունը որը կպարունակի , ամենաշատ բառերը։
#
# def f(lst):
#     count = 0
#     el = ''
#     for i in range(len(lst)):
#         my_list = lst[i].split()
#         if len(my_list) > count:
#             el = ' '.join(my_list)
#             count = len(my_list)
#     return el
#
# print(f(['hello', 'hello world', 'what is your name', 'asd']))

# 27․Գրել ֆունկցիա որը որպես արգումենտ կստանա տող իրականում
# նախադասություն և կվերադարձնի այդ նախադասությունում առկա ամենամեծ թիվը ոչ թե թվանշանը։

# def f(mstr):
#     lst = mstr.split()
#     my_list = []
#     for x in lst:
#         if x.isdecimal():
#             my_list.append(int(x))
#     return max(my_list)
#
# print(f('Process 5 finished 15 with 65 exit code 0'))

# 28.Գրել ֆունկցիա որը որպես արգումենտ կստանա բառարանների լիստ՝
# մարդկանց նկարագրող և կվերադարձնի այն բառարանը որում մարդու տարիքն ամենամեծն է։
#
#
# def f(lst):
#     max = 0
#     d = dict()
#     for x in lst:
#         for k, v in x.items():
#             if v > max:
#                 max = v
#                 d = x
#     return d
#
# print(f([{'Ovak': 31}, {'Karen': 32}, {'Arsen': 25}, {'Karapet': 66}]))

# 29․Գրել ֆունկցիա որը որպես արգումենտ կստանա բառարանների լիստ՝
# ուսանողների նկարագրող և կվերադարձնի այդ ուսանողների լիստը դասավորված աճման կարգով՝ ըստ միասվորների։
#
# def f(lst):
#     my_lst = []
#     for x in lst:
#         for k, v in x.items():
#             my_lst.append((k, v))
#     return sorted(my_lst, key = lambda x: x[-1])
#
# print(f([{'Ovak': 31}, {'Karen': 32}, {'Arsen': 25}, {'Karapet': 66}]))
#

# 30.Գրել ֆունկցիա որը որպես արգումենտ կստանա բառարանների լիստ՝
# համալսարանների նկարագրող և կվերադարձնի այն համալսարանը որի , անվանումն ամենաերկարն է։
#
# lst = [{"a": 21}, {'ab': 22}, {'abc': 23}, {'abcd': 24}, {'abcde': 25}]
#
# def f(lst):
#     my_list = []
#     for x in lst:
#         for k, v in x.items():
#             my_list.append((k, v))
#     return sorted(my_list, key = lambda x : len(x[0]))[-1]
#
# print(f([{"a": 21}, {'ab': 22}, {'abc': 23}, {'abcd': 24}, {'abcde': 25}]))