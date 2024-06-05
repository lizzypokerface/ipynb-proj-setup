import pytest

from my_project.classroom.classroom import (
    Student,
    Teacher,
    Classroom,
    TooManyStudentsException,
)

"""
ChatGPT 3.5 Prompt: 
Using pytest and its functionalities such as fixtures, parametrize, raises,
and mark, test the following code. Theme the test names and messages after Harry Potter.
Attach: <classroom.py>
"""


# Fixtures
@pytest.fixture
def harry_potter_classroom():
    teacher = Teacher("Albus Dumbledore")
    students = [Student(name) for name in ["Harry Potter", "Hermione Granger", "Ron Weasley"]]
    return Classroom(teacher, students, "Defense Against the Dark Arts")


@pytest.fixture
def new_teacher():
    return Teacher("Minerva McGonagall")


@pytest.fixture
def new_student():
    return Student("Draco Malfoy")


# Parametrized Test
@pytest.mark.parametrize("student_name", [
    "Neville Longbottom",
    "Luna Lovegood",
    "Ginny Weasley"
])
def test_add_student(harry_potter_classroom, student_name):
    student = Student(student_name)
    harry_potter_classroom.add_student(student)
    assert student in harry_potter_classroom.students, f"{student_name} should be in the classroom"


def test_add_student_exception(harry_potter_classroom):
    for i in range(7):
        harry_potter_classroom.add_student(Student(f"Student {i}"))

    with pytest.raises(TooManyStudentsException):
        harry_potter_classroom.add_student(Student("Overflow Student"))


def test_remove_student(harry_potter_classroom):
    harry_potter_classroom.remove_student("Ron Weasley")
    student_names = [student.name for student in harry_potter_classroom.students]
    assert "Ron Weasley" not in student_names, "Ron Weasley should have been removed from the classroom"


def test_change_teacher(harry_potter_classroom, new_teacher):
    harry_potter_classroom.change_teacher(new_teacher)
    assert harry_potter_classroom.teacher.name == "Minerva McGonagall", "Teacher should have been changed to Minerva McGonagall"


# Marked Test
@pytest.mark.xfail
def test_remove_nonexistent_student(harry_potter_classroom):
    harry_potter_classroom.remove_student("Tom Riddle")
    student_names = [student.name for student in harry_potter_classroom.students]
    assert "Tom Riddle" not in student_names, "Tom Riddle should not be in the classroom since they were never added"
