Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # '{ }'.format()
>>> print('my name is %s' % ('tom'))
my name is tom
>>> print('my name is {}'.format('Tom'))
my name is Tom
>>> print('{} x {} = {}'.for(2, 3,, 2*3))
SyntaxError: invalid syntax
>>> print('{} x {} = {}'.format(2, 3, 2*3))
2 x 3 = 6
>>> print('{1} x {0} = {2}'.format(2, 3, 2*3))
3 x 2 = 6
>>> 
