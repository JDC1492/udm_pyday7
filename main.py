import random
#Step 1 

word_list = ["aardvark", "baboon", "camel"]
rand_word = random.randrange(len(word_list))
guess_the_word = word_list[rand_word]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

letter = input("Choose A Letter:")

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

for word_letter in guess_the_word:
  if word_letter == letter:
    print('right')
  else:
    print('wrong')



