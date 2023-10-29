# Orderd, mutable(can be changed), allow duplicate values
myList = [11,2,31,56,12,3,14,2]

myList.append(10)  #it will insert the item to the end of the list
# myList.sort()  #it will sort the list (assending order)
# myList.sort(reverse=True)  # it will sort the list backwards(descending order)
# myList.reverse() # reverse the list (last item to the first)
# print(myList.index(31))  #it tells us the index of the item presnet in the list
# print(myList.count(3))  it counts how many times the item presnet in the list
# newList = myList  if we make a change in newList the change will also commense in orignal list
# newList[0] = 10
# newList[1] = 5
# print(newList)
# myList.insert(0, 1)  #you can insert an item at any given index using insert function
# nlist = myList
# nlist.insert(0, 1) #you can insert an item at any given index
# print(nlist) 
# myList.remove(2) it remove the item from the list
# myList.pop(1) #it will pop item from the list at given index
# print(min(myList))
# print(max(myList))
# print(sum(myList))
# print(myList[0:5])
# print(myList[3:5])

# n = 300
# m = 200
# m = n
# print(id(n)) # same memory address
# print(id(m))

# myList.append(["i","am", "learning", 'pyhton'])
# myList.extend(["i","am", "learning", 'pyhton'])

# list1 = ['original', 'list']
# list2 = list1.copy()  # it will not change the original list
# list1.append(1)
# print(list1)


# print(myList)

# list1 = ["M", "na", "i", "Ke"]
# list2 = ["y", "me", "s", "lly"]
# # list3 = [list1[0]+ list2[0], list1[1]+ list2[1]]
# list3 = [i + j for i, j in zip(list1, list2)]
# print(list3)


# if 11 in numbers:
#     print('yes')
# else:
#     print('no')

# arr = [x*x for x in numbers]  # list comprehension
# print(arr)

# list = [100,200,300,400,500]
# list.reverse()
# print(list)
numbers = [1, 2, 3, 4, 5, 6, 7]

# for index, num in enumerate(numbers):
#     print(num)
#     if num == 3:
#         print('exit')
#         break
#     else:
#         continue

# for index, num in enumerate(numbers):
#     print(index, num)
