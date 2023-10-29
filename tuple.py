# tuples are ordered, immutable(cannot be changed) and can have duplicate values

# def convert_second(seconds):
#     hours = seconds // 3600
#     minutes = (seconds - hours * 3600) // 60
#     remaining_sec = seconds - hours * 3600 - minutes * 60
#     return hours, minutes, remaining_sec

# result  =  convert_second(5000)
# print(result)

# hours, minutes, seconds = convert_second(1000)
# print(hours, minutes, seconds)

courses = ('Math', 'Science', 'Engineering', 'Journal')

# print(courses[0:3])
# print(type(courses))

import sys
list1 = [1,2,'hello', True]
tuple1 = (1,2,'hello', True)

print(sys.getsizeof(list1), 'bytes') #lists has more bytes than tuples
print(sys.getsizeof(tuple1), 'bytes')