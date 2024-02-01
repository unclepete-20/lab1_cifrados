'''
Nombre: Pedro Arriola
Carnet: 20188
'''

def vigenere_encrypt(plaintext, keyword):
    keyword = keyword.upper()
    return ''.join([chr(((ord(char) - ord('A') + ord(keyword[i % len(keyword)]) - ord('A')) % 27) + ord('A')) if char.isalpha() else char for i, char in enumerate(plaintext.upper())])

def vigenere_decrypt(ciphertext, keyword):
    keyword = keyword.upper()
    return ''.join([chr(((ord(char) - ord('A') - (ord(keyword[i % len(keyword)]) - ord('A'))) % 27) + ord('A')) if char.isalpha() else char for i, char in enumerate(ciphertext.upper())])

# Prueba del cifrado Vigenère
plaintext_vigenere = 'HELLOWORLD! 123'
keyword_vigenere = 'KEY'
encrypted_vigenere = vigenere_encrypt(plaintext_vigenere, keyword_vigenere)
print("Texto cifrado con cifrado Vigenère:", encrypted_vigenere)

# Prueba del descifrado Vigenère
decrypted_vigenere = vigenere_decrypt(encrypted_vigenere, keyword_vigenere)
print("Texto descifrado con cifrado Vigenère:", decrypted_vigenere)
