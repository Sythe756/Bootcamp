matrix = [
    "7ii",
    "Tsx",
    "h%?",
    "i #",
    "sM ",
    "$a ",
    "#t%",
    "^r!",
]

def decrypt_matrix(matrix):
    columns = [''] * len(matrix[0])
    for row in matrix:
        for i, char in enumerate(row):
            columns[i] += char
    hidden_message = ''
    for col in columns:
        alpha_chars = ''.join(char for char in col if char.isalnum())
        hidden_message += alpha_chars + ' '
    hidden_message = ' '.join(word if word.isalnum() else ' ' for word in hidden_message.split())
    return hidden_message
decrypted_message = decrypt_matrix(matrix)
print(decrypted_message)
