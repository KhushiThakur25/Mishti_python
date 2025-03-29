Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
============= RESTART: E:/Mishti_python/ArmstrongNumber.py =============
Enter the value for n..153
Your number is an Armstrong..
>>> print("* * * * *")
* * * * *
>>> for i in range(5):
...     print("*",end = " ")
... 
* * * * * 
>>> for i in range(10):
...     print("*",end = " ")
... 
* * * * * * * * * * 
>>> for j in range(5):
...     for i in range(5):
...         print("*",end = " ")
... 
* * * * * * * * * * * * * * * * * * * * * * * * * 
for j in range(5):
    for i in range(5):
        print("*",end = " ")
    print()

* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * * 
for j in range(5):
    for i in range(5):
        print(j,i,end = " ")
    print()

0 0 0 1 0 2 0 3 0 4 
1 0 1 1 1 2 1 3 1 4 
2 0 2 1 2 2 2 3 2 4 
3 0 3 1 3 2 3 3 3 4 
4 0 4 1 4 2 4 3 4 4 
for j in range(5):
    for i in range(5):
        print(f"{j,i}",end = " ")
    print()

(0, 0) (0, 1) (0, 2) (0, 3) (0, 4) 
(1, 0) (1, 1) (1, 2) (1, 3) (1, 4) 
(2, 0) (2, 1) (2, 2) (2, 3) (2, 4) 
(3, 0) (3, 1) (3, 2) (3, 3) (3, 4) 
(4, 0) (4, 1) (4, 2) (4, 3) (4, 4) 
for i in range(5):
    for j in range(i+1):
        print("*",end = " ")
    print()

* 
* * 
* * * 
* * * * 
* * * * * 
for i in range(5):
    for j in range(i+1):
        if (i+j)%2 == 0:
            print("1",end = " ")
        else:
            print("0",end= " " )
    print()

1 
0 1 
1 0 1 
0 1 0 1 
1 0 1 0 1 
