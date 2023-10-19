from src.auth.authenticator import Authenticator
from src.policy.reference_monitor import ReferenceMonitor
from src.utils.inputhandler import handle_input

while True:
    username = input('enter your username\n')
    password = input('enter password\n')

    if Authenticator.login(username, password):
        print('login successful')

        current_user = Authenticator.get_current_user(username, password)

        entity_type = input('what is your entity type: account or record\n')
        operation_type = input('what is you operation type: r for read, w for write, d for delete\n')

        if ReferenceMonitor.has_access(current_user['user_type'], entity_type, operation_type):
            print('you have access')

            handle_input(current_user, entity_type, operation_type)

        else:
            print('access denied! sorry!')

    else:
        print('login error! program stopped!')
    print('==================================')
