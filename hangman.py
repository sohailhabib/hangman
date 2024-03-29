# Problem Set 2, hangman.py
# Name:
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
global wordlist
wordlist = load_words()



def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"

    matches=0
    index=0

    for char1 in secret_word:
        for char2 in letters_guessed:
            if char1 == char2:
                matches+=1
                break
            index+=1
    

    if matches == len(secret_word):
        guessed = True
    else:
        guessed = False
    return guessed



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    ret_str =""
    index = 0
    let_con = 0 #used to check if an alphabet is in the guessed_string
   
    for char1 in secret_word:
       for char2 in letters_guessed:
           if char1 ==  char2:
               ret_str = ret_str[0:index] + char1
               break
           let_con +=1
           if let_con == len(letters_guessed):
               ret_str = ret_str[0:index] + '_ '
               index+=1
               
           
       let_con = 0        
       index +=1
    return ret_str



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    available_letters = string.ascii_lowercase
    
    for char1 in available_letters:
        for char2 in letters_guessed:
            if char1 == char2:
                available_letters = available_letters.replace(char1,"")
                break


    return available_letters

def get_input(warnings,guesses,avail_alphabet,warnings_over):
    '''Function for getting user input
    '''
    
    user_guess = input('Enter your guess ')
    user_guess = user_guess.lower()
    is_alpha = user_guess.isalpha()
    already_gussed = avail_alphabet.find(user_guess)

    #if user has already guessed the aplhabet then they lose a guess
    if is_alpha == True:
        if already_gussed == -1:
            warnings -=1

                       
            if warnings < 0:
                guesses -= 1
                warnings = 0
                warnings_over = True
        
    
    if is_alpha == False:
        warnings -=1
        
        if warnings < 0:
            guesses -= 1
            warnings = 0
            warnings_over = True
            

   
  
    return user_guess, warnings, guesses,warnings_over

def get_input_hints(warnings,guesses,avail_alphabet,warnings_over):
    '''Function for getting user input
    '''
    
    user_guess = input('Enter your guess ')
    user_guess = user_guess.lower()
    if user_guess == "*":
        print(show_possible_matches(guessed_list))
        help_req = 1
    else:
        help_req = 0
    is_alpha = user_guess.isalpha()
    already_gussed = avail_alphabet.find(user_guess)

    #if user has already guessed the aplhabet then they lose a guess
    if is_alpha == True:
        if already_gussed == -1:
            warnings -=1

                       
            if warnings < 0:
                guesses -= 1
                warnings = 0
                warnings_over = True
        
    
    if is_alpha == False:
        if user_guess == "*":
            warnings = warnings
        else:
            warnings -=1
        
        if warnings < 0:
            guesses -= 1
            warnings = 0
            warnings_over = True
            

   
  
    return user_guess, warnings, guesses,warnings_over,help_req


def calc_score(guess_remain,word):
    '''
    Function for calculating the game score
    '''
    word_set = set(word)
    unique_letters = len(word_set)
    total_score = guess_remain*unique_letters
    
    return total_score


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"'
    num_of_gusses = 6
    num_of_warnings = 3
    guessed = []
    word_is_guessed = False
    warnings_over = False
    vowels = 'aeiou'
    first_run =  True
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is ',len(secret_word),' letters long')
    
    while word_is_guessed == False:
         
        print('You have ', num_of_gusses,' gusses left')
        if(first_run == True):
            print('Remaining Warnings ', num_of_warnings,)
            first_run = False
            
        available_letters = get_available_letters(guessed)
        print('Available letters:' , available_letters)
        guessed_alphabet, num_of_warnings, num_of_gusses, warnings_over = get_input(num_of_warnings,num_of_gusses,available_letters,warnings_over)
        
           
        guessed.append(guessed_alphabet)
        global guessed_list
        guessed_list = get_guessed_word(secret_word,guessed)
        word_is_guessed = is_word_guessed(secret_word,guessed)
        
        if guessed_alphabet.isalpha() == True:
            
            if secret_word.find(guessed_alphabet) != -1:
                print('Good guess: ', guessed_list)
                print('_ _ _ _ _ _ _ _ _ _ _\n')
                
            elif secret_word.find(guessed_alphabet) == -1:
                print('Oops! That is not in my word: ', guessed_list)
                print('_ _ _ _ _ _ _ _ _ _ _\n')
                
                if vowels.find(guessed_alphabet) != -1:
                    if available_letters.find(guessed_alphabet) != -1:
                        print('You failed to guess a vowel so you lose 2 gusses')
                        num_of_gusses -=2
                else:
                    if available_letters.find(guessed_alphabet) != -1:
                        num_of_gusses -=1
#This part handels the messages if the letter is already guessed
#        if num_of_warnings >= 0:
#            warnings_over = False
#        else:
#            warnings_over = True
#        
        already_guessed = available_letters.find(guessed_alphabet)
        if already_guessed != -1:
            already_guessed_status = False
        elif already_guessed == -1:
            already_guessed_status = True
            
        if (guessed_alphabet.isalpha() == True and \
            already_guessed_status == True and \
            warnings_over == False):
            print('Oops! You have already guessed this letter. You have',num_of_warnings,' warnings left:',guessed_list)
        elif (guessed_alphabet.isalpha() == True and \
              already_guessed_status == True and \
              warnings_over == True):
            print('Oops! TYou have already guessed this letter. You have no warnings left:')
            print('so you lose a guess',guessed_list)
            
#This part handels the messages if the gussed word is an alaphabet
        if (guessed_alphabet.isalpha() == False and \
            warnings_over == False):
            print('Oops! That is not a valid letter. You have',num_of_warnings,'warnings left:',guessed_list)
        elif (guessed_alphabet.isalpha() == False and \
              warnings_over == True):
            print('Oops! That is not a valid letter. You have no warnings left:')
            print('so you lose a guess',guessed_list)
            
        if word_is_guessed == True:
            print('Your Guess is correct you won the word was',secret_word)
            print('Your toal score for this game is',calc_score(num_of_gusses,secret_word))
        if num_of_gusses <= 0:
            print('YOU HAVE RUN OUT OF GUSSES SO YOU LOSE THE GAME')
            print ('The word that I was thinking was',secret_word)
            break
    



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    word1 = my_word.replace(' ','')
    word2 = other_word
    match = False
    length = len(word2)
    num1 = 0
    num2 = 0

    if len(word1) == len(word2):
        for x in range(length):
            if word1[x] != '_':
                num1 = word1.count(word1[x])
                num2 = word2.count(word2[x])
                if num1 == num2:
                    if word1[x] == word2[x]:
                        match = True
                    else:
                        match = False
                        break
                    
                else:
                    match = False
                    break
            elif word1[x] == '_':
                match = True
         
    return match
    pass



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
#    pass
    ret_list = list()
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for word in wordlist:
        if match_with_gaps(my_word,word):
            ret_list.append(word)
    
    if not ret_list:
        print('No matches found')
    ret_str = " "
    ret_str = ret_str.join(ret_list)
    return ret_str
     




def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    num_of_gusses = 6
    num_of_warnings = 3
    guessed = []
    word_is_guessed = False
    warnings_over = False
    vowels = 'aeiou'
    first_run =  True
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is ',len(secret_word),' letters long')
    
    while word_is_guessed == False:
         
        print('You have ', num_of_gusses,' gusses left')
        if(first_run == True):
            print('Remaining Warnings ', num_of_warnings,)
            first_run = False
            
        available_letters = get_available_letters(guessed)
        print('Available letters:' , available_letters)
        guessed_alphabet, num_of_warnings, num_of_gusses, warnings_over, help_req = get_input_hints(num_of_warnings,num_of_gusses,available_letters,warnings_over)
        
           
        guessed.append(guessed_alphabet)
        global guessed_list
        guessed_list = get_guessed_word(secret_word,guessed)
        word_is_guessed = is_word_guessed(secret_word,guessed)
        
        if guessed_alphabet.isalpha() == True:
            
            if secret_word.find(guessed_alphabet) != -1:
                print('Good guess: ', guessed_list)
                print('_ _ _ _ _ _ _ _ _ _ _\n')
                
            elif secret_word.find(guessed_alphabet) == -1:
                print('Oops! That is not in my word: ', guessed_list)
                print('_ _ _ _ _ _ _ _ _ _ _\n')
                
                if vowels.find(guessed_alphabet) != -1:
                    if available_letters.find(guessed_alphabet) != -1:
                        print('You failed to guess a vowel so you lose 2 gusses')
                        num_of_gusses -=2
                else:
                    if available_letters.find(guessed_alphabet) != -1:
                        num_of_gusses -=1
#This part handels the messages if the letter is already guessed
#        if num_of_warnings >= 0:
#            warnings_over = False
#        else:
#            warnings_over = True
#        
        already_guessed = available_letters.find(guessed_alphabet)
        if already_guessed != -1:
            already_guessed_status = False
        elif already_guessed == -1:
            already_guessed_status = True
            
        if (guessed_alphabet.isalpha() == True and \
            already_guessed_status == True and \
            warnings_over == False):
            print('Oops! You have already guessed this letter. You have',num_of_warnings,' warnings left:',guessed_list)
        elif (guessed_alphabet.isalpha() == True and \
              already_guessed_status == True and \
              warnings_over == True):
            print('Oops! TYou have already guessed this letter. You have no warnings left:')
            print('so you lose a guess',guessed_list)
            
#This part handels the messages if the gussed word is an alaphabet
        if (guessed_alphabet.isalpha() == False and \
            warnings_over == False) and \
            help_req != 1:
            print('Oops! That is not a valid letter. You have',num_of_warnings,'warnings left:',guessed_list)
        elif (guessed_alphabet.isalpha() == False and \
              warnings_over == True and \
              help_req != 1):
            print('Oops! That is not a valid letter. You have no warnings left:')
            print('so you lose a guess',guessed_list)
            
        if word_is_guessed == True:
            print('Your Guess is correct you won the word was',secret_word)
            print('Your toal score for this game is',calc_score(num_of_gusses,secret_word))
        if num_of_gusses <= 0:
            print('YOU HAVE RUN OUT OF GUSSES SO YOU LOSE THE GAME')
            print ('The word that I was thinking was',secret_word)
            break
    

    



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    secret_word = choose_word(wordlist)
#    secret_word = 'else'
    hangman_with_hints(secret_word)
#    print(match_with_gaps('a_ ple','apple'))
    
#    print(show_possible_matches("*"))

###############

    # To test part 3 re-comment out the above lines and
    # uncomment the following two lines.

    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
