my_student = {
    'name':'Rolf Smith',
    'grades':[70,88,90,99],
    'average': 80,# something here, 
}

def average_grade(student):
    return sum(student['grades']) / len(student['grades'])

class Student:
    def __init__(self, new_name, new_grade):
        self.name = new_name
        self.grades = new_grade

    def average(self):
        return sum(self.grades) / len(self.grades)
    
student_one = Student('Rolf Smith', [70, 88, 90, 99])
student_two = Student('Jose Valdez', [75, 88, 96, 100])

print(student_one.grades[3])

class Movie:
    def __init__(self, title, director):
        self.title = title
        self.director = director
    def print_info(self):
        print(f"<<{self.title}>> by {self.director}")

movie_1 = Movie('Speed Racer','Wachowski')
movie_2 = Movie('Fellowship of the Ring','Peter Jackson')

movie_1.print_info()
movie_2.print_info()
