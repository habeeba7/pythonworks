# Given two lists, one with fruits and the other with prices, write a dictionary comprehension to pair them together into a dictionary.


fruits=["apple","banana","mango"]
price=[32,41,23]

price_fruit={fruits[i]:price[i] for i in range(len(price))}
print(price_fruit)

