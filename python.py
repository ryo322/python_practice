class Person:
    nationality = 'Japan'

    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f'こんにちは、私の国籍は{self.nationality}です')

    def say_my_name(self):
        print(f'私の名前は{self.name}です。')

A = Person('田中')
A.nationality
A.name

print(A.say_my_name())