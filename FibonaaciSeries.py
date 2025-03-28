n = 8
first = 0
second = 1
print(first,second,end= " ")
for i in range(2,n):
    third = first + second
    print(third,end=" ")
    first = second
    second = third
