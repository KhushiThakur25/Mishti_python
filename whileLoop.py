# i = 1

# while i <= 10:
#     print(i)
#     i += 1

n = 49


prime = True
i = 2
while i < n:
    if(n%i == 0):
        print("Number is not prime..")
        prime = False
        break
    
        
    i += 1  
if prime:
    print("Number is prime...")
   