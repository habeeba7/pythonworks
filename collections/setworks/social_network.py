

users=["rahul","rohit","kohli","rishab","sanju","pandya","siraj"]

rahul_followers=["rohit","kohli","rishab","rahul"]

sanju_followers=["sanju","rohit","kohli"]

# mutual_friends
# follow_sugestion ["sanju","pandya","siraj"]

rahul_follow_sugg=set(users).difference(set(rahul_followers))

mutual_friends=set(rahul_followers).intersection(sanju_followers)

print(mutual_friends)

print(rahul_follow_sugg)