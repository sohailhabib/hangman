# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 09:18:01 2019

@author: User
"""
#secret_word = 'aeroplane'
#letters_guessed = ['e','a','i','l','r','o','p','n']
#ret_string = '_ '*len(secret_word)
#matches=0
#index=0
#
#for char1 in secret_word:
#    for char2 in letters_guessed:
#        if char1 == char2:
#            print('match found which is',char1,'and it is on',index,'of word')
#            ret_string=ret_string[0:(index*2)]+char1+ret_string[(index*2+1):]
#            matches+=1
#            break
#    index+=1
#    
#
#if matches == len(secret_word):
#    guessed = True
#else:
#    guessed = False
#ret_string = ret_string.replace(" ","")
#index1 = 0
#for char3 in ret_string:
#    if char3 == "_":
#       ret_string = ret_string[0:index1] + " " + ret_string[index1+1:]
#    index1+=1
#ret_string = ret_string.replace(" ","_ ")
import string

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

def get_input(warnings,guesses,avail_alphabet):
    '''Function for getting user input
    '''
    user_guess = input('Enter your guess ')
    user_guess = user_guess.lower()
    is_alpha = user_guess.isalpha()
    already_gussed = avail_alphabet.find(user_guess)
    #if user has already guessed the aplhabet then they lose a guess
    if is_alpha == True:
        if already_gussed == -1:
            print('This alphabet is already guessed')
            warnings -=1
            if warnings < 0:
                guesses -= 1
                warnings = 0
        
    
    if is_alpha == False:
        print('Please Enter an alphabet')
        warnings -=1
        if warnings <= 0:
            guesses -= 1
            warnings = 0
   
  
    return user_guess, warnings, guesses

word = 'aeroplane'
num_of_gusses = 6
num_of_warnings = 3
guessed = []
word_is_guessed = False
vowels = 'aeiou'
print('Welcome to the game Hangman!')
print('I am thinking of a word that is ',len(word),' letters long')

while word_is_guessed == False:
     
    print('You have ', num_of_gusses,' gusses left')
    print('Remaining Warnings ', num_of_warnings,)
    available_letters = get_available_letters(guessed)
    print('Available letters:' , available_letters)
    guessed_alphabet, num_of_warnings, num_of_gusses = get_input(num_of_warnings,num_of_gusses,available_letters)
    
       
    guessed.append(guessed_alphabet)
    guessed_list = get_guessed_word(word,guessed)
    word_is_guessed = is_word_guessed(word,guessed)
    if guessed_alphabet.isalpha() == True:
        
        if word.find(guessed_alphabet) != -1:
            print('Good guess: ', guessed_list)
            print('_ _ _ _ _ _ _ _ _ _ _\n')
            
        elif word.find(guessed_alphabet) == -1:
            print('Oops! That is not in my word: ', guessed_list)
            print('_ _ _ _ _ _ _ _ _ _ _\n')
            
            if vowels.find(guessed_alphabet) != -1:
                if available_letters.find(guessed_alphabet) != -1:
                    print('You failed to guess a vowel so you lose 2 gusses')
                    num_of_gusses -=2
            else:
                if available_letters.find(guessed_alphabet) != -1:
                    num_of_gusses -=1
    if num_of_gusses < 0:
        print('YOU HAVE RUN OUT OF GUSSES SO YOU LOSE THE GAME')
        print ('The word that I was thinking was',word)
        break



#print(is_word_guessed(word,guessed))
#out_word = get_guessed_word(word,guessed)
#print(out_word)
#string1 = get_available_letters(guessed)
#print(len(string1))