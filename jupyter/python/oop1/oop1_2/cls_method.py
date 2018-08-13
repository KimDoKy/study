class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def init_from_string(cls, string):
        '''
        string format: '<name>_<age>'
        '''
        name, age = string.split('_')
        return cls(name, int(age))

if __name__ == '__main__':
    p = Person.init_from_string('greg_30')
    print(p.name)
    print(p.age)
