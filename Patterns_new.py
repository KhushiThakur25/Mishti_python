Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> n = 5
>>> for i in range(n):
...     for j in range(n):
...         if(i == 0 or i == n-1 or j == 0 or j == n-1):
...             print("*",end = " ")
...         else:
...             print(" ",end = " ")
...     print()
... 
* * * * * 
*       * 
*       * 
*       * 
* * * * * 
>>> for i in range(n):
...     for j in range(n,0,-1):
...         print(j,end = " ")
...     print()

5 4 3 2 1 
5 4 3 2 1 
5 4 3 2 1 
5 4 3 2 1 
5 4 3 2 1 
for i in range(n):
    for j in range(n-i,0,-1):
        print(j,end = " ")
    print()

5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1 
m = 1
for i in range(5):
    for j in range(i+1):
        print(m,end = " ")
        m += 1
    print()

1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15 
i,j = 0
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    i,j = 0
TypeError: cannot unpack non-iterable int object
n = 5
for i in range(5):
    for j in range(0,n-1-i):
        print(" ",end = " ")
    for j in range(n-1-i,n):
        print("*",end = " ")
    print()

        * 
      * * 
    * * * 
  * * * * 
* * * * * 
for i in range(5):
    for j in range(0,i):
        print(" ",end = " ")
    for j in range(i,n):
        print("*",end = " ")
    print()

* * * * * 
  * * * * 
    * * * 
      * * 
        * 
