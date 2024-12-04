
from re import finditer

text="fatcatrunsveryfasttocaththerat"

matcher=finditer("at",text) #[(start,gruop),(),(),()]

for obj in matcher:

    print(obj.start(),obj.group())


