print('''
ADDITION       = +
SUBTRACTION    = -
MULTIPLYCATION = *
DIVISION       = /
''')

n1 = eval(input("input the value 1:-"))
n2 = eval(input("input the value 2:-"))
opr = input("Enter the opration:-")

if opr == "+":
    print(n1+n2)
elif opr == "-":
    print(n1-n2)
elif opr == "*":
    print(n1*n2)
elif opr == "/":
    print(n1/n2)
else:
    print("invalid opr...")

print("Thank U For Using Calculator")