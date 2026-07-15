#Program - Find the sum of a 3 digit number enterd by the user
number = int(input('Enter 3 number ' ))
#345%10->. 5
a = number % 10

#345//10->. 34
number = number //10
#34%10->4
b = number % 10
number = number // 10
#3%10->3
c = number % 10

print(a+b+c)


 
