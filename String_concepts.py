Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
st = 's'
sts = "s"
type(st)
<class 'str'>
type(sts)
<class 'str'>
n = 56
type(n)
<class 'int'>
m = 2.3
type(m)
<class 'float'>
st = "This is my python class"
st[0]
'T'
st[1]
'h'
st[4]
' '
st[0] = 'd'
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    st[0] = 'd'
TypeError: 'str' object does not support item assignment
del st[0]
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    del st[0]
TypeError: 'str' object doesn't support item deletion
st
'This is my python class'
st.lower()
'this is my python class'
>>> st
'This is my python class'
>>> st.upper()
'THIS IS MY PYTHON CLASS'
>>> st.title()
'This Is My Python Class'
>>> st.swapcase()
'tHIS IS MY PYTHON CLASS'
>>> st.capitalize()
'This is my python class'
>>> st.islower()
False
>>> st.isupper()
False
>>> st.istitle()
False
>>> st.isalpha()
False
>>> t = "apple"
>>> t.isalpha()
True
s = "12345"
s.isdigit()
True
s.isnumeric()
True
s = "app123"
s.isdigit()
False
s = "  This is my book     "
s.strip()
'This is my book'
s.lstrip()
'This is my book     '
s.rstrip()
'  This is my book'
"hello" == "Hello"
False
"hello".casefold() == "Hello".casefold()
True
s
'  This is my book     '
s.index('s')
5
s.rindex('s')
8
s.index('z')
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    s.index('z')
ValueError: substring not found
s.find('z')
-1
s.find('s')
5
s.count("s")
2
s.count("s",5)
2
s.count("s",6)
1
s.partition("my")
('  This is ', 'my', ' book     ')
st.split()
['This', 'is', 'my', 'python', 'class']
s = "this,is,my,book"
s.split(",")
['this', 'is', 'my', 'book']
s.replace(","," ")
'this is my book'
s.replace(","," ",3)
'this is my book'
s.replace(","," ",1)
'this is,my,book'
st = st.split()
type(st)
<class 'list'>
st
['This', 'is', 'my', 'python', 'class']
" ".join(st)
'This is my python class'
st = " ".join(st)
st
'This is my python class'
