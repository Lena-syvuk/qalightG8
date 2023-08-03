class Human:
    favorite_drink = 'beer'

    def __init__(self, age):
        self.age = age

    def napiy(self):
        print(self.favorite_drink)

    def drink(self):
        if self.age < 18:

            self.favorite_drink = 'juice'
        print(f'{type(self).__name__}likes drink {self.favorite_drink}')

kate = Human(age=50)
kate.napiy()
kate.drink()


class Worker(Human):


    def __init__(self, age, salary):
        super().__init__(age)
        self.salary = salary


    def drink(self):
        if self.salary > 1000:
            self.favorite_drink = 'whiskey'
        super().drink()

stepan = Worker(salary=20000, age=44)
stepan.napiy()
stepan.drink()

