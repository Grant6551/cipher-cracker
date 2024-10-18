
width = 80

print('\n')
print('--------------------- Welcome To Caesar Cipher Decrypting Tool ----------------------'.center(width))
print('\n')
print(r'[%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%|------------|%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%]'.center(width))
print(r'[%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%| $S`?a,     |%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%]'.center(width))
print(r'[%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%|       `?a, |%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%]'.center(width))
print(r'[ .------ . .---..   ..----  .----:   .-----  .---. .---. .----- |  /  .---- .---. ]'.center(width))
print(r'[ |       | |___||__ ||____  | ,,,;   |       | ,,; |___| |      |-@_  |____ | ,,; ]'.center(width))
print(r'[ |______ | |    |   ||____  |  \     |_____  |  \  |   | |_____ |   \ |____ |  \  ]'.center(width))
print(r'[%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%|------------|%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%]'.center(width))
print(r'[%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%| _____ _____|%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%]'.center(width))
print(r'[%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\_____ ____/ %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%]'.center(width))
print(r'[%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%]'.center(width))
print(r'[---------------------------------------------------------------------- bY z3r0_c001]'.center(width))
print('\n')

mode = 'Decrypt'

# Ask user for message and key, with centered text and custom prompt
print('-' * width)
print(f'Enter your Message to {mode}:'.center(width))
print('-' * width)
# Message input prompt
message = input('$Decryptor> ')
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Loop through every possible key
for key in range(len(LETTERS)):

    # Reset translated for each key
    translated = ''

    # Decryption code on each symbol in the message
    for symbol in message.upper():
        if symbol in LETTERS:
            # Get the number of the symbol
            num = LETTERS.find(symbol)
            num = num - key

            # Handle the wrap-around if num is less than 0
            if num < 0:
                num = num + len(LETTERS)

            # Add the decrypted letter to the translated message
            translated = translated + LETTERS[num]
        else:
            # Just add the symbol without decrypting (like spaces or punctuation)
            translated = translated + symbol

    # Display the current key being tested, along with its decryption, centered
    print('-' * width)
    print(f'Key #{key}: {translated}'.center(width))
    print('-' * width)
