import re
import sys
import os
import time

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_validated_cpf():
    while True:
        # Main function to validate a CPF entered by the user
        cpf = input('Enter your CPF in the following format: [xxx.xxx.xxx-xx]: ')
        cpf_user = re.sub(r'[^0-9]', '', cpf)  # Collects only numbers and ignores the rest (spaces, commas, dots, etc)
        
        # Checks if the user entered repeated commands
        cpf_sequential = cpf == cpf[0] * len(cpf)
        
        if cpf_sequential:
            print('You entered sequential data.')
            sys.exit()

        # Validating the last 10th digit
        nine_digits = cpf_user[:9]
        counter_1 = 10
        result_digit_1 = 0
        
        for digit in nine_digits:
            result_digit_1 += int(digit) * counter_1
            counter_1 -= 1

        digit_1 = (result_digit_1 * 10) % 11
        digit_1 = digit_1 if digit_1 <= 9 else 0
        
        # Validating the last 11th digit
        ten_digits = nine_digits + str(digit_1)
        counter_2 = 11
        result_digit_2 = 0
        
        for digit in ten_digits:
            result_digit_2 += int(digit) * counter_2
            counter_2 -= 1
        
        digit_2 = (result_digit_2 * 10) % 11
        digit_2 = digit_2 if digit_2 <= 9 else 0
    
        cpf_validated = f'{nine_digits}{digit_1}{digit_2}'
        
        # Comparing the original CPF with the calculated CPF
        
        if cpf_user == cpf_validated:
            cpf_formatted = f'{cpf_user[:3]}.{cpf_user[3:6]}.{cpf_user[6:9]}-{cpf_user[9:]}'
            print(f'The CPF: {cpf_formatted} is valid')
        else:
            print('Invalid CPF')
            continue
        
        run_again = input('Do you want to validate another CPF? Type (Y)es to continue or any letter to exit: ')
        if run_again.strip().lower() != 'y' and run_again.strip().lower() != 'yes' and run_again.strip().lower() != 's' and run_again.strip().lower() != 'sim':
            print('Exiting')
            sys.exit()
        time.sleep(0.1)
        clear_terminal()
# Start of code execution
get_validated_cpf()