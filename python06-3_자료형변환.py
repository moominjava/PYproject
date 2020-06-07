Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #자료형 변환하기
>>> int(3.14)
3
>>> tyle(int(3,14))
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    tyle(int(3,14))
NameError: name 'tyle' is not defined
>>> type(int(3.14))
<class 'int'>
>>> float(4)
4.0
>>> type(float(6))
<class 'float'>
>>> list('3.14,a')
['3', '.', '1', '4', ',', 'a']
>>> type(list(3.14,a))
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    type(list(3.14,a))
NameError: name 'a' is not defined
>>> type(list('3.14,a'))
<class 'list'>
>>> 
