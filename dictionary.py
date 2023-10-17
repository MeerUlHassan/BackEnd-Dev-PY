student = {'name': 'Meer', 'age': 23, 'courses' : ['Math', 'CompSci']}

# print(student['courses'])
# print(student.get('name'))
# print(student.get('phoen', "Not Found"))

# student.update({'name': 'Sam', 'age': 20, 'phone': '042-3453453'})

# del student['courses']  # we can also use pop method here

# print(student.keys(), student.values())
# print(student.items())

# to iterate over each key value pair we can use

for key, value in student.items():
    print(key, value)