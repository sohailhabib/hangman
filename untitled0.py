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
    let_con = 0
   
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

def get_input(warnings):
    '''Function for getting user input
    '''
    user_guess = input('Enter your guess ')
    is_alpha = user_guess.isalpha()
    if is_alpha == False:
        print('Please Enter an alphabet')
        warnings -=1
        
    else:
        user_guess = user_guess.lower()
    
    return user_guess, warnings

word = 'aeroplane'
num_of_gusses = 6
num_of_warnings = 3
guessed = []
print('Welcome to the game Hangman!')
print('I am thinking of a word that is ',len(word),' letters long')

print('Remaining guesses ', num_of_gusses,)
print('Available letters:' ,get_available_letters(guessed))
guessed, warnings = get_input(num_of_warnings)


#print(is_word_guessed(word,guessed))
#out_word = get_guessed_word(word,guessed)
#print(out_word)
#string1 = get_available_letters(guessed)
#print(len(string1))