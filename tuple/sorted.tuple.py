names = ("Narendra","Naari","Vishnu","Hari","Naari","Naari","Arjun")



 #print(names.sort())     'tuple' object has no attribute 'sort'

print(tuple(sorted(names)))

num=(100,20,5,150,300,450,80)

print(tuple(sorted(num)))