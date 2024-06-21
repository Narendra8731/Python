employees=[{'id':101, 'name':'Narendra','sal':45000},
             {'id': 102, 'name': 'Hari', 'sal': 55000},
            {'id': 103, 'name': 'Mahi', 'sal': 65000},
            {'id': 104, 'name': 'Naari', 'sal': 70000}]

for emp in employees:
    print(emp['id'])

for emp in employees:
        print(emp['name'])


total=0
for emp in employees:
      total= total+emp['sal']
      print(total)
