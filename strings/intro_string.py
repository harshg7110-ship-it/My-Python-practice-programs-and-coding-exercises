name= 'Harsh'

print(len(name)) # ans is 5 because string index starts with 0 

nameshort= name[0:3] #handbook jarur dekh lena  numbers yanha par 0 se start honge 

# agar right to left ja rahe ho or agar left to right ja rahe ho to -1 se start honge 
 
print(nameshort) #here 0 se lekar 2 tak character output me aayenge 3rd character include nahi hoga 

character1= name[1]

print(character1) #yanha par sirf firts character output me aayega yaniki A aayega

print(name[10]) # IndexError: string index out of range because only 5 index are there 

name[0]="J" # idher 0 index pe jo bhi hoga vo replace ho jayega 
print(name)

word="Computer"
print(word[-3]) # negative me right to left and starts with -1  
# output = t


#Predic the output

text = "harsh"
print(len(text))
print(text[4])

text="Python"
x=len(text)
print(x+text[1])
# output= typeError because 6+"y" int+string

text="Artificial"
print(text[2:7]) # output = 2 to 7 = t i f i c

word = "MachineLearning"
print(word[-3] + word[2])

text = "Python"
number = 10
result = text[0] * number
print(result)

text = "AI"
x = True
print(text[0] + x) #output= typeError because string+boolean

