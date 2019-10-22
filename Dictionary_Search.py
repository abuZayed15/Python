""""
@author: Abu Zayed
@Name: Dictionary search using data.json 
""""
import json
import difflib
from difflib import SequenceMatcher

userInput = ""
count = 0

while userInput != "y":
    count = count + 1

    #ToDo: Find meaning of word from data.json file
    data = json.load(open("data.json")) # putting the json data inside variable data
    
    #ToDo: The user enters a word, converts to small letter and then searchs
    userInput = input("Enter word: ").lower() 

    if userInput in data:
        sanitizedWord = difflib.get_close_matches(userInput, data.keys())
        print(f"{sanitizedWord} is sanitized word")
        for word in sanitizedWord:
            if userInput == word:
                print(data[userInput])
            break
    

    # comparing userInput to key inside json
    #loop through the keys in the dictionary
    for char in data.keys(): 
        if char in userInput: #checking to see if key is similar to user input
            sequence = SequenceMatcher(None, userInput, char).ratio()
            if sequence == 1.0:
                lenVal = len(data[char])
                for x in data[char]:
                    print(str(data[char]).replace(', ',',\n*****\n'))
            elif sequence > 0.75 and sequence < 0.9:
                clarityInput = input(f"Did you mean {char} instead? Enter Y if yes, or N if no: ")
                if clarityInput == "Y".lower():
                    print(data[char])
                elif clarityInput == "N".lower():
                    print("input inner if not in data")
            elif sequence < 0.0:
                print("Invalid input")
       

     


    #ToDo: If word not found print friendly error
    # if userInput in data:
    #     print(data[userInput])
    #elif userInput not in data: 
    # elif userInput not in data and clarityInput:
    #     print("Invalid input")


    #exit check
    if userInput == "quit now":
        clarityInput = input("Are you sure you want to exit?(Y/N): ").lower()
        if clarityInput == "Y".lower():
            break

#ToDo: If word found the meaning is shown. 
#Word can have more than one meaning. So it should show all the meanings.
#Delimiters between meanings


#ToDo:If the word has a spelling mistake then the dictionary suggests the closest word 
# and ask the user if this is what they are looking for

#
