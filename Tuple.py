Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> tu = (5,62,3,41,45,41)
>>> max(tu)
62
>>> min(tu)
3
>>> sum(tu)
197
>>> tu.index(62)
1
>>> tu.count(41)
2
>>> tu = list(tu)
>>> type(tu)
<class 'list'>
>>> tu[0]
5
>>> tu[0] = 100
>>> tu
[100, 62, 3, 41, 45, 41]
tu = tuple(tu)
tu
(100, 62, 3, 41, 45, 41)
