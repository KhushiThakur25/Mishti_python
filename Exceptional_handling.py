'''
try
except
else
finally
raise'''
'''
try:
    a = int(input("Enter your number 1"))
    b = int(input("Enter your number 2"))
    add = a+b
    sub = a-b
    mul = a*b
    div = a/b
except ZeroDivisionError as msg:
    print("Integer can't divided by zero.")
except ValueError as msg:
    print(msg)
except Exception as msg:
    print(msg)
else:
    print(add)
    print(sub)
    print(mul)
    print(div)
finally:
    print("I'm always executed")
'''

def atm():
    PIN = "1234"
    total = 10000
    pin = input("Enter the PIN")
    if PIN ==pin:
        print("Login successfully")
    else:
        raise ValueError("Login Failed")
    amount = int(input("Enter the amount."))
    if amount > total:
        raise ValueError("Insufficient balance")
    else:
        remaining = total - amount
        print("Remaining balance is",remaining)
try:
    atm()
except ValueError as msg:
    print(msg)


