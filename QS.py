Python 3.13.0 (tags/v3.13.0:60403a5, Oct  7 2024, 09:38:07) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
st = "This is my book"
st = st.split()
st
['This', 'is', 'my', 'book']
st = st[::-1]
st
['book', 'my', 'is', 'This']
st = " ".join(st)
st
'book my is This'
st = "Brain,mentors.and.skill,risers."
st = st.replace(",","@")
st = st.replace(".",",")
st = st.replace("@",".")
st
'Brain.mentors,and,skill.risers,'
n = 4
for i in range(n):
    for j in range(n-i):
        print(" ",end = " ")
    for j in range(n-i,n):
        print("*",end = " ")
    print()

        
      * 
    * * 
  * * * 
for i in range(n):
    for j in range(n-i):
...         print(" ",end = " ")
...     for j in range(2*i+1):
...         print("*",end = " ")
...     print()
... 
        * 
      * * * 
    * * * * * 
  * * * * * * * 
>>> for i in range(n):
...     for j in range(n-i-1):
...         print(" ",end = " ")
...     for j in range(2*i+1):
...         print("*",end = " ")
...     print()
... 
      * 
    * * * 
  * * * * * 
* * * * * * * 
