Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> my_list=[]
>>> my_list.append(123)
>>> print(my_list)
[123]
>>> my_list.append('abc', Ttue)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    my_list.append('abc', Ttue)
NameError: name 'Ttue' is not defined
>>> my_list.append('abc', 456)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    my_list.append('abc', 456)
TypeError: append() takes exactly one argument (2 given)
>>> my_list.append('abc')
>>> my_list
[123, 'abc']
>>> my_typle=()
>>> my_tuple1 = (1, 2, 4)
>>> my_tuple1
(1, 2, 4)
>>> my_tuple1 = 3.24, 'apple', true
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    my_tuple1 = 3.24, 'apple', true
NameError: name 'true' is not defined
>>> my_tuple2 = 3.14, 'Pythone', True
>>> my_tuple2
(3.14, 'Pythone', True)
>>> my_dict = {}
>>> my_dict[1] = 'a'
>>> my_dict[1]
'a'
>>> my_['d'] = 1234
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    my_['d'] = 1234
NameError: name 'my_' is not defined
>>> my_dict['d'] = 1234
>>> print(my_dict)
{1: 'a', 'd': 1234}
>>> #리스트 (List) list = []
>>> #튜플 (Tuple) tuple = ()
>>> #딕셔너리 (Dictionary) dic[1] = 'a'
>>> 
