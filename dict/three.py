emp={'id':101,'Name':'Narendra','loc':'Bangalore'}
print(emp.get('id'))
print(emp.get('Name'))


emp.pop('loc')
emp.popitem()
print(emp)