import random

def hangman():
    words=[
    "apple", "banana", "cherry", "date", "elderberry", "fig", "grape",
    "honeydew", "kiwi", "lemon", "mango", "nectarine", "orange", "papaya",
    "quince", "raspberry", "strawberry", "tangerine", "ugli", "vanilla",
    "watermelon", "yellow", "zucchini", "avocado", "blueberry",
    "cantaloupe", "dragon", "eggplant", "grapefruit"]
    
    random_word=words[random.randint(1,28)]
    # print(random_word)

    print('Welcome to the hangman game!')
    print(f'The word has been selected, it has {len(random_word)} letters')
    
    hidden_word = hidden_letters_array(random_word)
    guessed_word = hidden_word
    
    print(guessed_word)
    print('please guess a letter')
    
    guess = input()
    
    guess_array = []
    guess_array.append(guess)
    
    guessed=False

    while guessed == False:
                
        if guess in random_word:
            print("letter is in the word!")
            
            guessed_word = find_letters(random_word, guess, guessed_word)
            
            print(guessed_word)
            
            guess = input(f"please guess another letter or word: (guessed letters- {guess_array})")

            guess_array.append(guess)
            
            if guess == random_word:
                guessed = True
                    
        else:
            print("letter is not in the word, try again!")
            guess = input (f'please guess another letter or word: (guessed letters- {guess_array})')
            guess_array.append(guess)

    if guessed == True:
        print ("!!CONGRATULATIONS!!\nYOU WIN!!!")


def hidden_letters_array(word):
    return_array = []
    
    for l in word:
        return_array.append('_')
    
    return return_array


def find_letters(word, letter,input_array):
    positions = [pos for pos, char in enumerate(word) if char == letter]
    
    # print(f'letter is in the {positions} positions')
    
    for i in positions:
        input_array[i] = letter
    
    return input_array

    
hangman()