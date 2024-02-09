import re

# Function to decrypt ciphertext using Vigenère decryption
def vigenere_decrypt(ciphertext, keyword):
    decrypted_text = ""
    keyword_length = len(keyword)
    keyword_index = 0

    for char in ciphertext:
        if char.isalpha():
            shift = (ord(char) - ord(keyword[keyword_index % keyword_length])) % 26
            decrypted_text += chr((ord('A') + shift) if char.isupper() else (ord('a') + shift))
            keyword_index += 1
        else:
            decrypted_text += char
    
    return decrypted_text

# Function to calculate similarity score between two texts
def calculate_similarity(text1, text2):
    # Remove non-alphabetic characters and convert to lowercase
    clean_text1 = re.sub(r'[^a-zA-Z]', '', text1.lower())
    clean_text2 = re.sub(r'[^a-zA-Z]', '', text2.lower())
    
    # Calculate similarity score (Jaccard similarity coefficient)
    intersection = len(set(clean_text1) & set(clean_text2))
    union = len(set(clean_text1) | set(clean_text2))
    similarity_score = intersection / union if union > 0 else 0
    
    return similarity_score


def bruteforce_vigenere(ciphertext):
    best_decryption = ""
    best_keyword = ""
    best_similarity = 0

    for keyword_length in range(1, len(ciphertext) + 1):
        for keyword_start in range(len(ciphertext) - keyword_length + 1):
            keyword = ciphertext[keyword_start:keyword_start + keyword_length]
            decrypted_text = vigenere_decrypt(ciphertext, keyword)
            similarity_score = calculate_similarity(ciphertext, decrypted_text)

            if similarity_score > best_similarity:
                best_similarity = similarity_score
                best_decryption = decrypted_text
                best_keyword = keyword
    
    return best_decryption, best_keyword, best_similarity

# Read ciphertext from cipher3.txt file
file_path = "cipher3.txt"
with open(file_path, 'r') as file:
    ciphertext = file.read().strip()

# Perform brute-force attack on Vigenere cipher to find the best decryption
best_decryption, best_keyword, best_similarity = bruteforce_vigenere(ciphertext)

# Write the best decryption, keyword, and similarity score to a text file
with open("analysis_results_vigenere.txt", 'w') as output_file:
    output_file.write(f"Best Decryption: {best_decryption}\n")
    output_file.write(f"Keyword: {best_keyword}\n")
    output_file.write(f"Similarity Score: {best_similarity}\n")


print("Analysis results saved to 'analysis_results_vigenere.txt'")
