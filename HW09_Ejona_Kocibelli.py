from prettytable import PrettyTable
from collections import defaultdict
import os


class Student:
    student_fields = ['Student Id', 'Student Name', 'Student Major', 'Courses']

    def __init__(self, cwid, name, major):
        """Initiliaze student id, name, major and a container of courses and grades"""
        self._cwid = cwid
        self._name = name
        self._major = major
        self._courses_taken = defaultdict(str)  # key: course, value: grade

    def add_course(self, course, grade):
        """Allows other classes to add a course and grade to the container of courses and grades"""
        self._courses_taken[course] = grade

    def student_info(self):
        """Returns the summary data about a single student needed in the pretty table"""
        return [self._cwid, self._name, self._major, sorted(self._courses_taken.keys())]


class Instructor:
    instructor_fields = ['Instructor Id', ' Instructor Name', 'Department', 'Course', 'Number of Students']

    def __init__(self, cwid, name, dept):
        """Initiliaze instructor id, name, department and a container of courses courses taught"""
        self._cwid = cwid
        self._name = name
        self._dept = dept
        self._courses_taught = defaultdict(int)  # key: course value: number of students

    def add_course(self, course):
        """Allows other classes to specify a course, and updates the container of courses taught to increment the number
         of students by 1"""
        self._courses_taught[course] += 1

    def instructor_info(self):
        """Returns information needed by the Instructor prettytable"""
        for course, nr_course in self._courses_taught.items():
            yield self._cwid, self._name, self._dept, course, nr_course


class Repository:
    def __init__(self, dir_path, doprint=True):
        """Initialize the path, student repository container, instructor repository container, and initialize the
        functions read_students, read_instructors, read_grades"""
        self._dir_path = dir_path
        self._students = dict()  # key: student_id value: Instance of class Student
        self._instructors = dict()  # key: instructor_id value: Instance of class Instructor
        self.grades = list()
        self.read_student()
        self.read_instructor()
        self.read_grades()
        if doprint:
            print(self.student_pretty_table())
            print(self.instructor_pretty_table())

    def read_student(self):
        """Read the students.txt file, creating a new instance of class Student for each line in the file, and add the
        new Student to the repository's container with all students."""
        try:
            for cwid, name, major in file_reading_gen(os.path.join(self._dir_path, "students.txt"), 3, '\t', False):
                if cwid in self._students:
                    raise ValueError(f"Student id: {cwid} is already in file")
                else:
                    self._students[cwid] = Student(cwid, name, major)
        except FileNotFoundError:
            raise FileNotFoundError(f"{os.path.join(self._dir_path, 'students.txt')} cannot open.")

    def read_instructor(self):
        """Read the instructiors.txt file, creating a new instance of class Instructor for each line in the file, and
        add the new Instructor to the repository's container with all instructors."""
        try:
            for cwid, name, dept in file_reading_gen(os.path.join(self._dir_path, "instructors.txt"), 3, '\t', False):
                if cwid in self._instructors:
                    raise ValueError(f"{cwid} already in file")
                else:
                    self._instructors[cwid] = Instructor(cwid, name, dept)
        except FileNotFoundError:
            raise FileNotFoundError(f"{os.path.join(self._dir_path, 'instructors.txt')} cannot open.")

    def read_grades(self):
        """Read the grades.txt file, check if the student_id exists, and if the instructor_id exists and add course and
        grade to students repository, add the course and increment the number of students at instructors repository"""
        try:
            for cwid_st, course, grade, cwid_in in file_reading_gen(os.path.join(self._dir_path, "grades.txt"), 4, '\t',
                                                                    False):
                if cwid_st not in self._students:
                    raise ValueError(f"Student with id: {cwid_st} not exist")
                elif cwid_in not in self._instructors:
                    raise ValueError(f"Instructor with id: {cwid_in} not exist")
                else:
                    self._students[cwid_st].add_course(course, grade)
                    self._instructors[cwid_in].add_course(course)
        except FileNotFoundError:
            raise FileNotFoundError(f"{os.path.join(self._dir_path, 'grades.txt')} cannot open.")

    def student_pretty_table(self):
        """print a student prettytable"""
        pt = PrettyTable(field_names=Student.student_fields)
        for student in self._students.values():
            pt.add_row(student.student_info())
        return pt

    def instructor_pretty_table(self):
        """print an instructor prettytable"""
        pt = PrettyTable(field_names=Instructor.instructor_fields)
        for instructor in self._instructors.values():
            for row in instructor.instructor_info():
                pt.add_row(row)
        return pt


def file_reading_gen(path, fields, sep=',', header=True):
    """Function file_reading_gen reads a file path, fields, separator and header and returns the values of the fields
    in the file if the fields given is equal to fields number in file """
    try:
        fp = open(path, 'r')
    except FileNotFoundError:
        raise FileNotFoundError(f"Can't open {path}")
    else:
        with fp:
            for counter, line in enumerate(fp):
                line = line.rstrip('\n')
                tokens = line.split(sep)
                if fields != len(tokens):
                    raise ValueError(f"{os.path.basename(path)} has {len(tokens)} fields on line {counter + 1}"
                                     f" but expected {fields} ")
                elif header and counter == 0:
                    continue
                else:
                    yield tuple(tokens)


def main():
    stevens = Repository(r"C:\Users\Ejona's Surface\PycharmProjects\Homework 9")


if __name__ == '__main__':
    main()
