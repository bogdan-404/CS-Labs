def caesar_cipher(input_text, key, operation):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    if key < 1 or key > 25:
        return 'Key must be between 1 and 25 inclusive.'

    modified_text = ''.join(input_text.split()).upper()
    result = ''

    for char in modified_text:
        if char in alphabet:
            index = alphabet.index(char)
            if operation == 'E':
                new_index = (index + key) % 26
            elif operation == 'D':
                new_index = (index - key + 26) % 26
            result += alphabet[new_index]
        else:
            return 'Only English alphabet characters (A-Z) are allowed!'

    return result


operation = input(
    'Enter operation (E - encrypt/D - decrypt): ').strip().upper()
key_input = input('Enter the key (1-25): ').strip()

try:
    key = int(key_input)
    if key < 1 or key > 25:
        print('Invalid key. Key must be between 1 and 25.')
    elif key == 0:
        print('Result: No encryption/decryption needed.')
    else:
        message = input('Enter message: ')
        result = caesar_cipher(message, key, operation)
        print(f'Result: {result}')
except ValueError:
    print('Invalid key. Key must be an integer value between 1 and 25.')
