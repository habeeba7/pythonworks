



# print("Good",end="$$")

# print("Afternoon",end="\t")

# print("All")


#     c1   c2 c3
# 1 r1 *   *   *
# 2 r2 *   *   *
# 3 r3 *   *   *
# 4 r4 *   *   *
# 5 r5 *   *   *
# 6 r6 *   *   *



for row in range(1,7):

    for col in range(1,4):

        print("*",end="\t")

    print()



for row in range(1,7):

    for col in range(1,row+1):

        print("$",end="\t")

    print()


# 1
# 2  2
# 3  3  3
# 4  4  4  4
# 5  5  5  5  5


         
for row in range(1,6):
    for col in range(1,row+1):

        print(row,end="\t")

    print()


#  *   *   *   *   *
#  *   *   *   *   
#  *   *   *   
#  *   *   
#  *  

for row in range(5,0,-1):

    for col in range(1,row+1):

        print("*",end="\t")

    print()



for row in range(1,6):

    for col in range(5,row-1,-1):

        print("*",end="\t")

    print()