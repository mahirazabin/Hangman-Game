import java.util.Random;
import java.util.Scanner;


public class assignment3 {
   

    public class Main {
        static pickRandomWord() {
            List words = Collections.word()
            
            with open('lexicon.txt', 'r') as file:
                line = file.readline()
                while line:
                    # arrange the words into a dictionary
                    words.append(line.replace("\n","".strip()))
                    line = file.readline()
            # pick a random index
            # index = random.randint(1,len(words))
            index = random.randint(1,10)
            choice = words[index]
            return choice
        }
      }


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
while count != 0 and guesses < 8:

    found = False
    # display current state of dashes/letters
    print(" ".join(listForDisplay))
    # take user input
    letter = input("Guess your letter: ")

    if letter.lower() in usedList:
        print("You already guessed that letter!")
    else:
        for i in range(0,len(encryptedWord)):
            if letter.lower() == encryptedWord[i]:
                found = True
                listForDisplay[i]=letter.lower()
                count -= 1 

        if found == False: 
            badGuesses.append(letter)
            badGuesses.append(" ")      
            guesses +=1
            print()
            print("Sorry, there is no '" + letter +"'")
            
        else:
            if found == True:
                print("Nice Guess!")
            
    usedList.append(letter.lower())
    badGuessesStr = "".join(badGuesses)
    
    print()
    print("Your bad guesses so far: {}".format(badGuessesStr))
    print("You have {} guesses left".format(8 - guesses))


if guesses >= 8 or "_" in dashes:
    print("Sorry, you lost!")
else:
    # for i in dashes:
    #     if i != "_":
    #         game = True
    # if game == True:
    print(" ".join(listForDisplay))
    print("Congratulations!")
    print("You figured that the word is '"+encryptedWord+"' with only {} wrong guesses!".format(guesses))












    
}
