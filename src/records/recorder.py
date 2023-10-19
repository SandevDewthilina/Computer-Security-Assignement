from src.database.operations import add_record


class Recorder:

    @staticmethod
    def create_record(user, record):
        record['sensitivity_level'] = user['privilege_level']
        add_record(record)
