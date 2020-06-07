Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #포매팅
>>> # % 연산자를 이용해 문자열에 숫자, 문자열 등을 대입합니다.
>>> # %d : 정수형 숫자를 대입할 수 있습니다.
>>> # %f : 실수형 숫자를 대입할 수 있습니다.
>>> # %s : 문자열을 대입할 수 있습니다.
>>> print('my name is $s' $ 'magi')
SyntaxError: invalid syntax
>>> print('my name is %s' % 'magi')
my name is magi
>>> print('a = %d, b = %d' %(2,4))
a = 2, b = 4
>>> print('%d X %d = %d' % (2, 3, 2*3))
2 X 3 = 6
>>> print('%f' % 3.25)
3.250000
>>> print('$s' % 'Pythone')
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    print('$s' % 'Pythone')
TypeError: not all arguments converted during string formatting
>>> print('%s' % 'Pythone')
Pythone
>>> 
