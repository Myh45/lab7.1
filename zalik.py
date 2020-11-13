class Student:
    def __init__(self, name, zalik):
        self.name = name
        self.__zalik = zalik

    def __str__(self):
        return str(self.name) + " : " + str(self.__zalik)

    def set(self, value):
        if value <= 2:
            self.__zalik = 'ne zarah'
        else:
            self.__zalik = 'zarah'

    def get(self):
        return str(self.name) + " : " + str(self.__zalik)


s1 = Student('Taras', None)
s1.set(3.6)
print(s1.get())