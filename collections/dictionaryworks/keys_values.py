
# Write a Python program to create a dictionary from a list of keys and values using dictionary comprehension.

keys=["anu","arum","hari"]
values=[43,55,32]

dict_keys_values={keys[i]:values[i] for i in range(len(keys))}
print(dict_keys_values)