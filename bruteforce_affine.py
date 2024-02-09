import math
from collections import Counter

# Alphabet
alphabet = 'abcdefghijklmnñopqrstuvwxyz'
alphabet_list = list(alphabet)

def affine_decrypt(word, a_value, b_value):
    decrypted = []
    word = list(word.lower())
    for x in word:
        if x in alphabet_list:
            index = alphabet_list.index(x)
            if math.gcd(a_value, len(alphabet_list)) == 1:
                a_inverse = pow(a_value, -1, len(alphabet_list))
                position = int((a_inverse * (index - b_value)) % len(alphabet_list))
            else:
                # If 'a' is not coprime, use a different logic
                position = int((a_value * (index - b_value)) % len(alphabet_list))
            decrypted.append(alphabet_list[position])
        else:
            decrypted.append(x)
    decrypted = "".join(decrypted)
    return decrypted

def calculate_distribution(word):
    word = word.lower()
    letter_count = Counter(word)
    total_letters = sum(letter_count.values())
    distribution = {letter: (letter_count[letter] / total_letters) * 100 if total_letters > 0 else 0 for letter in alphabet}
    return distribution

def read_cipher_text(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip()

# Read the cipher text from cipher2.txt
cipher_text = read_cipher_text("cipher2.txt")

# Brute force for affine encryption
best_result = None
best_key = None
best_distribution = None

for a in range(1, 27):
    for b in range(27):
        result = affine_decrypt(cipher_text, a, b)
        distribution = calculate_distribution(result)
        # Check if this result is better than the previous best
        if best_result is None or distribution['e'] > best_distribution['e']:
            best_result = result
            best_key = (a, b)
            best_distribution = distribution

# Save the best result, key, and distribution to a text file
with open("analysis_results_affine.txt", "w") as file:
    file.write(f"Best Key: {best_key}\n")
    file.write(f"Best Decrypted Text:\n{best_result}\n\n")
    file.write("Frequency Distribution:\n")
    for letter, frequency in best_distribution.items():
        file.write(f"{letter}: {frequency:.2f}%\n")

print("Analysis results saved to 'analysis_results_affine.txt'")