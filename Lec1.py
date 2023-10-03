example_list = [1, "Hello", 5.9, "S"]
print(type(example_list))
print(example_list[2])

a= int('123')
print(type(a))

num1 = eval(input("Enter 1st number :"))
num2 = eval(input("Enter 2nd number :"))

result = print(num1+num2)
print(result)

billTotal = 94
dics = 10

if billTotal > 100:
    print("Bill is greater than 100")
    billTotal= billTotal-dics
print("Total Bill " +str(billTotal))

for i in range(10,100):     #range(starting, ending, stepSize)
    print("Loading",i)