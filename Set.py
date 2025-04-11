Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> st = {}
>>> type(st)
<class 'dict'>
>>> st = {1,2,3}
>>> dic = {"name":"om","roll-no":6}
>>> m = {\}
...     
SyntaxError: unexpected character after line continuation character
>>> st = set()
>>> st
set()
>>> type(st)
<class 'set'>
>>> st = {1,2,3,4,5,6}
>>> s = {4,5,6,7,8,9}
>>> st.union(s)
{1, 2, 3, 4, 5, 6, 7, 8, 9}
>>> st.intersection(s)
{4, 5, 6}
st.difference(s)
{1, 2, 3}
st.symmetric(s)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    st.symmetric(s)
AttributeError: 'set' object has no attribute 'symmetric'
st.symmetric_difference(s)
{1, 2, 3, 7, 8, 9}
st.issuperset(s)
False
st.issubset(s)
False
t = {1,2}
w = {5,6}
t.isdisjoint(w)
True
t.add("hello")
t
{1, 2, 'hello'}
w = {1,2,1,2,1,2,12,3}
w
{1, 2, 3, 12}
w.remove(12)
w
{1, 2, 3}
w.remove(56)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    w.remove(56)
KeyError: 56
w.discard(2)
w
{1, 3}
w.discard(56)
w.clear()
w
set()
del w
w
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    w
NameError: name 'w' is not defined
t.pop()
1
t[0]
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    t[0]
TypeError: 'set' object is not subscriptable
st.update(s)
st
{1, 2, 3, 4, 5, 6, 7, 8, 9}
st = {1,2,3,4,5,6}
s = {4,5,6,7,8,9}
st.union(s)
{1, 2, 3, 4, 5, 6, 7, 8, 9}
st
{1, 2, 3, 4, 5, 6}
dic = {"name":"Ram","roll-no":7,"marks":89}
dic
{'name': 'Ram', 'roll-no': 7, 'marks': 89}
dic["div"] = 1
dic
{'name': 'Ram', 'roll-no': 7, 'marks': 89, 'div': 1}
dic["name"]
'Ram'
dic.keys()
dict_keys(['name', 'roll-no', 'marks', 'div'])
dic.values()
dict_values(['Ram', 7, 89, 1])
dic.items()
dict_items([('name', 'Ram'), ('roll-no', 7), ('marks', 89), ('div', 1)])
dic.get("name")
'Ram'
dic.popitem()
('div', 1)
dic
{'name': 'Ram', 'roll-no': 7, 'marks': 89}
dic.remove("roll-no")
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    dic.remove("roll-no")
AttributeError: 'dict' object has no attribute 'remove'
dic.pop('roll-no')
7
dic
{'name': 'Ram', 'marks': 89}
di = {"roll-no":96,'div':2}
dic.update(di)
dic
{'name': 'Ram', 'marks': 89, 'roll-no': 96, 'div': 2}
di = dic.copy()
di
{'name': 'Ram', 'marks': 89, 'roll-no': 96, 'div': 2}
di["name"] = "amit"
di
{'name': 'amit', 'marks': 89, 'roll-no': 96, 'div': 2}
dic
{'name': 'Ram', 'marks': 89, 'roll-no': 96, 'div': 2}
dic["seq"] = [1,2,3,45,6,8,9]
dic
{'name': 'Ram', 'marks': 89, 'roll-no': 96, 'div': 2, 'seq': [1, 2, 3, 45, 6, 8, 9]}
dic["seq"][0]
1
li = [{"name":"jay"}]
li[0]["name"]
'jay'
