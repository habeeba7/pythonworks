
# lst=[]
# tp=()



st=set()  #set

st={20,30,40,50,60,60,50,"hello","hai"}

print(st) #does nor support index

colors={"red","green","blue"}

colors.add("yellow")

print(colors)

st1={1,2,3,10,20}

st2={1,2,3,4,5}

st1.update(st2)

print(st1)

# 10,20,4,5 symmetric diefference(aUb-a@b)

syymetric_difference=st1.symmetric_difference(st2)

print(syymetric_difference)

print(st1.issubset(st2))

# print(st2.issuperset(st1))

text="this is a test to remove duplicate words this test is simple"

text2="this simple test remove duplicate words"


# split text wrt space

# words=text.split(" ")
# print(set(words))

print(set(text2).issubset(set(text)))


