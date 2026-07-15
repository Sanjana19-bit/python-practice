#menu driven calculator
a = int(input('Enter the 1st number'))
b  = int(input('Enter the 2nd number'))

op = input('Enter the operations')
if op=='+':
    print(a+b)
elif op == '-':
    print(a-b)
elif op == '*':
    print(a*b)
elif op == '/':
    print(a/b)
else:
    print('Not found the number')            
