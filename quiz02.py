def skip_elements(element):
    myList = []
    i = 0
    for i in element:   
        if int(i) % 2 == 0:
            myList.append(i)
        i += 1
    return myList

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"]))
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach']))
print(skip_elements([])) 
