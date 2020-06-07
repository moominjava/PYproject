Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #인덱싱 문자열 위치접근
>>> index = 'abcde'
>>> index
'abcde'
>>> index[2]
'c'
>>> index[5]
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    index[5]
IndexError: string index out of range
>>> index[4]
'e'
>>> name = 'あなたの名前'
>>> name
'あなたの名前'
>>> name[3]
'の'
>>> name[-2]
'名'
>>> name[-1]
'前'
>>> 
