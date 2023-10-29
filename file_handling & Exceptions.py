# with open('sales.txt', 'x')as f:
#     f.write('First Line\n 2nd line\n Third')

# try:
    # with open('D:\BackEnd-Dev-P\sales.txt', 'r') as fp:
#         print(fp.readlines())
# except FileNotFoundError as e:
#     print(e)
    

# try:
#     with open ('countries.txt', 'x') as file:
#         file.write('Pakistan\nAustralia\nUnited States\nCanada')
#         print('File successfully created')
# except FileNotFoundError as e:
#     print('File not found')
# finally:
#     print('Exit')

# try:
#     with open ('countries.txt', 'r') as file:
#         print('File successfully created')
#         print(file.read())
# except FileNotFoundError as e:
#     print('File not found')
# finally:
#     print('Exit')

# try:
#     with open('countries.txt', 'a') as fp:
#         fp.write("\nAdded this line by opening the file in append mode ")
#         print("File successfully edited")
# except FileNotFoundError as t:
#     print(t)
# finally:
#     print('Exit')


# try:
#     # Creating a new file
#     with open("sample.txt", "x") as fp:
#         fp.write("Hello World! I am a new file")

#     # reading the contents of the new file
#     fp = open("sample.txt", "r")
#     print(fp.read())
# except FileExistsError:
#     print("The file already exists")

try:
    # opening a exsisting file
    with open("sample.txt", "r+") as fp:
        print(fp.read())
    # adding some more content to the file
        fp.write('\nThis is a new Line')
        print('File updated')
except FileExistsError:
    print("The file already exists")
finally:
    print('Exit')


# try:
#     with open('fastFood.txt', 'x') as f:
#         f.write('Burger\nPizza')
#         print('file created')
# except Exception:
#     print('Error...')
# finally:
#     print('exit')

# try:
#     with open('fastFood.txt', 'r+') as f:
#         print(f.read())
# except Exception as e:
#     print(e)
# finally:
#     print('exit')