def generate_modified_alphabet(key2):
    key2 = ''.join(sorted(set(key2.upper()), key=key2.upper().index))
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    modified_alphabet = key2 + \
        ''.join(filter(lambda char: char not in key2, alphabet))

    return modified_alphabet


def caesar_cipher(input_text, key1, key2, operation):
    modified_alphabet = generate_modified_alphabet(key2)
    if key1 < 1 or key1 > 25:
        return 'Key must be between 1 and 25 inclusive.'
    modified_text = ''.join(input_text.split()).upper()
    result = ''

    for char in modified_text:
        if char in modified_alphabet:
            index = modified_alphabet.index(char)
            if operation == 'E':
                new_index = (index + key1) % len(modified_alphabet)
            elif operation == 'D':
                new_index = (index - key1 + len(modified_alphabet)
                             ) % len(modified_alphabet)
            result += modified_alphabet[new_index]
        else:
            return 'Only English alphabet characters (A-Z) are allowed!'

    return result


operation = input(
    'Enter operation (E - encrypt/D - decrypt): ').strip().upper()

key1_input = input('Enter key (1-25): ').strip()
key2 = input('Enter key2 (duplicate letters will be removed): ').strip()

try:
    key1 = int(key1_input)
    if key1 < 1 or key1 > 25:
        print('Invalid key. Key must be between 1 and 25.')
    else:
        message = input('Enter message: ')
        result = caesar_cipher(message, key1, key2, operation)
        print(f'Result: {result}')
except ValueError:
    print('Invalid key. Key must be an integer between 1 and 25.')
