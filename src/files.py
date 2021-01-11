import csv 
import json
#Part1: parsing file and storing usernames
try:
    compromised_users = []
    with open('passwords.csv') as password_file:
        password_csv = csv.DictReader(password_file)
        for row in password_csv:
            password_row = row
            compromised_users.append(password_row['Username'])

    with open('compromised_users.txt', 'a') as compromised_users_file:
        for user in compromised_users:
            compromised_users_file.write(user)

#Part2: writing a json object to a file
    with open('boss_message.json', 'w') as boss_message:
        boss_message_dict = {'recipient': 'The Boss', 'message': 'Mission Success'}
        json.dump(boss_message_dict, boss_message)

#Part3: writing into file
    with open('passwords.csv', 'w') as new_passwords_obj:
        slash_null_sig = """
  _  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/
"""
    new_passwords_obj.write(slash_null_sig)
except FileNotFoundError:
    print('File Not Found Error')



