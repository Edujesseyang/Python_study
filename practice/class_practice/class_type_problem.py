# ===============================================
# class problem, Module 9
# Create a student class. The class should have an init function and member variables:
# first_name, last_name, id, courses. Classes should be a dictionary that maps a course id to a list containing course name,
# grade as percentage float, and grade as string letter (i.e. B+). Percentage float should be rounded to 2 decimal places.
# Solution:
class Student:
    def __init__(self, first_name, last_name, id):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id
        self.courses = []
        self.grade = ""
        self.gpa = 0.0
        self.info = {}

    def get_info(self):
        self.info = {
            "First name": self.first_name,
            "Last name": self.last_name,
            "ID": self.id,
            "Course": self.courses,
            "Grade": self.grade,
            "GPA": self.gpa
        }
        return self.info

    def print_info(self):
        '''No return'''
        print(f'{self.last_name}, {self.first_name}:\n ID:   {self.id}\n Course:   {self.courses}\n   Grade:{self.grade}\n   GPA: {self.gpa}')

    def add_courses(self):
        '''No input, No return'''
        self.input = (input("Enter your courses: "))
        while self.input != "":
            self.input = (input("Enter your courses: "))
            self.courses.append(self.input)
        self.courses.pop()
        self.grade = input("Enter your grade: ")
        valid = False
        while valid == False:
            try:
                self.gpa = float(input("Enter your GPA: "))
                valid = True
            except ValueError:
                print("Invalid GPA.")


'''Create student_1'''
student_1 = Student("Jesse", "Yang", 20545215)
student_1.add_courses()

'''TEST'''
print(student_1.get_info())
student_1.print_info()

# ===================================================
