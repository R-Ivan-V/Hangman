from art import stages, logo
from words import word_list
import random

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

lives = 6

print(logo)
#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
  display += "_"

while True:
  guess = input("Guess a letter: ").lower()

  if guess in display:
    print(f'You have already entered this letter: "{guess}"')

  #Check guessed letter
  for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
      display[position] = letter
  #Check and punishment
  if guess not in chosen_word:
    if guess not in display:
      print(f'This letter "{guess}" is not in the word')
    lives -= 1
    if lives == 0:
      print("You lose.")
      break

  #Join all the elements in the list and turn it into a String.
  print(f"{' '.join(display)}")

  print(stages[lives])

  if not "_" in display:
    print("You win.")
    break
