
lst=[
    1,2,
    [10,20],
    [1,2,5,[10,3]],
    100
    ]

list_objects=[item for item in lst if isinstance(item,list)]
print(max(list_objects,key=len))