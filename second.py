# Шифр перестановки
# Рівень 1: Проста перестановка з ключем "SECRET"
def simple_transposition_encrypt(text, key):
    columns = len(key)
    rows = -(-len(text) // columns)

    grid = ['' for _ in range(columns)]
    for i, char in enumerate(text.replace(" ", "").upper()):
        grid[i % columns] += char

    ordered_columns = sorted(range(len(key)), key=lambda k: key[k])
    return ''.join([grid[i] for i in ordered_columns])


def simple_transposition_decrypt(ciphertext, key):
    columns = len(key)
    rows = -(-len(ciphertext) // columns)

    ordered_columns = sorted(range(len(key)), key=lambda k: key[k])
    column_lengths = [len(ciphertext) // columns + (1 if i < len(ciphertext) % columns else 0) for i in range(columns)]

    grid = ['' for _ in range(columns)]
    idx = 0
    for col in ordered_columns:
        grid[col] = ciphertext[idx:idx + column_lengths[col]]
        idx += column_lengths[col]

    plaintext = ''.join([grid[i][j] for j in range(rows) for i in range(columns) if j < len(grid[i])])
    return plaintext


plaintext = "THE ARTIST IS THE CREATOR"
key = "SECRET"
encrypted_text = simple_transposition_encrypt(plaintext, key)
decrypted_text = simple_transposition_decrypt(encrypted_text, key)

print("Encrypted:", encrypted_text)
print("Decrypted:", decrypted_text)



# Рівень 2: Подвійна перестановка з ключами "SECRET" та "CRYPTO"
key1 = "SECRET"
key2 = "CRYPTO"
encrypted_once = simple_transposition_encrypt(plaintext, key1)
encrypted_twice = simple_transposition_encrypt(encrypted_once, key2)

decrypted_once = simple_transposition_decrypt(encrypted_twice, key2)
decrypted_twice = simple_transposition_decrypt(decrypted_once, key1)

print("Double Encrypted:", encrypted_twice)
print("Double Decrypted:", decrypted_twice)
