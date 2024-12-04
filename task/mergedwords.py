word1="abc"

word2="pqr"

merged_word=""

for i in range(0,len(word1)):
    merged_word+=word1[i]+word2[i]

print(merged_word)