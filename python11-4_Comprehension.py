Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Comprehension
>>> num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> num
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> for number in num:
	if number % 2 == 1:
		print(number)

		
1
3
5
7
9
>>> odd_numbers = [number for number in num in number % 2 == 1]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    odd_numbers = [number for number in num in number % 2 == 1]
TypeError: argument of type 'int' is not iterable
>>> odd_numbers = [number for number if num in number % 2 == 1]
SyntaxError: invalid syntax
>>> odd_numbers = [number for number in num if number % 2 == 1]
>>> odd_numbers
[1, 3, 5, 7, 9]
>>> 
