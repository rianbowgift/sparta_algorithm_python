class Person:

    def __init__(self,param_name):
        print("hello",self)
        self.name = param_name

    def talk(self):
        print("재이름은"+ self.name +"입니다")


person_1 = Person("철수")
print(person_1)
person_1.talk()
person_2 = Person("민수")
print(person_2)