a=int(input('Enter your age:'))

if(a%2==0): # a%2==0 ka mtlab hai ki agar a ko 2 se divide karke zero aata hai tho even
    print('a is even')


if(a>=18):
    print('You are above the age of consent')
    print('Good for you')

elif(a==0):
    print('You are entering 0 which is an invalid input')

else:
    print('Your are below the age of consent')    

print('end of program')

