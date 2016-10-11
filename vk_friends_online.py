import vk
import getpass


APP_ID = 5134149


def get_user_login():
    return input("Введите Логин (VK.com): ")


def get_user_password():
    return getpass.getpass(prompt="Введите Пароль (VK.com): ")


def get_online_friends(login, password):
    session = vk.AuthSession(
        app_id=APP_ID,
        scope='friends',
        user_login=login,
        user_password=password
    )
    api = vk.API(session)
    list_friends = api.friends.getOnline()
    return api.users.get(user_ids=str(list_friends).strip('[]'))


def output_friends_to_console(friends_online):
    for friend in friends_online:
        print("%s %s" % (friend['first_name'], friend['last_name']))

if __name__ == '__main__':
    login = get_user_login()
    password = get_user_password()
    friends_online = get_online_friends(login, password)
    output_friends_to_console(friends_online)
