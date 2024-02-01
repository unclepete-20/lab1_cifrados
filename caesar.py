'''
Nombre: Pedro Arriola
Carnet: 20188
'''

import string

def caesar_encrypt(text, displacement):
    text = text.upper()
    alphabet = list(string.ascii_uppercase) + ['Ñ']
    return ''.join([alphabet[(alphabet.index(char) + displacement) % 27] if char in alphabet else char for char in text])

def caesar_decrypt(cyphered_text, displacement):
    cyphered_text = cyphered_text.upper()
    alphabet = list(string.ascii_uppercase) + ['Ñ']
    return ''.join([alphabet[(alphabet.index(char) - displacement) % 27] if char in alphabet else char for char in cyphered_text])

# Texto plano original
text_test = 'HELLOWY! HOLA7'
# Desplazamiento para el cifrado César
displacement_test = 3

# Cifrado del texto plano utilizando el cifrado César
new_text = caesar_encrypt(text_test, displacement_test)
print("Texto cifrado con cifrado César:", new_text)

# Texto cifrado esperado
cyphered_expected = 'KHÑÑRZB! KRÑD7'

# Descifrado del texto cifrado utilizando el cifrado César
decyphered = caesar_decrypt(cyphered_expected, displacement_test)
print("Texto descifrado con cifrado César:", decyphered)

