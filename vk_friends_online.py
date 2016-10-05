import vk

"""
# чтобы получить app_id, нужно зарегистрировать своё приложение на
 https://vk.com/dev\
"""
APP_ID = -1


def get_user_login():
    return str(input("Введите Логин (VK.com): "))


def get_user_password():
    return str(input("Введите Пароль (VK.com): "))


def get_online_friends_in_all(list_friends):
    return [user for user in list_friends if user['online'] != 0]


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        user_login=login,
        user_password=password
    )
    api = vk.API(session)
    list_friends = api.friends.get(fields='last_name, first_name')
    return get_online_friends_in_all(list_friends)


def output_friends_to_console(friends_online):
    for friend in friends_online:
        print("%s %s" % (friend['first_name'], friend['last_name']))

if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)
