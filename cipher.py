from glob import glob
from operator import ne


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
UserInput = input("Type in the word to encode \n")
UserInput = list(UserInput.lower())
print(UserInput)
cipher=int(input("Type in cypher number\n"))
    
def encode ():
    global UserInput
    global cipher
    for letter in UserInput:
        index = alphabet.index(letter)
        print(index)
        userindex = UserInput.index(letter)
        print(userindex)
        newindex = index+cipher
        print(newindex)
        newletter = alphabet[newindex]
        UserInput[userindex] = newletter

def decode():
    global UserInput
    global cipher
    for letter in UserInput:
        index = alphabet.index(letter)
        print(index)
        userindex = UserInput.index(letter)
        if(index>cipher):
            newindex = index-cipher
            newletter = alphabet[newindex]
        else:
            newindex = cipher-index
            newletter = alphabet[newindex]
        UserInput[userindex] = newletter

#encode()
decode()
print(UserInput)