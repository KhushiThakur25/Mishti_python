n = int(input("Enter the value for n.."))
org = n
count = 0
sum_ = 0
while n > 0:
    count += 1
    n //= 10
#print("Your count of number is :",count)

n = org
#print("Your n is:",n)

while n > 0:
    sum_ = sum_ + pow(n%10,count)
    n //= 10
#print("Your sum is:",sum_)

if sum_ == org:
    print("Your number is an Armstrong..")
else:
    print("Your number is not an Armstrong..")
