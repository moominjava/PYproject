Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #modual
>>> import random
>>> stu = [ 'Tom', 'Amy', 'Sally', 'Eric']
>>> print(random.choice(sty))
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print(random.choice(sty))
NameError: name 'sty' is not defined
>>> print(random.choice(stu))
Tom
>>> print(random.choice(stu))
Amy
>>> print(random.sample(stu, 2))
['Eric', 'Sally']
>>> print(random.randint(1, 20))
11
>>> print(random.randint(1, 20))
10
>>> print(random.randint(1, 20))
8
>>> print(random.randint(1, 20))
1
>>> print(random.randint(1, 20))
15
>>> print(random.randint(1, 20))
15
>>> my_int = random.randint(1, 45)
>>> print(random.sample(my_int, 6))
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    print(random.sample(my_int, 6))
  File "C:\Users\moomi\AppData\Local\Programs\Python\Python37\lib\random.py", line 317, in sample
    raise TypeError("Population must be a sequence or set.  For dicts, use list(d).")
TypeError: Population must be a sequence or set.  For dicts, use list(d).
>>> print(my_int)
33
>>> list = []
>>> list.append(random.sample(my_int, 6))
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    list.append(random.sample(my_int, 6))
  File "C:\Users\moomi\AppData\Local\Programs\Python\Python37\lib\random.py", line 317, in sample
    raise TypeError("Population must be a sequence or set.  For dicts, use list(d).")
TypeError: Population must be a sequence or set.  For dicts, use list(d).
>>> 
