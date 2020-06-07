Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # for 변수 in 컨테이너:
>>> num = ['three', 'one', 'two', 'four', 'five', 'six']
>>> num
['three', 'one', 'two', 'four', 'five', 'six']
>>> for number in num:
	print(number)

	
three
one
two
four
five
six
>>> for name in 'PYTHONHAPPY':
	print(name)

	
P
Y
T
H
O
N
H
A
P
P
Y
>>> # 보통 띄어쓰기 4칸을 권장합니다.
>>> # range()
>>> for n in range(4):
	print(n)

	
0
1
2
3
>>> for n in range(3, 9):
	print(n)

	
3
4
5
6
7
8
>>> 
>>> # for X 2
>>> for i in range(2, 10):
	for j in range(1, 10):
		print('{} X {} = {}'.format(j, i, j*i)


		      )

		
1 X 2 = 2
2 X 2 = 4
3 X 2 = 6
4 X 2 = 8
5 X 2 = 10
6 X 2 = 12
7 X 2 = 14
8 X 2 = 16
9 X 2 = 18
1 X 3 = 3
2 X 3 = 6
3 X 3 = 9
4 X 3 = 12
5 X 3 = 15
6 X 3 = 18
7 X 3 = 21
8 X 3 = 24
9 X 3 = 27
1 X 4 = 4
2 X 4 = 8
3 X 4 = 12
4 X 4 = 16
5 X 4 = 20
6 X 4 = 24
7 X 4 = 28
8 X 4 = 32
9 X 4 = 36
1 X 5 = 5
2 X 5 = 10
3 X 5 = 15
4 X 5 = 20
5 X 5 = 25
6 X 5 = 30
7 X 5 = 35
8 X 5 = 40
9 X 5 = 45
1 X 6 = 6
2 X 6 = 12
3 X 6 = 18
4 X 6 = 24
5 X 6 = 30
6 X 6 = 36
7 X 6 = 42
8 X 6 = 48
9 X 6 = 54
1 X 7 = 7
2 X 7 = 14
3 X 7 = 21
4 X 7 = 28
5 X 7 = 35
6 X 7 = 42
7 X 7 = 49
8 X 7 = 56
9 X 7 = 63
1 X 8 = 8
2 X 8 = 16
3 X 8 = 24
4 X 8 = 32
5 X 8 = 40
6 X 8 = 48
7 X 8 = 56
8 X 8 = 64
9 X 8 = 72
1 X 9 = 9
2 X 9 = 18
3 X 9 = 27
4 X 9 = 36
5 X 9 = 45
6 X 9 = 54
7 X 9 = 63
8 X 9 = 72
9 X 9 = 81
>>> 
