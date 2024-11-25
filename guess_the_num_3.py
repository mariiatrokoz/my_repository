'''Guess the Number Game: Make a game where the computer generates a random number, and the player has to guess it.

Input values:

Player guesses the randomly generated number.

Output value:

Feedback on whether the guess is correct, too high, or too low. Repeat until the correct number is guessed.

example: Input values:
Enter your guess: 7


Output value:
Too low! Try again.


Input values:
Enter your guess: 12


Output value:
Too high! Try again.


Input values:
Enter your guess: 10


Output value:
Correct! You guessed the number.'''


import numpy as np

random_int = np.random.randint(1, 101)

result = None

while True:
    guess = int(input("Тімур, який в мене сьогодні психологічний вік? "))
    if guess > random_int:
        result = "Завеликий. Спробуй ще. "
    elif guess < random_int:
        result = "Замалий. Спробуй ще."
    else:
        result = "Вгадав!"
        break

    print(result)

print(result)




