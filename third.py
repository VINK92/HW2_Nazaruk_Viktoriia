# Табличний шифр
# Рівень 1: Табличний шифр із ключем "MATRIX"
from first import vigenere_cipher


def create_table_cipher(text, key):
    columns = len(key)
    ordered_columns = sorted(range(len(key)), key=lambda k: key[k])

    rows = -(-len(text) // columns)
    grid = ['' for _ in range(columns)]
    for i, char in enumerate(text.replace(" ", "").upper()):
        grid[i % columns] += char

    return ''.join([grid[i] for i in ordered_columns])


plaintext = "THE ARTIST IS THE CREATOR OF BEAUTIFUL THINGS"
key = "MATRIX"
encrypted_text = create_table_cipher(plaintext, key)
print("Encrypted with Table Cipher:", encrypted_text)

# Рівень 2: Комбіноване шифрування

# Віженер
vigenere_key = "CRYPTO"
vigenere_encrypted = vigenere_cipher(plaintext, vigenere_key, mode='encrypt')

# Табличний
table_key = "MATRIX"
combined_encrypted = create_table_cipher(vigenere_encrypted, table_key)

print("Combined Encrypted:", combined_encrypted)
