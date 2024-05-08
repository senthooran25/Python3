# def find_duplicate(numlst):
#     snumlist = sorted(numlst)
#     print(snumlist)
# l=[4,5,8,11,56,4,5,7,96,35,14,45]
# find_duplicate(l)

#Python program to print a list
# without using the sort() function
# without an extra variable

# l1=[76, 23, 45, 12, 54, 9]
# print("Original List:", l1)
#
# # sorting list using nested loops
# for i in range(0, len(l1)):
# 	for j in range(i+1, len(l1)):
# 		if l1[i] >= l1[j]:
# 			l1[i], l1[j] = l1[j],l1[i]
#
# # sorted list
# print("Sorted List", l1)

#
# def revomesort(lst):
# 	newlst = list(sorted(set(lst)))
# 	print(newlst)
# 	newsrt = ''.join(newlst)
# 	print(newsrt)
#
#
#
# a = ['a','e','f','a','s','d','e','f']
# revomesort(a)


# def fun(num):
# 	if num < 0 or num <= 1000:
# 		print('this number is between 1 to 1000')
# fun(10055)

class Car:
	def __init__(self,num,doors):
		self.num = num
		self.doors =doors

	def wheels(self):
		print("This car has  wheels =", self.num)

class audi(Car):
	def doors(self):
		print('Number of Doors =', self.doors)

c = Car(5,10)
Myaudi = audi(4,5)
print(Myaudi.doors())
