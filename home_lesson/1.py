friends_names = ['Аня', 'Коля', 'Лёша', 'Лена', 'Миша']
friends_cities = ['Владивосток', 'Красноярск', 'Москва', 'Обнинск', 'Чебоксары']

# Объявлен пустой словарь, его нужно будет наполнить элементами, 
# каждый из которых составлен по схеме "имя: город"
friends =  {}

# Допишите ваш код сюда
for friends_names,friends_cities in friends.items():
    
    friends.update(friends_names,friends_cities)
    


print(friends)