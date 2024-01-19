class Person:
    nationality = 'Japan'

    def say_hello(self):
        print(f'こんにちは、私の国籍は{self.nationality}です')

Person = Person()
Person.nationality

print(Person.say_hello())