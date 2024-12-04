

arr=[100,200,300,400,500,600,700,800]

odd_position_elements=[num for index,num in enumerate(arr) if index%2!=0]
odd_position_elements.reverse()

print(odd_position_elements)



