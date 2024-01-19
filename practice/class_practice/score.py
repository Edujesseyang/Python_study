def main():
    classList = ["math", "calc", "english"]
    S = Student("Sam", classList)
    S.search("CIS 40")
    S.display()  # Renamed the print method to display
    S.class_count()


class Student:
    def __init__(self, name, classList):
        self.name = name
        self.classList = classList

    def search(self, className):
        found_bool = 0
        for classes in self.classList:
            if classes == className:
                print("found")
                found_bool = 1
        if found_bool == 0:
            print("not found")

    def display(self):  # Renamed the print method to display
        print(f'Name: {self.name}: ')
        print("Classes:")
        for classes in self.classList:
            print(classes)

    def class_count(self):
        count = len(self.classList)
        print(f'The student is enrolled in {count} classes.')


# Calling the main function
main()
