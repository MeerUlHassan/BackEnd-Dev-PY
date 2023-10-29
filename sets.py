#SETS ARE : unordered, Mutable and no duplicates

# create a set using curly brackets{,}
my_set = {100, 25.75, "Jessa"}
print(my_set)  # {25.75, 100, 'Jessa'}
print(type(my_set))  # class 'set'  

# create a set using set class
my_set = set({100, 25.75, "Jessa"})
print(my_set)  # {25.75, 100, 'Jessa'}
print(type(my_set))  # class 'set'

# add element to set
my_set.add(300)
print(my_set)  # {25.75, 100, 'Jessa', 300}

# remove element from set
# my_set.remove(100) # remove fun will give us a key error
print(my_set)  # {25.75, 'Jessa', 300}
my_set.discard(100) # discard fun will not give us an error
print(my_set)  # {25.75, 'Jessa', 300}

odds = {1,3,5,7,9,11}
evens = {1,2,4,6,8,10,12}

u = odds.union(evens)
print(u) 

i = odds.intersection(evens)
print(i) 

diff = evens.difference(odds)
print(diff)

odds.update(evens)
print(odds)