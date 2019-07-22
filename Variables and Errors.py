Python 3.6.8 (default, Jan 14 2019, 11:02:34) 
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = 5
>>> b = 10
>>> a = b
>>> b = a
>>> a
10
>>> b
10
>>> a = 5
>>> b = 10
>>> a = b
>>> a
10
>>> b
10
>>> a = 5
>>> c = a
>>> a = b
>>> b = c
>>> a
10
>>> b
5
>>> four = '4'
>>> print(four*3)
444
>>> five = 4
>>> print950
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    print950
NameError: name 'print950' is not defined
>>> print(5)
5
>>> print(five*3)
12
>>> my_name = 'student'
>>> print('my name is '+my_name)
my name is student
>>> print('Hi' + my_name)
Histudent
>>> my_age = 15
>>> print('I am ' + my_age + ' years old')
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    print('I am ' + my_age + ' years old')
TypeError: must be str, not int
>>> my_age = str(my_age)
>>> my_age
'15'
>>> print('i am ' + my_age + ' years old')
i am 15 years old
>>> score = 4
>>> count = 5
>>> total = score*count
>>> print(total)
20
>>> num_people = 20
>>> num_places = 30
>>> num_food = 25
>>> num_food = 25+ num_places/num_people
>>> print(num_food)
26.5
>>> print('have a niceeeeee day)
	  
SyntaxError: EOL while scanning string literal
>>> print('have a niceeeeeeeeee day')
	  
have a niceeeeeeeeee day
>>> print('good for you")
	  
SyntaxError: EOL while scanning string literal
>>> print("good for you")
	  
good for you
>>> myName = "hallel"
	  
>>> familyName = "appelbaum-elad"
	  
>>> print(myName + familyName)
	  
hallelappelbaum-elad
>>> hi you
	  
SyntaxError: invalid syntax
>>> 
