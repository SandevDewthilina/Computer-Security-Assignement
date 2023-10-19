import json


def read_all_records():
    try:
        with open("src/records.json", "r") as json_file:
            data = json.load(json_file)
    except FileNotFoundError:
        data = []
    return data


def add_record(record):
    try:
        with open("src/records.json", "r") as json_file:
            data = json.load(json_file)
    except FileNotFoundError:
        data = []

    data.append(record)

    with open("src/records.json", "w") as json_file:
        json.dump(data, json_file, indent=4)


def read_records(current_user):
    try:
        with open("src/records.json", "r") as json_file:
            data = json.load(json_file)
    except FileNotFoundError:
        data = []

    filtered_data = []
    for record in data:
        if (record['patient_name'] == current_user['username']) or \
                (current_user['user_type'] == 'doctor' and record['doctor'] == current_user['username']):
            filtered_data.append(record)
    return filtered_data


def delete_records(record_id):
    try:
        with open("src/records.json", "r") as json_file:
            data = json.load(json_file)
    except FileNotFoundError:
        data = []

    filtered_data = []
    for record in data:
        if record['id'] is not record_id:
            filtered_data.append(record)

    with open("src/records.json", "w") as json_file:
        json.dump(filtered_data, json_file, indent=4)


def get_user(username):
    try:
        with open("src/users.json", "r") as json_file:
            data = json.load(json_file)
    except FileNotFoundError:
        data = []

    for user in data:
        if user['username'] == username:
            return user


def add_user(current_user, user):
    try:
        with open("src/users.json", "r") as json_file:
            data = json.load(json_file)
    except FileNotFoundError:
        data = []

    if user['user_type'] == 'doctor':
        user['privilege_level'] = 3
    elif user['user_type'] == 'patient':
        user['privilege_level'] = 2
    elif user['user_type'] == 'staff':
        user['privilege_level'] = 1

    if not user['privilege_level'] == current_user['privilege_level']:
        print('permission denied')
        return

    data.append(user)
    with open("src/users.json", "w") as json_file:
        json.dump(data, json_file, indent=4)


def delete_user(username):
    try:
        with open("src/users.json", "r") as json_file:
            data = json.load(json_file)
    except FileNotFoundError:
        data = []

    filtered_data = []
    for user in data:
        if not user['username'] == username:
            filtered_data.append(user)

    with open("src/users.json", "w") as json_file:
        json.dump(filtered_data, json_file, indent=4)


def read_all_users():
    try:
        with open("src/users.json", "r") as json_file:
            data = json.load(json_file)
    except FileNotFoundError:
        data = []
