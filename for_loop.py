# #For loop demo

# for i in range(1,11,2):
#  print(i)

# for i in range(10,0,-1):
#     print(i)

# for i in 'Delhi':
#     print(i)

# for i in [1,2,3,4,5]:
#     print(i)  
# 
# 
#  

#---------------------------------------------------------------------------------------------------------------------------
#Program - The current population of town is 10000. The population of town is increasing at the rate of 10% per year . You have a program to find out the 
#populatin at the end of the last 10 year
curr_pop =10000
for i in range(10,0,-1):
    print(i,curr_pop)
    curr_pop=curr_pop/1.1
#======================================================================

#Question nth terms
#1/1!+2/2!+3/3!+.......

n = int(input('Enter n'))
result=0
fact =1
for i in range(1,n+1):
    fact=fact*i
    result += i/fact
    print(result)



