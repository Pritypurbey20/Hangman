import string
from words import choose_word
from images import IMAGES


def ifValid(user_input):
    if len(user_input) != 1:
        return False

    if not user_input.isalpha():
        return False
    return True 

def is_word_guessed(secret_word, letters_guessed):
    return False
def get_guessed_word(secret_word, letters_guessed):
    index = 0
    guessed_word = ""
    while (index < len(secret_word)):
        if secret_word[index] in letters_guessed:
            guessed_word += secret_word[index]
        else:
            guessed_word += "_"
        index += 1
    
    return guessed_word

def get_available_letters(letters_guessed):
    import string
    letters_left = string.ascii_lowercase
    for i in letters_guessed:
      letters_left=letters_left.replace(i,"")
    return letters_left

def get_hint(secret_word, letters_guessed):
    import random
    letters_not_guessed = []
    for i in  secret_word:
        if i not in letters_guessed:
            if i not in letters_not_guessed:
                letters_not_guessed.append(i)
    return random.choice(letters_not_guessed) 

def hangman(secret_word):

    print ("Welcome to the game, Hangman!")
    print ("I am thinking of a word that is " + str(len(secret_word)) + " letters long.")
    print ("")
    user_difficulty_choice = input("Aap abhi kitni difficulty par yeh game khelna chahte ho?\na)\tEasy\nb)\tMedium\nc)\tHard\n\nApni choice a, b, ya c ki terms mei batayein\n")

    total_lives = remaining_lives = 8
    letters_guessed = [] 
    images_selection_list_indices = [0, 1, 2, 3, 4, 5, 6, 7]

    if user_difficulty_choice not in ["a", "b", "c"]:
        print ("Aapki choice invalid hai.\nGame easy mode mei start kar rahe hai")

    else:
        if user_difficulty_choice == "b":
            total_lives = remaining_lives = 6
            images_selection_list_indices = [0, 2, 3, 5, 6, 7]

        elif user_difficulty_choice == "c":
            total_lives = remaining_lives = 4
            images_selection_list_indices = [1, 3, 5, 7]
    
    while remaining_lives > 0:
      available_letters = get_available_letters(letters_guessed)
      print("Available letters: " + available_letters)

      guess = input("Please guess a letter: ")
      letter = guess.lower()

      if guess == "hint":
          print("Your hint for this secret word is "+get_hint(secret_word, letters_guessed))
          continue                                                                      
      else:
        if (not ifValid(letter)) and letter!="hint":
          print("invalid input")
          continue

        if secret_word==letters_guessed:
            print (" * * Congratulations, you won! * * ")
            print ("")
            break
        
        if letter in secret_word:
            letters_guessed.append(letter)
            print("Good guess: " + get_guessed_word(secret_word, letters_guessed))
            print("")

        else:
            print ("Oops! That letter is not in my word: " + get_guessed_word(secret_word, letters_guessed))
            print (IMAGES[images_selection_list_indices[total_lives-remaining_lives]]) 
            print ("Remaining Lives : ", remaining_lives)
            print ("")
            letters_guessed.append(letter)
            remaining_lives -= 1 
    else:
      print("Sorry you lose the game,the word was-"+ secret_word )
secret_word = choose_word()
hangman(secret_word)