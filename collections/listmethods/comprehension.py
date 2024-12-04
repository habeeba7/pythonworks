# list comprehension

# [return iteration condition]

arr=[2,3,4,5,6,7]

map_num=[num+1 if num>5 else num-1 for num in arr]
print(map_num)
squares=[num**2 for num in arr]
print(squares)

add_ten=[num+10 for num in arr]

print(add_ten)

evens=[num for num in arr if num%2==0]

print(evens)

odd_numbers=[num for num in arr if num%2!=0]
print(odd_numbers)

text=["apple","iphone","orange","potatto","tomatto"]

# words starting with vowels

vowel_words=[w for w in text if w[0] in ['a','e','i','o','u']]

print(vowel_words)

constant_words=[w for w in text if w[0] not in ['a','e','i','o','u']]
print(constant_words)

# longest word
long=max([len(w) for w in text])

longest_words=[w for w in text if len(w)==long]

print(longest_words)
