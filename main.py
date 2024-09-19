class User:
    def __init__(self, user_id, name, access_level='User'):
        self._user_id = user_id
        self._name = name
        self._access_level = access_level

    # Getters
    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def get_access_level(self):
        return self._access_level

    # Setters
    def set_name(self, name):
        self._name = name

    def set_access_level(self, access_level):
        self._access_level = access_level

    def __repr__(self):
        return f"Пользователь(ID: {self._user_id}, Имя: {self._name}, Уровень доступа: {self._access_level})"


class Admin(User):
    def __init__(self, user_id, name, access_level='Admin'):
        super().__init__(user_id, name, access_level)

    def add_user(self, user_list, new_user):
        if isinstance(new_user, User):
            user_list.append(new_user)
            print(f"Пользователь {new_user.get_name()} добавлен.")
        else:
            print("Недопустимый пользователь, не удается добавить.")

    def remove_user(self, user_list, user_id):
        for user in user_list:
            if user.get_user_id() == user_id:
                user_list.remove(user)
                print(f"Пользователь {user.get_name()} удален.")
                return
        print("Пользователь не найден.")


# Пример использования
user1 = User(1, "Мария")
user2 = User(2, "Иван")
user3 = User(3, "Антон")
user4 = User(4, "Анастасия")


admin1 = Admin(7, "Ольга")
admin2 = Admin(5, "Вадим")

# Список пользователей
user_list = [user1, user2, user3, user4, admin1, admin2]

# Администратор добавляет нового пользователя
new_user = User(6, "Даниил")
admin1.add_user(user_list, new_user)

# Администратор удаляет пользователя
admin2.remove_user(user_list, 2)

# Просмотр списка пользователей
print(user_list)

def print_admins(user_list):
    admins = [user for user in user_list if isinstance(user, Admin)]
    if admins:
        print("Admins:")
        for admin in admins:
            print(admin)
    else:
        print("Не найдены администраторы.")

# Вызов функции для печати администраторов
print_admins(user_list)
