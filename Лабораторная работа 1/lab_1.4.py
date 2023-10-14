users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']
number_users = len(users)
usersU = set(users)
U_visit = len(usersU)
visits = {"Общее количество": 0, "Уникальные посещения": 0}
visits["Общее количество"] = number_users
visits["Уникальные посещения"] = U_visit
print(visits)
# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
