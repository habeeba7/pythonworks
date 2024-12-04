# Given a sentence, count the frequency of each word using a dictionary.

text="this is a simple programming question is to find word with maximum number of characters "

word=text.split(" ")

word_count={}

for w in word:

    if w in word_count:

        word_count[w]+=1

    else:

        word_count[w]=1

print(word_count)
