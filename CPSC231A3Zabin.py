# NAME: MAHIRA ZABIN
# UCID: 30150211

# import necessary modules
import random

# pick a random word
def pickRandomWord():
    words = []
    # open file
    with open('lexicon.txt', 'r') as file:
        line = file.readline()
        # arrange the words into a dictionary using While loop
        while line:
            words.append(line.replace("\n","".strip()))
            line = file.readline()
    # pick a random index
    index = random.randint(1,len(words))
    choice = words[index]
    return choice

print("Welcome to Hangman!")
print("The secret word looks like: ")

encryptedWord = pickRandomWord() # secret word is the Choice 
dashes = list(encryptedWord) # find out how many dashes need to be displayed
listForDisplay = []

# create a display list using the number of dashes for the chosen word
for char in dashes:
    listForDisplay.append("_")

# initialize some variables
count = len(encryptedWord)
guesses = 0
letter = 0
usedList = []
badGuesses = []
badGuessesStr = ""
guess_limit = 8

# as long as there are still dashes and guess limit has not been reached:
while count != 0 and guesses < guess_limit:

    found = False
    # display current state of dashes/letters
    print(" ".join(listForDisplay))
    # take user input
    letter = input("Guess your letter: ")

    if letter.lower() in usedList:
        print("You already guessed that letter!")
    # if the new user input letter has not been entered before
    else:
        # iterate through the range of the length of the secret word
        for i in range(0,len(encryptedWord)):
            # if the user input matches any letter(s) of the secret word, replace _ in that position with the user input
            if letter.lower() == encryptedWord[i]:
                found = True
                listForDisplay[i]=letter.lower()
                count -= 1 
        # if user input did not match, add one wrong guess, add the input to the list of bad guesses
        if found == False: 
            badGuesses.append(letter)
            badGuesses.append(" ")      
            guesses +=1
            print()
            print("Sorry, there is no '" + letter +"'")

            # draw hangman for every wrong guess, sequentially 
            if guesses == 1:
                print("   _____ \n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "  |      \n"
                      "__|__\n")

            elif guesses == 2:
                print("   _____ \n"
                      "  |     | \n"
                      "  |     |\n"
                      "  |     | \n"
                      "  |         \n"
                      "  |          \n"
                      "  |           \n"
                      "__|__\n")

            elif guesses == 3:
                print("   _____ \n"
                      "  |     | \n"
                      "  |     |\n"
                      "  |     | \n"
                      "  |     o  \n"
                      "  |          \n"
                      "  |           \n"
                      "__|__\n")
            
            elif guesses == 4:
                print("   _____ \n"
                      "  |     | \n"
                      "  |     |\n"
                      "  |     | \n"
                      "  |     o  \n"
                      "  |     |   \n"
                      "  |           \n"
                      "__|__\n")

            elif guesses == 5:
                print("   _____ \n"
                      "  |     | \n"
                      "  |     |\n"
                      "  |     | \n"
                      "  |     o  \n"
                      "  |    /|   \n"
                      "  |           \n"
                      "__|__\n")

            elif guesses == 6:
                print("   _____ \n"
                      "  |     | \n"
                      "  |     |\n"
                      "  |     | \n"
                      "  |     o  \n"
                      "  |    /|\   \n"
                      "  |           \n"
                      "__|__\n")

            elif guesses == 7:
                print("   _____ \n"
                      "  |     | \n"
                      "  |     |\n"
                      "  |     | \n"
                      "  |     o  \n"
                      "  |    /|\   \n"
                      "  |    /      \n"
                      "__|__\n")


            elif guesses == 8:
                print("   _____ \n"
                      "  |     | \n"
                      "  |     |\n"
                      "  |     | \n"
                      "  |     o  \n"
                      "  |    /|\   \n"
                      "  |    / \     \n"
                      "__|__\n")
        
        # if the user input was found in the secret word:  
        else:
            if found == True:
                print("Nice Guess!")

    # add the user input to the used letter list
    # convert the list of bad guesses into string       
    usedList.append(letter.lower())
    badGuessesStr = "".join(badGuesses)
    
    print()
    print("Your bad guesses so far: {}".format(badGuessesStr))
    print("You have {} guess(es) left".format(8 - guesses))

# If there are still any _ after 8 guesses, then the player lost, else they win
if guesses >= 8 or "_" in dashes:
    print("Sorry, you lost!")
else:
    print(" ".join(listForDisplay))
    print("Congratulations!")
    print("You figured that the word is '"+encryptedWord+"' with only {} wrong guesses!".format(guesses))