# my_student = {
#     'name':'Rolf Smith',
#     'grades':[70,88,90,99],
#     'average': 80,# something here, 
# }

# def average_grade(student):
#     return sum(student['grades']) / len(student['grades'])

# # class Student:
# #     def __init__(self, new_name, new_grade):
# #         self.name = new_name
# #         self.grades = new_grade

# #     def average(self):
# #         return sum(self.grades) / len(self.grades)
    
# student_one = Student('Rolf Smith', [70, 88, 90, 99])
# student_two = Student('Jose Valdez', [75, 88, 96, 100])

# print(student_one.grades[3])

# class Movie:
#     def __init__(self, title, director):
#         self.title = title
#         self.director = director
#     def print_info(self):
#         print(f"<<{self.title}>> by {self.director}")

# movie_1 = Movie('Speed Racer','Wachowski')
# movie_2 = Movie('Fellowship of the Ring','Peter Jackson')

# movie_1.print_info()
# movie_2.print_info()

# '''
# __init__ is for making a new dictionary
# __class__ gets the item's 

# int makes an integer
# str makes a string
# sum adds together a list
# print puts shit in the terminal
# range does a bunch of numbers?
# len gets the length of stuff
# max gets the highest number in a list
# min gets the lowest number in a list
# round rounds a decimal to an int. .5 goes up. 


# I need to learn dictionaries vs objects. 

# '''


class Movie:
    def __init__(self, name, year):
        self.name = name
        self.year = year
    def print_info(self):
        print(f"<<{self.name}>> by {self.year}")

class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def __getitem__(self, i):
        return self.cars[i]

    def __repr__(self):
        return f'<Garage {self.cars}>'

    def __str__(self):
        return f'Garage with {len(self)} cars.'

ford = Garage()
ford.cars.append('Fiesta')
ford.cars.append('Mustang')
ford.cars.append('Truck')
print(ford[1])

for car in ford:
    print(car)

print(ford)

class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary

    def average(self):
        return sum(self.marks) / len(self.marks)
    
    @property
    def weekly_salary(self):
        return self.salary * 37.5

rolf = WorkingStudent('Rolf', 'MIT', 15.50)
print('{:.2f}'.format(rolf.salary))
rolf.marks.append(57)
rolf.marks.append(99)
print(rolf.average())
print(rolf.weekly_salary)

class Foo:
    @classmethod
    def hi(cls):
        print(cls.__name__)

my_object = Foo()
my_object.hi()

class Bar:
    @staticmethod
    def hi():
        print('Hello, I don\'t take parameters.')

another_object = Bar()
another_object.hi()

class FixedFloat:
    def __init__(self, amount):
        self.amount = amount

    def __repr__(self):
        return f'<FixedFloat {self.amount:.2f}>'
    
    @staticmethod # typically not useful!
    def from_sum(value1, value2):
        return FixedFloat(value1 + value2)

number = FixedFloat(18.5746)
new_number = number.from_sum(19.575, 0.789)
print(new_number)

class Euro(FixedFloat):
    def __init__(self, amount):
        super().__init__(amount)
        self.symbol = "€"
    
    def __repr__(self):
        return f'<Euro {self.symbol}{self.amount:>2f}'

money = Euro(18.76)
print(money)