#methods used in list
a = [1,2,3]#a is list of numberzs

# to add some element at end of list
a.append(4)
print(a)

# to clear list
a.clear()
print(a)

# to create copy of list
b = a.copy()
print(b)

# to count occurence of an element
e = [1,2,3,2,3,4,2]
print(e.count(2))

# to remove data at end 
a=[1,2,3]
a.pop()
print(a)





# to remove specified element
a.remove(2)
print(a)

# to add element of list[4,5]
a.extend([4,5])
print(a)

# to reverse the list
a.reverse()
print(a)

# to sort list in ascending order
g = [4,3,2,1]
g.sort()
print(g)

# to print data in decending order
print(a.sort(reverse=True))



# to print data in specified index
print(a[2])

# to change element in specified index
a[0]=5
print(a)

# to insert an element in list
b=[1,3]
b.insert(1,2)
# 1 = index,2=object
print(b)
#  ascii table