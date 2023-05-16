# STRING#########################################################################################################
##################################################################################################################

# 1. Write a Python program to calculate the length of a string.
#
# string = 'abc'
#
# print(len(string))

# 2. Write a Python program to count the number of characters (character frequency) in a string.
#
# string = 'hello'
#
# d = dict()
#
# for x in string:
#     if x in d:
#         d[x] += 1
#     else:
#         d[x] = 1
# print(d)

# 3. Write a Python program to get a string made of the first 2 and last 2 characters of a given string.
# If the string length is less than 2, return the empty string instead.
#
# string = 'Hello'
#
# answer = ''
#
# if len(string) < 2:
#     print(answer)
# else:
#     answer = string[:2] + string[-2:]
#     print(answer)

# 4. Write a Python program to get a string from a given string where all occurrences of its first char
# have been changed to '$', except the first char itself.
#
# string = 'ararat'
#
# answer = string[0]
#
# for x in string[1:]:
#     if x == string[0]:
#         answer += '$'
#     else:
#         answer += x
# print(answer)

# 5. Write a Python program to get a single string from two given strings,
# separated by a space and swap the first two characters of each string.
#
# string1 = 'hello'
# string2 = 'world'
#
# answer = string2[:2] + string1[2:] + ' ' + string1[:2] + string2[2:]
#
# print(answer)

# 6. Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
# If the given string already ends with 'ing', add 'ly' instead.
# If the string length of the given string is less than 3, leave it unchanged.
#
# string = 'hello'
#
# if len(string) < 3:
#     print(string)
# elif len(string) >= 3 and string[-3:] != 'ing':
#     print(string + 'ing')
# else:
#     print(string + 'ly')

# 7. Write a Python program to find the first appearance of the substrings 'not' and 'poor' in a given string.
# If 'not' follows 'poor', replace the whole 'not'...'poor' substring with 'good'.
# Return the resulting string.
#
# string = "The lyrics is not that poor!"
# a = string.find('not')
# b = string.find('poor')
#
# if b > a and a > 0 and b > 0:
#     string = string[:a] + 'good' + string[b + 4:]
#
# print(string)

# 8. Write a Python function that takes a list of words and return the longest word
# and the length of the longest one.
#
# def long_word(lst):
#     leng = 0
#     answer = ''
#     for x in lst:
#         if len(x) > leng:
#             leng = len(x)
#             answer = x
#     return answer, leng
#
# print(long_word(['hello', 'terraform', 'docker']))

# 9. Write a Python program to remove the nth index character from a nonempty string.
#
# def remove(mstr, index):
#     mstr = mstr[:index] + mstr[index + 1:]
#     return mstr
#
# print(remove('hello', 1))

# 10. Write a Python program to change a given string to a newly string
# where the first and last chars have been exchanged.
#
# def exchange(mstr):
#     newstr = mstr[-1] + mstr[1:-1] + mstr[0]
#     return newstr
#
# print(exchange('hello'))

# 11. Write a Python program to remove characters that have odd index values in a given string.
#
# def odd_remove(mstr):
#     answer = mstr[::2]
#     return answer
#
# print(odd_remove('python'))

# 12. Write a Python program to count the occurrences of each word in a given sentence.
#
# def occur(mstr):
#     d = dict()
#     lst = mstr.split()
#     for x in lst:
#         if x in d:
#             d[x] +=1
#         else:
#             d[x] = 1
#     return d
#
# print(occur('one two three five five'))

# 13. 44. Write a Python program to print the index of a character in a string.
#
# def char_index(mstr):
#     for i in range(len(mstr)):
#         print(f"Current character {mstr[i]} position - {i}")
#     return mstr
#
# print(char_index('hello'))

# 14. 90. Write a Python program to remove duplicate words from a given string.
#
# def rem_dup(mstr):
#     lst1 = mstr.split()
#     lst2 = []
#     for x in lst1:
#         if x not in lst2:
#             lst2.append(x)
#     return ' '.join(lst2)
#
# print(rem_dup('Python Exercises Practice Solution Exercises'))

# 15. 34. Write a Python program to print the following integers with '*' to the right of the specified width.
#
# def integer(mstr, char):
#     answer = ''
#     for i in range(len(mstr)):
#         if mstr[i] == char:
#             answer += mstr[i] + '*'
#         else:
#             answer += mstr[i]
#     return answer
#
# print(integer('hello', 'l'))

# LIST###########################################################################################################
################################################################################################################

# 1. 10. Write a Python program to find the list of words that are longer than n from a given list of words.
#
# def longer(lst, n):
#     longer_words = []
#     for x in lst:
#         if len(x) > n:
#             longer_words.append(x)
#     return longer_words
#
# print(longer(['Hello', 'from', 'my', 'python', 'function'], 3))

# 2. 27. Write a Python program to find the second smallest number in a list.
#
# ls = [6, 3, 8, 1, 9, 134, 87, 23]
# ls.sort()
# print(ls[1])

# 3. 52. Write a Python program to compute the difference between two lists.
#
# def difference(lst1, lst2):
#     dif_lst = []
#     for x in lst1:
#         if x not in lst2:
#             dif_lst.append(x)
#     return dif_lst
#
# print(difference([1, 2, 3, 5, 'asd'], [6, 7, 3, 'asd']))

# 4. 57. Write a Python program to check if all items in a given list of strings are equal to a given string.
#
# def equal(lst, mstr):
#     flag = False
#     for x in lst:
#         if x == mstr:
#             flag = True
#     return flag
#
# print(equal(['asd', 'tre', 'hgf', 'vbn'], 'vb'))

# 5. 63. Write a Python program to insert a given string at the beginning of all items in a list.

# def insert(lst, mstr):
#     lst1 = []
#     for el in lst:
#         x = str(el) + mstr
#         lst1.append(x)
#     return lst1
#
# print(insert([1, 2, 3, 4, 5], 'str'))

# 6. 65. Write a Python program to move all zero digits to the end of a given list of numbers.
#
# def zero(lst):
#     a = lst.count(0)
#     lst1 = []
#     for x in lst:
#         if x != 0:
#             lst1.append(x)
#     lst1.extend([0]*a)
#     return lst1
#
# print(zero([1, 2, 3,4,5,6,0,0,0,3,4,5,6,7,8,0,2,3,4,0]))

# 7. 70. Write a Python program to find items starting with a specific character from a list.
#
# def find(lst, char):
#     lst1 = []
#     for x in lst:
#         if x[:len(char)] == char:
#             lst1.append(x)
#     return lst1
#
# print(find(['qwe', 'dfg', 'asd', 'mnb', 'asdf'], 'as'))

# 8. 66. Write a Python program to find the list in a list of lists whose sum of elements is the highest.
#
# def hi_sum(lst):
#     max = 0
#     answer = None
#     for x in lst:
#         if sum(x) > max:
#             max = sum(x)
#             answer = x
#     return answer, max
#
# print(hi_sum([[1,2,3], [4,5,6], [10,11,12], [7,8,9]]))

# 9. 35. Write a Python program to create a list by concatenating a given list with a range from 1 to n.
#
# def conc(lst, n):
#     lst1 = []
#     for el in lst:
#         for i in range(1, n+1):
#             lst1.append(str(el) + str(i))
#     return lst1
#
# print(conc(['p', 'q'], 5))

# 10. 29. Write a Python program to get unique values from a list.
#
# def unique(lst):
#     lst1 = []
#     for x in lst:
#         if x not in lst1:
#             lst1.append(x)
#     return lst1

# DICT#############################################################################################################
##################################################################################################################

# 1. 3. Write a Python script to concatenate the following dictionaries to create a new one.
# d = dict()
# def upd(*args):
#     for x in args:
#         d.update(x)
#     return d
#
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
#
# print(upd(dic1, dic2, dic3))


# 2. 7. Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included)
# and the values are the square of the keys
# d = dict()
# def upd(n):
#     for x in range(n+1):
#         d[x] = x**2
#     return d
#
# print(upd(15))

# 3 13. Write a Python program to map two lists into a dictionary.
# d = dict()
# def map(lst1, lst2):
#     d = dict(zip(lst1, lst2))
#     return d
#
# print(map([1, 2, 3], ['a', 'b', 'c']))

# 4. 24. Write a Python program to create a dictionary from a string.
#
# d = dict()
# def dict_from_string(mstr):
#     for i in range(len(mstr)):
#         d[mstr[i]] = i
#     return d
#
# print(dict_from_string('hello'))

# 5. 34. Write a Python program to count the number of items in a dictionary value that is a list.
#
# def cnt(d):
#     count = 0
#     for k in d:
#         if type(d[k]) == list:
#             count += 1
#     return count
#
# print(cnt({'x': [11, 12, 13, 14, 15, 16, 17, 18, 19],
# 'y': [21, 22, 23, 24, 25, 26, 27, 28, 29],
# 'z': [31, 32, 33, 34, 35, 36, 37, 38, 39], 'a': 1}))

# 6. 45. Write a Python program to verify that all values in a dictionary are the same.
#
# def same(d):
#     x = d['a']
#     answer = True
#     for k in d:
#         if d[k] != x:
#             answer = False
#     return answer
#
# print(same({'a':12, 'c':12, 'b': 12}))

# 7.
