# SIMPLE IF-ELSE STATMENT

# PASSWORD = input("Enter password: ")

# if PASSWORD == "DWUE9NKw":
#     print("Password correct")
# else:
#     print("Password incorrect")

# IF-ELIF-ELSE STATMENT

# def user_check(choice):
#     if choice == 1:
#         print("Admin")
#     elif choice == 2:
#         print("Editor")
#     elif choice == 3:
#         print("Guest")
#     else:
#         print("Wrong entry")

# user_check(1)
# user_check(20)
# user_check(3)
# user_check(4)

# NESTED-IF ELSE STATMENT

# num1 = int(input('Enter first number '))
# num2 = int(input('Enter second number '))

# if num1 >= num2:
#     if num1 == num2:
#         print(num1, 'and', num2, 'are equal')
#     else:
#         print(num1, 'is greater than', num2)
# else:
#     print(num1, 'is smaller than', num2)


# number = 56
# if number > 0: print("positive") 
# else: print("negative")

var = 10
for i in range(10):
    for j in range(2, 10, 1):
        if var % 2 == 0:
            continue
            var += 1
    var+=1
else:
    var+=1
print(var)


x = 0
while (x < 100):
      x+=2
print(x)