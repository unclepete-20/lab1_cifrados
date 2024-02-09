from collections import Counter

# Read the Spanish frequency file and construct the frequency list
frequency_list = {}
with open("sp_frequencies.txt", "r") as file:
    next(file)  # Skip the header line
    for line in file:
        letter, percentage = line.strip().split("\t")
        frequency_list[letter.lower()] = float(percentage[:-1])  # Remove the percentage sign and convert to float

# Alphabet
alphabet = 'abcdefghijklmnñopqrstuvwxyz'

def caesar_decrypt(word, displacement):
    return ''.join([alphabet[(alphabet.index(x) - displacement) % len(alphabet)] if x in alphabet else x for x in word.lower()])

def calculate_distribution(word):
    word = word.lower()
    letter_count = Counter(word)
    total_letters = sum(letter_count.values())
    distribution = {letter: (letter_count[letter] / total_letters) * 100 if total_letters > 0 else 0 for letter in alphabet}
    return distribution

def read_cipher_text(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip()

# Read the cipher text from cipher1.txt
cipher_text = read_cipher_text("cipher1.txt")

# Calculate distribution of letters in the cipher text
cipher_distribution = calculate_distribution(cipher_text)

# Find the most frequent letter in the cipher text and the frequency list
most_frequent_cipher = max(cipher_distribution, key=cipher_distribution.get)
most_frequent_list = max(frequency_list, key=frequency_list.get)

# Find the displacement needed to decrypt the cipher text
displacement = abs(alphabet.index(most_frequent_cipher) - alphabet.index(most_frequent_list))

# Decrypt the cipher text using the displacement
decrypted_text = caesar_decrypt(cipher_text, displacement)

# Calculate the distribution of letters in the decrypted text
decrypted_distribution = calculate_distribution(decrypted_text)

# Calculate the distance between the decrypted distribution and the frequency list
distance = sum((decrypted_distribution[letter] - frequency_list[letter])**2 for letter in alphabet)

# Save analysis results to a text file
with open("analysis_results_caesar.txt", "w") as result_file:
    result_file.write("Analysis Results:\n\n")
    result_file.write(f"The best key (or displacement) for Caesar decryption is: {displacement}\n")
    result_file.write(f"Decrypted Text:\n{decrypted_text}\n")
    result_file.write(f"Distance between decrypted distribution and frequency list: {distance}\n\n")
    result_file.write("Frequency Table for Cipher Text:\n")
    result_file.write("Letter  |  Frequency\n")
    for letter, frequency in sorted(cipher_distribution.items()):
        result_file.write(f"{letter.upper():<7} |  {frequency:.2f}%\n")
    result_file.write("\nFrequency Table for Decrypted Text:\n")
    result_file.write("Letter  |  Frequency\n")
    for letter, frequency in sorted(decrypted_distribution.items()):
        result_file.write(f"{letter.upper():<7} |  {frequency:.2f}%\n")

print("Analysis results saved to 'analysis_results_caesar.txt'")

