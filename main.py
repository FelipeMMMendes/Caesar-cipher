alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#lower serve para deixar tudo minusculo
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
direction = direction.lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 

encryptedWord = []
def encrypt(text, shift):
    word = list(text)
    for word in text:
        position = alphabet.index(word)#position recebe a posicao da letra especifica no alfabeto
        ShiftedPosition = position + shift#ShiftedPosition recebe a posição + a marcha
        word = alphabet[ShiftedPosition]# a letra  é trocada pela que esta na posicao que a marcha colocou            
        encryptedWord.append(word)#append coloca a word no final da lista encryptedWord

encrypt(text,shift)#chama a funcao encrypt, passando os parametros coletados la atras

encryptedWord = ''.join(encryptedWord)#transforma a Lista encryptedWord em uma String encryptWord
print(encryptedWord)
