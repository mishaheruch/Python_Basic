class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.gender},{self.age},{self.first_name},{self.last_name}"


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{self.gender},{self.age},{self.first_name},{self.last_name},{self.record_book}"


class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= 10:
            raise MyError("Досягнути максимальне число студентів в групі.")
        self.group.add(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = ""
        for student in self.group:
            all_students += str(student) + "\n"
        return f"Number:{self.number}\n {all_students} "


class MyError(Exception):
    pass


st1 = Student("Male", 30, "Steve", "Jobs", "AN142")
st2 = Student("Female", 25, "Liza", "Taylor", "AN145")
gr = Group("PD1")
gr.add_student(st1)
gr.add_student(st2)

try:
    for i in range(10):
        gr.add_student(Student("Male", 20, f"Student{i}", f"LastName{i}", f"AN{i}"))
except MyError as e:
    print(f"Помилка: {e}")

print(gr)
assert str(gr.find_student("Jobs")) == str(st1), "Test1"
assert gr.find_student("Jobs2") is None, "Test2"
assert (
    isinstance(gr.find_student("Jobs"), Student) is True
), "Метод пошуку повинен повертати екземпляр"

gr.delete_student("Taylor")
print(gr)  # Only one student

gr.delete_student("Taylor")  # No error!
