class Database:
    def __init__(self, criteria, element):
        self._criteria = criteria
        self._element = element

    def read_data(self):
        user_list = []
        if element in criteria:
            user_list.append(user)
        print(list(user_list))

    def write_data(self):
        return element


class Data(Database):
    def __int__(self, _user):
        self.user = user

    def __init__(self, country, name, age, gender, height, weight):
        self._country = country
        self.__name = name
        self.age = age
        self._gender = gender
        self._height = height
        self._weight = weight


user1 = Data(country="USA", name="Ann", age=25, gender='Female', height=160, weight=60)
user = user1
element = user.__dict__.get('age')
user.write_data()
crit = dict(age1=25, age2=30)
criteria = list(crit.values())
c = Database(criteria, element)
c.read_data()
