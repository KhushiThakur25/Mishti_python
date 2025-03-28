n = 123
org = n
rev = 0
while n > 0:
    rev = rev * 10 + n%10
    n //= 10
 
if org == rev:
    print("Number is palindrome..")
else:
    print("Number is not palindrome..")
print(rev)