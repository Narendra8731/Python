list = [10,20,40,50,60]
b=bytes(list)
b[2] = 30
for value in b:
  print(value)   #TypeError: 'bytes' object does not support item assignment