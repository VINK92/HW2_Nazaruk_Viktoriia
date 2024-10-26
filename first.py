from collections import Counter
# Шифр Віженера
# Рівень 1: Шифрування та дешифрування за ключем
def vigenere_cipher(text, key, mode='encrypt'):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    key = key.upper()
    result = []

    expanded_key = (key * (len(text) // len(key) + 1))[:len(text)]

    for i, char in enumerate(text.upper()):
        if char in alphabet:
            key_index = alphabet.index(expanded_key[i])
            text_index = alphabet.index(char)
            if mode == 'encrypt':
                shift = (text_index + key_index) % 26
            elif mode == 'decrypt':
                shift = (text_index - key_index) % 26
            result.append(alphabet[shift])
        else:
            result.append(char)

    return ''.join(result)


plaintext = "THE ARTIST IS THE CREATOR OF BEAUTIFUL THINGS"
key = "CRYPTOGRAPHY"
encrypted_text = vigenere_cipher(plaintext, key, mode='encrypt')
decrypted_text = vigenere_cipher(encrypted_text, key, mode='decrypt')

print("Encrypted:", encrypted_text)
print("Decrypted:", decrypted_text)

# Рівень 2: Розшифрування без відомого ключа (Метод Касіскі або тест Фрідмана)

def friedman_test(text):
    n = len(text)
    freq = Counter(text)
    ic = sum(f * (f - 1) for f in freq.values()) / (n * (n - 1))
    estimated_key_length = (0.027 * n) / ((0.065 - ic) + ic * (n - 1))
    return round(estimated_key_length)


encrypted_text = vigenere_cipher(plaintext, key, mode='encrypt')
key_length_estimate = friedman_test(encrypted_text)
print("Estimated Key Length:", key_length_estimate)
