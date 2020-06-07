Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #list
>>> # 값들은 변경할 수 있고 순서가 있습니다.
>>> #가변(mutable) : 값을 변경할 수 있습니다. 리스트, 딕셔너리 등이 해당됩니다.
>>> # 불변(immutable) : 값을 변경할 수 없습니다. 문자열, 튜플 등이 해당됩니다.
>>> my_list = []
>>> type(my_list)
<class 'list'>
>>> my_list = [1, 3, 5, 7, 9]
>>> print(my_list)
[1, 3, 5, 7, 9]

>>> # .append
>>> my_list.append('betty')
>>> my_list
[1, 3, 5, 7, 9, 'betty']
>>> my_list.append('Python')
>>> my_list
[1, 3, 5, 7, 9, 'betty', 'Python']
>>> 
>>> my_list[2]
5
>>> my_list[5]
'betty'
>>> my_list.append('apple')
>>> my_list
[1, 3, 5, 7, 9, 'betty', 'Python', 'apple']
>>> my_list.sort()
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    my_list.sort()
TypeError: '<' not supported between instances of 'str' and 'int'
>>> my_list2 = ['banana', 'apple', 'pain', 'phone', 'computer')
SyntaxError: invalid syntax
>>> my_list2 = ['banana', 'apple', 'pain', 'phone', 'computer']
>>> my_list2
['banana', 'apple', 'pain', 'phone', 'computer']
>>> my_list2.sort()
>>> my_list2
['apple', 'banana', 'computer', 'pain', 'phone']
>>> 
