import gspread

# url_sheets = https://docs.google.com/spreadsheets/d/10_NKQaFogN7w-CsRfhMqflC2-NiKWuYb_T5z2PRqmzE/edit#gid=0

# Basics variables
password = input('Введите пароль: ')
step = int(input('Введите шаг: '))
alphabet = "ABCDEFGHabcdeQRfghijklmnoIJKLMNpqr09stuOPSvwxyzTU876qrstuvwxyz54321VWXYZABCDEFGHIJKabcdeijklmnopLMNOPQfghRSTU09876u54321VWXYZ0987654321"

# Passwords
enc_pass = []
decr_pass = []

# Gspread variables
access = gspread.service_account(filename='cryptopy-418507-a5fe8e4b47d7.json') # Key for Googlesheets
open_table = access.open("CryptoPy")
open_worksheet = open_table.get_worksheet(0)
previous_password_value = open_worksheet.cell(1, 2).previous_password_value # Previous password value
next_crypt = previous_password_value + '__' + password # Encrypted password + password

# Check step
if step > 11:
    print('Такой шаг нельзя, нужно меньше')
elif (step < 1):
    print('Такой шаг нельзя, нужно больше')

#Main functions
def encrypted_password(password_stirng):
    for char in password_stirng:
        if char in alphabet:
            char_search = alphabet.find(char)
            enc_pass.append(alphabet[char_search+step])
        elif char not in alphabet:
            enc_pass.append(char)
encrypted_password(next_crypt)

def decryption_password(password_stirng):
    for char in password_stirng:
        if char in alphabet:
            char_search = alphabet.find(char)
            decr_pass.append(alphabet[char_search-step])
        elif char not in alphabet:
            decr_pass.append(char)
decryption_password(enc_pass)

# Push in Googlesheets
open_worksheet.update_cell(1, 2, ''.join(enc_pass))
open_worksheet.update_cell(2, 2, ''.join(decr_pass))