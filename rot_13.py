base = ['A','B','C','D','E','F','G','H','I','J','K','L',
    'M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

newMessage = []


while True:
    print(" ")
    prompt = input(" Press 'Y' if you want to encrypt a message\n Press 'N' if you want to decrypt a message\n Press 'Q' if you want to exit\n ")
    if prompt.upper() == 'Y':
            messageInput = input(" Please enter the message you want to encrypt: ")
            for i in messageInput.upper():
                if i in base:
                    basePos = base.index(i)
                    newMessage.append(base[basePos-13])
                else:
                    newMessage.append(' ')
            printString = ''.join([str(item) for item in newMessage])
            print("Your encrypted message is: " + printString)
    elif prompt.upper() == "N":
        print(prompt + "is")

    else:
        print("no choice selected")
        break
    # rot 13 isnt actually a good cihper because you can apply the
    # same exact algorithm used to encrypt it to decrypt it
