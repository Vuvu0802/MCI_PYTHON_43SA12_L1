class Student:
    def __init__(self, student_code, name):
        self.student_code = student_code
        self.name = name

    def update_student_name(self, name):
        self.name = name


class StudentManager:
    def __init__(self):
        self.student_list = []

    def add_student(self, student):
        self.student_list.append(student)
        return student

    def delete_student(self, student_code):
        for student in self.student_list:
            if student_code == student.student_code:
                self.student_list.remove(student)
                return student.student_code, student.name
            else:
                return None

    def update_student(self, student_code, student_name):

        for student in self.student_list:
            if student_code == student.student_code:
                student.update_student_name(student_name)
                return student.name

    def list_all_students(self):
        for student in self.student_list:
            print(f'Student code: {student.student_code}, student name: {student.name}')


if __name__ == '__main__':

    student_1 = Student(1, 'Nguyen Manh Truong')
    student_2 = Student(2, 'La Ton Huy')
    student_3 = Student(3, 'Minh Hieu')
    student_4 = Student(4, 'Nguyen Dat')
    student_5 = Student(5, 'Vu My Linh')
    student_6 = Student(6, 'Ngoc Nguyen')
    student_7 = Student(7, 'Hoang Pham')
    student_8 = Student(8, 'Long Aiden')

    student_manager = StudentManager()
    student_manager.add_student(student_1)
    student_manager.add_student(student_2)
    student_manager.add_student(student_3)
    student_manager.add_student(student_4)
    student_manager.add_student(student_5)
    student_manager.add_student(student_6)
    student_manager.add_student(student_7)
    student_manager.add_student(student_8)

    student_manager.list_all_students()
    print('-'*100)
    student_manager.delete_student(1)
    student_manager.list_all_students()
    print('-' * 100)

    student_manager.update_student(6, 'Nguyen Anh Ngoc')
    student_manager.list_all_students()

    print('DONE')
