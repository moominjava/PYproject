Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # 함수 여러 개 돌려 받기
>>> def add_mul(num1, num2):
	return num1 + num2, num1 * num2

>>> my_add, my_mul = add_mul(3, 5)
>>> 
>>> 1
1
>>> add_mul
<function add_mul at 0x00000261DEF6C268>
>>> my_
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    my_
NameError: name 'my_' is not defined
>>> my_add
8
>>> my_mul
15
>>> 
