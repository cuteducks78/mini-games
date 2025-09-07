import random

print("Welcome to the Number Guessing Game!")
print('Levels: \neasy:1-50 \nmedium:1-100 \nhard:1-500')

tries = 0

level = input('Pick a level(easy, medium, hard): ').lower()

if level == 'easy':
    random_number = random.randint(1, 50)
    while True:
        guess = int(input('Guess the number: '))
        tries = tries + 1
        if guess == random_number:
            print('Congrats! You guessed it right!')
            print(f'It took you {tries} tries')
            break
        elif guess > random_number:
            print('Too big! Try again!')
        else:
            print('Too little! Try again!')
elif level == 'medium':
    random_number = random.randint(1, 100)
    while True:
        guess = int(input('Guess the number: '))
        tries = tries + 1
        if guess == random_number:
            print('Congrats! You guessed it right!')
            print(f'It took you {tries} tries')
            break
        elif guess > random_number:
            print('Too big! Try again!')
        else:
            print('Too little! Try again!')
elif level == 'hard':
    random_number = random.randint(1, 500)
    while True:
        guess = int(input('Guess the number: '))
        tries = tries + 1
        if guess == random_number:
            print('Congrats! You guessed it right!')
            print(f'It took you {tries} tries')
            break
        elif guess > random_number:
            print('Too big! Try again!')
        else:
            print('Too little! Try again!')
else:
    print('Invalid input')


