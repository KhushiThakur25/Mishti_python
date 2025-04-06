Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> li = [1,2,3,5,6,47,8,9,6,4]
>>> type(li)
<class 'list'>
>>> li[0]
1
>>> li[0] = 100
>>> li
[100, 2, 3, 5, 6, 47, 8, 9, 6, 4]
>>> s = ["12","om",True,56,23.2]
>>> type(s)
<class 'list'>
>>> s[::-1]
[23.2, 56, True, 'om', '12']
>>> li
[100, 2, 3, 5, 6, 47, 8, 9, 6, 4]
>>> li.append(56)
>>> li
[100, 2, 3, 5, 6, 47, 8, 9, 6, 4, 56]
li.remove(2)
li
[100, 3, 5, 6, 47, 8, 9, 6, 4, 56]
li.pop()
56
li
[100, 3, 5, 6, 47, 8, 9, 6, 4]
li.remove(6)
li.remove(3)
li
[100, 5, 47, 8, 9, 6, 4]
li.insert(1,4)
li
[100, 4, 5, 47, 8, 9, 6, 4]
li.append(23,56)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    li.append(23,56)
TypeError: list.append() takes exactly one argument (2 given)
li.append([23,56])
li
[100, 4, 5, 47, 8, 9, 6, 4, [23, 56]]
li.extend([23,56])
li
[100, 4, 5, 47, 8, 9, 6, 4, [23, 56], 23, 56]
li.remove([23, 56])
li
[100, 4, 5, 47, 8, 9, 6, 4, 23, 56]
sum(li)
262
max(li)
100
min(li)
4
li.count(4)
2
len(li)
10
for i in li:
    print(i)

100
4
5
47
8
9
6
4
23
56
s
['12', 'om', True, 56, 23.2]
s.clear()
s
[]
li.reverse()
li
[56, 23, 4, 6, 9, 8, 47, 5, 4, 100]
li.sort()
li
[4, 4, 5, 6, 8, 9, 23, 47, 56, 100]
li.sort(reverse = True)
li
[100, 56, 47, 23, 9, 8, 6, 5, 4, 4]
li
[100, 56, 47, 23, 9, 8, 6, 5, 4, 4]
m = li
m
[100, 56, 47, 23, 9, 8, 6, 5, 4, 4]
m[0]
100
m[0] = 200
m
[200, 56, 47, 23, 9, 8, 6, 5, 4, 4]
li
[200, 56, 47, 23, 9, 8, 6, 5, 4, 4]
k = li.copy()
k
[200, 56, 47, 23, 9, 8, 6, 5, 4, 4]
li
[200, 56, 47, 23, 9, 8, 6, 5, 4, 4]
k[0] = 300
k
[300, 56, 47, 23, 9, 8, 6, 5, 4, 4]
li
[200, 56, 47, 23, 9, 8, 6, 5, 4, 4]
li[0] = 100
li
[100, 56, 47, 23, 9, 8, 6, 5, 4, 4]
