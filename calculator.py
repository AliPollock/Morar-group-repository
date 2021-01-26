x=int(input("enter value for x: "))
y=int(input("enter value for y: "))
symbol = input("enter operator ('*', '+', '-', '/'): ")

if symbol == '*':
    print(x*y)
elif symbol == '/':
    print(x/y)
elif symbol == '+':
    print(x+y)
elif symbol == '':
    print(x-y)
else:
    print("invalid operator")
