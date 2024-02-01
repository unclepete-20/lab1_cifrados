'''
Nombre: Pedro Arriola
Carnet: 20188
'''

def mod_inverse(a, m):
    return next((x for x in range(1, m) if (a * x) % m == 1), None)

def affine_encrypt(text, key):
    a, b = key
    return ''.join([chr(((a * (ord(char) - ord('A')) + b) % 27) + ord('A')) if char.isalpha() else char for char in text.upper()])

def affine_decrypt(ciphertext, key):
    a, b = key
    a_inv = mod_inverse(a, 27)
    if a_inv is None:
        return "Clave 'a' no válida. No tiene inverso modular."
    return ''.join([chr(((a_inv * (ord(char) - ord('A') - b)) % 27) + ord('A')) if char.isalpha() else char for char in ciphertext.upper()])

# Prueba del cifrado afín
plaintext_afin = 'HELLOWORLD! 123'
key_afin = (5, 8)
encrypted_afin = affine_encrypt(plaintext_afin, key_afin)
print("Texto cifrado con cifrado afín:", encrypted_afin)

# Prueba del descifrado afín
decrypted_afin = affine_decrypt(encrypted_afin, key_afin)
print("Texto descifrado con cifrado afín:", decrypted_afin)
