num=[1,2,3,4,5,6,7,]
print(num[0])
print(num[:2])
print(num[2:4])
print(num[-1])
names=['tomal','kamal','jamal']
valus=[5.50,'karim',7]
print(valus)
mil=[num, names]
print(mil)
num.append(8)
num.insert(1,66)
num.remove(8)
num.pop()# last element
del num[2:4]
num.extend([12,22,32])
#num.extend(names)
num.sort()

print(min(num))
print(max(num))
print(sum(num))
print(num)
print(num[-1])
