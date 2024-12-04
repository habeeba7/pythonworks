
text="this is a simple programming question to find word with maximum number of characters "

words=text.split(" ")

# def get_length(w):
#     return len(w)

# print(max(words,key=get_length))

def get_length(w):

    return len(w)

srt_words=sorted(words,key=get_length)

print(srt_words)

# def get_count(w):

#     return words.count(w)

# frequent_word=max(words,key=get_count)

# print(frequent_word)