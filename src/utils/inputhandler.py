from src.database.operations import *
from src.auth.authenticator import encode


def handle_input(current_user, entity_type, operation_type):
    if entity_type == 'account':
        if operation_type == 'r':
            user = get_user(current_user['username'])
            del user['password']
            print(user)
        elif operation_type == 'w':
            username = input('username\n')
            password = input('password\n')
            user_type = input('user_type\n')
            add_user(current_user, {
                'username': username,
                'password': encode(password),
                'user_type': user_type
            })
        elif operation_type == 'd':
            delete_user(current_user['username'])
    elif entity_type == 'record':
        if operation_type == 'r':
            print(read_records(current_user))
        elif operation_type == 'w':
            add_record({
                "id": input('record id\n'),
                "patient_name": input('patient name\n'),
                "sickness_details": input('sickness\n'),
                "doctor": current_user['username'],
                "drug_prescriptions": input('drug description\n'),
                "sensitivity_level": current_user['privilege_level']
            })
        elif operation_type == 'd':
            delete_records(input('record id\n'))
    print('operations completed!')
