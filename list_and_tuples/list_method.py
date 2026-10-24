friends=['apple','orange',340.3,444,'harsh','gupta']
print(friends[0])
friends[0]=('grapes') #strings are not changeable but lists are changeable
print(friends[0])

# append method se list ke last me add hoga

friends.append(3334)
print(friends)

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
