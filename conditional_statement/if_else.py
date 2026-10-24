a=int(input('Enter your age:'))

# isko if elif else ladder bolte hai

if(a<100>=18):
    print('You are above the age of consent')
    print('Good for you')

# elif if ke bich me kuch condition ke liye use hota hai
elif(a<0):
    print('You are entering an invalid input')

elif(a==0):
    print('You are entering 0 which is an invalid input')
    
# elif(a>100):
#     print("You are entering age above 100 which is an invalid input")

else:
    print('Your are below the age of consent')    

print('end of program')