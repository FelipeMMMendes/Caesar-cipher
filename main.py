alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

from art import logo

print(logo)

encryptedWord = []

def caesar(text,shift,direction):
    if direction == 'decode':#se a pessoa quiser decodificar, 
        shift *= -1
    encryptedWord = []
    word = list(text)
    for word in text:
        position = alphabet.index(word)#position recebe a posicao da letra especifica no alfabeto
        ShiftedPosition = position + shift#ShiftedPosition recebe a posição + a marcha
        word = alphabet[ShiftedPosition]# a letra  é trocada pela que esta na posicao que a marcha colocou            
        encryptedWord.append(word)#append coloca a word no final da lista encryptedWord 
    encryptedWord = ''.join(encryptedWord)#esse join serve para transformar a lista em uma string       
    print("The encrypted result is: "+ encryptedWord)     


userAnswer = 'y'

while userAnswer == 'y':
    #lower serve para deixar tudo minusculo
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    direction = direction.lower()

    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if shift>27:
        shift = shift % 27
    caesar(text,shift,direction)

    userAnswer = input("Wanna do it again? (y/n): ")
    userAnswer = userAnswer.lower()
 


