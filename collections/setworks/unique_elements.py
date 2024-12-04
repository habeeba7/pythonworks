


arr=[10,10,20,30,40,50,40,]

# 10,20,30,40,50

# create empty set
# st=set()

# fetch numbers from array
# for num in arr:
    # add num to set
    # st.add(num)

# display st
# print(st)

st1={10,20,30,40,50}

st1.remove(50)

print(st1)



st2={10,20,60,70}

intersection_set=st1.intersection(st2)

print(intersection_set)

# 10,20,30,40,50,60,70 union()

union_set=st1.union(st2)

print(union_set)

difference_set=st1.difference(st2)

print(difference_set)

