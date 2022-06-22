from glob import glob
from operator import ne


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
UserInput = input("Type encode to encrpyt, decode to decrypt\n").lower()
text = input("Type in the word to encode \n")
text = list(text.lower())
cipher=int(input("Type in cypher number\n"))
    
def encode ():
    global text
    global cipher
    for letter in text:
        index = alphabet.index(letter)
        # print(index)
        userindex = text.index(letter)
        # print(userindex)
        newindex = index+cipher
        # print(newindex)
        newletter = alphabet[newindex]
        text[userindex] = newletter

def decode():
    global text
    global cipher
    for letter in text:
        index = alphabet.index(letter)
        # print(index)
        userindex = text.index(letter)
        if(index>cipher):
            newindex = index-cipher
            newletter = alphabet[newindex]
        else:
            newindex = cipher-index
            newletter = alphabet[newindex]
        text[userindex] = newletter

if (UserInput=="encode"):
    encode()
if (UserInput=="decode"):
    decode()
print(text)