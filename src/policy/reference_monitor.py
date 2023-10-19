#           records accounts
# doctor    r,w,d   r,w,d
# patient   r,d     r,w,d
# staff     w       r,w,d
access_control_matrix = [['rwd', 'rwd'], ['rd', 'rwd'], ['w', 'rwd']]


class ReferenceMonitor:
    # entity_type = record/account
    # operation_type = r,w,d
    @staticmethod
    def has_access(user_type, entity_type, operation_type):
        col_num = 1 if entity_type == 'account' else 0
        row_num = 0 if user_type == 'doctor' else 1 if user_type == 'patient' else 2
        return operation_type in access_control_matrix[row_num][col_num]
