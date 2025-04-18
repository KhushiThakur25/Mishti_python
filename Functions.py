Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print"hello"
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
def calc():
    print("Hello i'm calc")

calc()
Hello i'm calc
calc()
Hello i'm calc
def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact

factorial(5)
120
def calc(n,m):
    print(n,m)

calc(4)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    calc(4)
TypeError: calc() missing 1 required positional argument: 'm'
calc(4,5)
4 5
def calc(n=1,m=5):
    print(n,m)

calc(2)
2 5
def calc(n,m):
    print(n,m)

calc(x = 5,y = 6)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    calc(x = 5,y = 6)
TypeError: calc() got an unexpected keyword argument 'x'
calc(m = 3,n = 5)
5 3
def calc(*args):
    print(args)

calc(5,6,2,3,4)
(5, 6, 2, 3, 4)
def calc(**kwargs):
    print(kwargs)

calc(name = "ram",m = 56,n = 332)
{'name': 'ram', 'm': 56, 'n': 332}
def pattern(n):
    for i in range(n):
        for j in range(i+1):
            print("*",end = " ")
        print()

pattern(5)
* 
* * 
* * * 
* * * * 
* * * * * 
pattern(8)
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * * * 
* * * * * * * 
* * * * * * * * 
eval("56-41+74*23-/6")
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    eval("56-41+74*23-/6")
  File "<string>", line 1
    56-41+74*23-/6
                ^
SyntaxError: invalid syntax
eval("56-41+74*23-56/6")
1707.6666666666667
def convert(c):
    return 9/2*c + 32

li = [563,4125,1225,741,7412,655]
>>> f = []
>>> for i in li:
...     f.append(convert(i))
... 
>>> f
[2565.5, 18594.5, 5544.5, 3366.5, 33386.0, 2979.5]
>>> map(convert,li)
<map object at 0x000001D0ACCDA9B0>
>>> list(map(convert,li))
[2565.5, 18594.5, 5544.5, 3366.5, 33386.0, 2979.5]
>>> def even(n):
...     return n%2 == 0
... 
>>> def odd(n):
...     return n%3 != 0
... 
>>> list(filter(even,li))
[7412]
>>> list(filter(odd,li))
[563, 1225, 7412, 655]
