friends=['apple','orange',340.3,444,'harsh','gupta']
print(friends[0])
friends[0]=('grapes') #strings are not changeable but lists are changeable
print(friends[0])

# append method se list ke last me add hoga
friends.append(3334)
print(friends)

#extend() add multiple items
numbers = [10, 20, 30]
numbers.extend([40, 50])
print(numbers)

#Major diff between append() and extend()
# Using append()
# a = [1, 2]
# a.append([3, 4])
# print(a)
# Output:[1, 2, [3, 4]] # Length = 3 because it consider [3,4] a single thing

# Using extend()
# a = [1, 2]
# a.extend([3, 4])
# print(a)
# Output:[1, 2, 3, 4] #Length:4

#sort me agar number ulte sidha likha hai to sahi hojaenge

l1=[1,10,5,90,1110,111011,2332,839,1740,]
l1.sort()
print(l1)

# reverse me aapki list reverse hojaegi
l1.reverse()
print(l1)

# insert things ko bechme ya list me kahi par bhi insert kar deti 
# hai or 'endswith' or 'startswith' sirf start me ya end me insert karti ha
l1.insert(3,334343)  #list ke index ke hisabse place lihni hai fir jo likhna hai 
print(l1)

l1.pop(2) #2 index delete ho gya
print(l1)

#remove() remove specific value

#clear() remove all items
#count() count how many times a value appears
#copy() create a shallow copy

# What will be the output?

numbers = [10, 20]
numbers.append(30)
numbers.append(40)
print(len(numbers))
print(numbers[-1])