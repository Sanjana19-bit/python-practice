# if-else in pyton
#email -> sanjana@gmail.com
#password -> 1234

email = input('enter email ')
password = input('enter password ' )
if(email=='sanjana@gmail.com' and password =='1234'):
    print('Welcome')
elif(email=='sanjana@gmail.com' and password !='1234'): 
    #tell the user
    print('Incorrect password') 
    password = input('Enter the password again')
    if password == '1234':
        print('Welcome,finally!')
    else:
        print('beta tumse nhi ho payega')
else:
    print('Not correct') 




   