# #take i/p to user and store in a variable 
# a=int(input('Enter 1st number ' ))
# b=int(input('Enter 2nd number ' ))
# print(type(a),type(b))
# # add the 2 variables
# result=int(a)+int(b)
# #print the result
# print(result)
# print(type(a))




# #Literals--------------------------------------------
# a =0b1010
# b = 100
# c = 0o310
# d = 0x12c

# float_1 = 10.5
# float_2 = 1.5e2

# print(a,b,c,d)
# print(float_1,float_2)




# #binary 
# x = 3.14j
# print(x.real)

# k=None
# a=5
# b=10


n=int(input('enter n'))
result=0
fact=1
for i in range(1,n+1):
    fact=fact*i
    result=result+i/fact
print(result)  