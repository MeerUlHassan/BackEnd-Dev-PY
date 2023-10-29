# DICTIONARY IS UNORDERED, MUTABLE, AND IN KEY-VALUE PAIR

student = {'name': 'Meer', 'age': 23, 'courses' : ['Math', 'CompSci']}
stu2 = dict(name='Meer', age= 23, courses= 'Programming') # also a way to create dict using dict class
# print(stu2)

# val = student['courses']
# print(val)
# student.popitem()  # it will pop the laste item 
# student.pop('age') # it will pop the given key
# try:
#     print(student['lastname'])
# except:
#     print('Error')
print(student)

# print(type(student))
# print(student['courses'])
# print(student.get('name', 'Found'))
# print(student.get('phone', "Not Found"))

# student.update({'name': 'Sam', 'age': 20, 'phone': '042-3453453'})

# del student['courses']  # we can also use pop method here

# print(student.keys(), student.values())
# print(student.items())

# to iterate over each key value pair we can use

for key, value in student.items():
    print(key, value)


