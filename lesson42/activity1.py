import numpy as np
data_type = [('name', 'S15'), ('class', int), ('height', float)]
student_details = [('Akshita', 9 , 160.02), ('Aakash', 4 , 139.70), ('Kashwini', 9 , 157.48), ('Arvind', 9 , 165.10)]
students = np.array(student_details, dtype=data_type)
#create a structured array 
print("Original array:")
print(students)
print("Sort by height")
print(np.sort(students, order = 'height'))