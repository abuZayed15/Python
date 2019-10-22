uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

new_sentence = ""
shift_value = 7


userInput = input("Write something to encrypt: ")

#check and print section
for x in userInput:
    location = 0
    if x == " ":
        new_sentence = new_sentence + ''.join(" ")
    else:
        if x in str(lowercase): # x = P
            location = lowercase.index(x) # 24, returns the position of y
            i = lowercase[(location + shift_value) %26] # returns the letter f
            new_sentence = new_sentence + ''.join(i)
        elif x in str(uppercase):
            location = uppercase.index(x) # 15, returns the position of P
            i = uppercase[(location + shift_value) %26] # returns the letter f
            new_sentence = new_sentence + ''.join(i)
    
print(new_sentence)

