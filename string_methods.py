# first_name = "Meer"
# last_name = "UL Hassan"
# full_name = first_name +" "+ last_name
# print(full_name)

# # num1=int(input("Enter first number ?"))
# num2=int(input("Enter 2nd number ?"))
# total=num1 + num2
# print("Total is ",total)

# input two values in one line 
# name, age = input("Enter your name age", "Enter your age")
# name, age = input("Enter your name and age : ").split()
# print(name)
# print(age)

# EXERCISE
# num1,num2,num3 = eval(input("Enter three numbers seperated by commas :"))
# average=(num1+num2+num3)/3
# print("Average is ",average)

# isnumeric method

# string1 = "12345" 
# print(string1.isdigit())

# name = ""
# print(name.join("MEER HASSAN"))

newList = ["I", 'AM', 'LEARING', 'PYTHON']
print(" ".join(newList))


print("this is another example".split(" "))

# name = input("Enter your name :")
# lname = input("Enter last name :")
# # print(f"Wellcome {name}")
# print("Hello {name} {lname}".format(name=name, lname=lname))

# price = 100
# taxPrice = price * 1.50
# print(price, taxPrice)
# print(" Base Price ${:.3f}, Tax Price ${:.3f}".format(price, taxPrice))

# def to_celsius(x):
#     return (x-32) * 5/9

# for x in range(0, 101, 10):
#     print("{:>3} F | {:>6.2f} C".format(x, to_celsius(x)))