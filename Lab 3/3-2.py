alphabet = "AĂÂBCDEFGHIÎJKLMNOPQRSȘTȚUVWXYZ"
alphabet_length = len(alphabet)


def sanitize_input(message):
    message = message.replace(" ", "").upper()
    for char in message:
        if char not in alphabet:
            raise ValueError(
                "Invalid character detected. Please enter only Romanian letters."
            )
    return message


def vigenere_encrypt(message, key):
    encrypted_text = ""
    key_length = len(key)
    for i in range(len(message)):
        char_index = alphabet.index(message[i])
        key_index = alphabet.index(key[i % key_length])
        encrypted_char = alphabet[(char_index + key_index) % alphabet_length]
        encrypted_text += encrypted_char
    return encrypted_text


def vigenere_decrypt(ciphertext, key):
    decrypted_text = ""
    key_length = len(key)
    for i in range(len(ciphertext)):
        char_index = alphabet.index(ciphertext[i])
        key_index = alphabet.index(key[i % key_length])
        decrypted_char = alphabet[(char_index - key_index) % alphabet_length]
        decrypted_text += decrypted_char
    return decrypted_text


if __name__ == "__main__":
    choice = input("Choose operation (encrypt/decrypt): ").lower()
    if choice not in ["encrypt", "decrypt", "e", "d"]:
        print("Invalid choice!")
    else:
        key = sanitize_input(input("Enter the key (min 7 characters): "))
        if len(key) < 7:
            print("Key must be at least 7 characters long.")
        elif choice == "encrypt" or "e":
            message = sanitize_input(input("Enter the message: "))
            print("Encrypted message:", vigenere_encrypt(message, key))
        else:
            ciphertext = sanitize_input(input("Enter the ciphertext: "))
            print("Decrypted message:", vigenere_decrypt(ciphertext, key))
