class Database:

    def read_data(self, user_el):
        criteria = list(dict(age1=25, age2=30).values())
        user_el = user_el
        data_list = []
        for c in criteria:
            for u in user_el:
                if u.__dict__.get('age') == c:
                    data_list.append(u)
        print(data_list)

    def write_data(self, element):

        users_el = []
        users_el.append(element)
        return users_el


class Data:

    def __init__(self, country, name, age, gender, height, weight):
        self.country = country
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height
        self.weight = weight


dtbs = Database()
user1 = Data(country="USA", name="Ann", age=25, gender='Female', height=160, weight=60)
user2 = Data(country="USA", name="Mike", age=42, gender='Male', height=182, weight=90)
user3 = Data(country="GB", name="John", age=30, gender='Male', height=170, weight=81)
user4 = Data(country="PRC", name="Ju", age=25, gender='Female', height=152, weight=51)

users = [user1, user2, user3, user4]

for u in users:
    dtbs.write_data(u)

dtbs.read_data(user_el=[])
