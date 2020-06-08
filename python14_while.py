Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # while
>>> # while 조건:
>>> #    실행할 문장1
>>> #    실행할 문장2
>>> count = 0
>>> while count < 7:
	print('python : ', count)
	count+-=1
	
SyntaxError: invalid syntax
>>> 
>>> while count < 7:
	print('python : ', count)
	count +=1

	
python :  0
python :  1
python :  2
python :  3
python :  4
python :  5
python :  6
>>> 
>>> while count < 10:
	count +=1
	if count < 5:
		continue
	if count == 8:
		break

	
>>> 
================ RESTART: C:/Users/moomi/Desktop/whileTest.py ================
Traceback (most recent call last):
  File "C:/Users/moomi/Desktop/whileTest.py", line 1, in <module>
    while count < 10:
NameError: name 'count' is not defined
>>> count
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    count
NameError: name 'count' is not defined
>>> 
================ RESTART: C:/Users/moomi/Desktop/whileTest.py ================
>>> count
8
>>> 
