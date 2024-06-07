import logging

# Configure logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)


class TooManyStudentsException(Exception):
    pass


class Person:
    def __init__(self, name):
        self.name = name
        logger.debug(f"Person created with name: {name}")


class Teacher(Person):
    def __init__(self, name):
        super().__init__(name)
        logger.debug(f"Teacher created with name: {name}")


class Student(Person):
    def __init__(self, name):
        super().__init__(name)
        logger.debug(f"Student created with name: {name}")


class Classroom:
    def __init__(self, teacher, students, course_title):
        self.teacher = teacher
        self.students = students
        self.course_title = course_title
        logger.debug(
            f"Classroom created with teacher: {teacher.name}, "
            f"{len(students)} students, course title: {course_title}"
        )

    def add_student(self, student):
        logger.debug(f"Adding student: {student.name} to the classroom")
        if len(self.students) < 10:
            self.students.append(student)
            logger.info(f"Student {student.name} added to the classroom")
        else:
            logger.error(f"Cannot add student {student.name}: Too many students")
            raise TooManyStudentsException(
                "Cannot add more than 10 students to a classroom"
            )

    def remove_student(self, name):
        logger.debug(f"Removing student with name: {name} from the classroom")
        for student in self.students:
            if student.name == name:
                self.students.remove(student)
                logger.info(f"Student {name} removed from the classroom")
                break
        else:
            logger.warning(f"Student with name: {name} not found in the classroom")

    def change_teacher(self, new_teacher):
        logger.debug(f"Changing teacher from {self.teacher.name} to {new_teacher.name}")
        self.teacher = new_teacher
        logger.info(f"Teacher changed to {new_teacher.name}")
