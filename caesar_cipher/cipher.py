from caesar_cipher.is_english import count_words

def encrypt(plaintext, key):
    ciphertext = ""

    for word in plaintext:
        if word.isalpha():
            if word.islower():
                encrypt_word = chr((ord(word) - ord('a') + key)% 26 + ord('a'))
            else:
                encrypt_word = chr((ord(word) - ord('A') + key) % 26 +ord('A'))
        else:
            encrypt_word = word
        ciphertext += encrypt_word

    return ciphertext


def encrypt():
    pass

def crack():
    pass

