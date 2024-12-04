

# class list:

#     def append(self):

#     def pop(self)
#     def insert(self,index,object)
#     def index(self,object)
#     def copy()
#     def sort(reverse=false)
#     count()

colors=["red","green","blue"]

colors.append() #insert new object to end of the list

colors.append("yellow")

# print(colors)

# colors.pop() remove last object from the list and return it
# colors.pop()

# colors.pop(0)

# print(colors)

# colors.insert(0,"purple")

# print(colors)

# red_index=colors.index("red") #return index of first occurance red
# print(red_index)

praveen_fvt_colors=["blue","yellow","black","white"]

my_fvt_colors=praveen_fvt_colors.copy()

my_fvt_colors.pop()

print("my",my_fvt_colors)
print("praveen",praveen_fvt_colors)

# copy()
# index(object)
# pop()
# append()
# insert(index,object)
# sort()
# extend()
# reverse()

# lst=[2,6,3,4,5,6]

# lst.sort()
# lst.sort(reverse=True)

# print(lst)

fruits=["apple","orange","mango"]

products=["onion","potato","brinjal"]

products.extend(fruits)

fruits.reverse()

print(products)

print(fruits)
