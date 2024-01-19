class Kid(Person):
    def say_hello(self, age):
        print(f'私の名前は{self.name}です。年齢は{age}です。')

Kid = Kid('たろう')
Kid.name

print(Kid.say_hello(12))