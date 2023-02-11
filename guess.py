import random
secret_number = random.randint(0, 200)
guess_count = 0
guess_limit = 10
while guess_count < guess_limit:
    guess = int(input('Guess a number (0-200): '))
    guess_count += 1
    if guess == secret_number:
        print('Yay!!!, you won!')
        break
    elif guess > secret_number:
        print("try a lower number")
    elif guess < secret_number:
        print("try a higher number")
else:
    print("You lost, try again")
