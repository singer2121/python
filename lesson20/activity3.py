student_data = {'id1':
        {'name': ['Akshita'],
         'class':['VIII'],
         'subject_integration':['English , hindi,punjabi']
           },
        'id2':
        {'name': ['Piya'],
         'class':['VIII'],
         'subject_integration':['English , hindi,punjabi']
           },
        'id3':
        {'name': ['Haripriya'],
         'class':['VIII'],
         'subject_integration':['English , hindi,punjabi']
           },
        'id4':
        {'name': ['Anika'],
         'class':['VIII'],
         'subject_integration':['English , hindi,punjabi']
           },
        }

result = {}

for key,value in student_data.items():
    if value not in result.values():
        result[key] = value

print(result)
        