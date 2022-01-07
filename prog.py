import random
# create a variable with a list

lst = []

for i in range(100):
	lst.append(random.randint(1, 100))
print(lst)

print(len(lst))


res = []

for x in lst:
	if(x >= 10 and x <= 20):
		res.append(x)
		
print(res)


print("The number of times 15 appears in the list is: ",lst.count(15))
