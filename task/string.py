
from re import finditer

text="On june 5th, 2024, we will celebrate @ our annual event: 'Tech innovations 2024!'"


pattern="[a-zA-Z]"

matcher=finditer(pattern,text)

for alphs in matcher:

      count=alphs.start(),alphs.group()
      print(len(count))
