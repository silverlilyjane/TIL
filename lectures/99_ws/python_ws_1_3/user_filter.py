def over_18(user_list) :
    return [user for user in user_list if user['age'] >= 18]

def is_active_true(user_list) :
    return [user for user in user_list if user['is_active'] == True]


def over18_activeTrue(user_list):
    return [user for user in user_list if user['is_active'] == True and user['age'] >= 18]