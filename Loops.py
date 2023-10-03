Python loops
While loop, for loop
print hello world 10 times using while loop

i=1
while i<=10:
    print('Hello World')
    i = i+1 #or you can write it as i += 1

EXERCISE 1
n = int(input('Enter any number : '))
total=0
i=1
while i<=n:
    total += i
    i+=1
print('Total is :',total)

EXERCISE 2

name = input('Enter your name : ')
i=0
while i< len(name):
    print(f"{name[i]} : {name.count(name[i])}")
    i += 1


FOR LOOP
Syntex:
for i in range(10): # 0 to 9 
    print(f'Hello Meer: {i}')

for i in range(1,11): # 1 to 10 
    print(f'Hello Meer: {i}')

EXAMPLE 2
Write a program that inputs user name and tell how many times each letter is present in
the name provided(with spaces).
 
name = input('Enter your name : ')
temp = ""
for i in range(len(name)):
    if name[i] not in temp:
        print(f"{name[i]}: {name.count(name[i])}")
        temp +=name[i]

DRY = Don't Repeat Yourself.

Number guessing game with fow loop
import random
winning_n = random.randint(1, 100)
guess = 1
game_over = False
n = int(input('gUESS a number btw 1 to 100 :   '))
while not game_over:
    n = int(input('gUESS again :   '))
    if winning_n> n:
        print('Guess is Low')
        guess+=1
    elif winning_n<n:
        print('Guess is High')
        guess+=1
    elif winning_n==n:
        print(f"You win the game in {guess} attempts")
        game_over = True