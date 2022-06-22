from glob import glob
from operator import ne


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
UserInput = input("Type encode to encrpyt, decode to decrypt\n").lower()
text = input("Type in the word. \n")
text = list(text.lower())
cipher=int(input("Type in cypher number\n"))

def caeser(start_text, shift_amount, cipher_direction):
    end_text=""
    if(cipher_direction=="decode"):
            shift_amount=shift_amount*-1
    for letter in start_text:
        index = alphabet.index(letter)
        newindex=index+shift_amount
        end_text=end_text+alphabet[newindex]
    return end_text


print(caeser(text,cipher,UserInput))