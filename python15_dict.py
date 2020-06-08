Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #dict
>>> students = { 'stu1': 'tom', 'stu2': 'sally', 'stu3': 'betty'}
>>> students
{'stu1': 'tom', 'stu2': 'sally', 'stu3': 'betty'}
>>> for student in students.values():
	print(students)

	
{'stu1': 'tom', 'stu2': 'sally', 'stu3': 'betty'}
{'stu1': 'tom', 'stu2': 'sally', 'stu3': 'betty'}
{'stu1': 'tom', 'stu2': 'sally', 'stu3': 'betty'}
>>> students = {'학생1': 'Tom', '학생2': 'Sally', '학생3': 'Betty'}
>>> for stu in students.values():
	print(stu)

	
Tom
Sally
Betty
>>> students
{'학생1': 'Tom', '학생2': 'Sally', '학생3': 'Betty'}
>>> 
>>> for key in students.keys():
	print(key)

	
학생1
학생2
학생3
>>> 
>>> for key, val in students.items():
	print(key, val)

	
학생1 Tom
학생2 Sally
학생3 Betty
>>> 
