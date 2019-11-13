import unittest
import sqlite3
from HW11_Ejona_Kocibelli import Student, Instructor, Repository, Major


class TestContainer(unittest.TestCase):
    def setUp(self):
        self.test_path = r"C:\Users\Ejona's Surface\PycharmProjects\Homework 11"
        self.repo = Repository(self.test_path, False)

    def test_instructor_pretty_table(self):
        """verify that instructor_pretty_table get the right information and prints out the right information from the
                instructor.txt file"""
        result1 = []
        for instructor in self.repo._instructors.values():
            for row in instructor.instructor_info():
                result1.append(row)

        actual1 = [('98764', 'Cohen, R', 'SFEN', 'CS 546', 1),
                   ('98763', 'Rowland, J', 'SFEN', 'SSW 810', 4),
                   ('98763', 'Rowland, J', 'SFEN', 'SSW 555', 1),
                   ('98762', 'Hawking, S', 'CS', 'CS 501', 1),
                   ('98762', 'Hawking, S', 'CS', 'CS 546', 1),
                   ('98762', 'Hawking, S', 'CS', 'CS 570', 1)]

        self.assertEqual(result1, actual1)

    def test_student_pretty_table(self):
        """verify that student_pretty_table get the right information and prints out the right information from the
        students.txt file"""
        result = [student.student_info() for student in self.repo._students.values()]
        actual = [['10103', 'Jobs, S', 'SFEN', {'SSW 810', 'CS 501'}, {'SSW 540', 'SSW 555'}, None],
                  ['10115', 'Bezos, J', 'SFEN', {'SSW 810'}, {'SSW 540', 'SSW 555'}, {'CS 546', 'CS 501'}],
                  ['10183', 'Musk, E', 'SFEN', {'SSW 810', 'SSW 555'}, {'SSW 540'}, {'CS 546', 'CS 501'}],
                  ['11714', 'Gates, B', 'CS', {'CS 570', 'SSW 810', 'CS 546'}, None, None],
                  ['11717', 'Kernighan, B', 'CS', None, {'CS 570', 'CS 546'}, {'SSW 810', 'SSW 565'}]]

        self.assertEqual(result, actual)

    def test_major_pretty_table(self):
        """verify that major_pretty_table get the right information and prints out the right information from the
        majors.txt file"""
        result2 = [major.major_info() for major in self.repo._majors.values()]
        actual2 = [['SFEN', {'SSW 555', 'SSW 540', 'SSW 810'}, {'CS 501', 'CS 546'}],
                   ['CS', {'CS 570', 'CS 546'}, {'SSW 565', 'SSW 810'}]]
        self.assertEqual(result2, actual2)

    def test_instructor_table_db(self):
        """verify that instructor_table_db get the right information from the database and prints out the right
        information from the database tables"""
        dbpath = r"C:\Users\Ejona's Surface\PycharmProjects\Homework 11\810_startup.db"
        db = sqlite3.connect(dbpath)
        result3 = []
        query = """select i.CWID, i.Name, i.Dept, g.Course, count(*) as students
                   from instructors i join grades g on i.CWID = g.InstructorCWID
                   group by i.Name, i.Dept, g.Course"""
        for row in db.execute(query):
            result3.append(row)

        actual3 = [('98764', 'Cohen, R', 'SFEN', 'CS 546', 1),
                   ('98762', 'Hawking, S', 'CS', 'CS 501', 1),
                   ('98762', 'Hawking, S', 'CS', 'CS 546', 1),
                   ('98762', 'Hawking, S', 'CS', 'CS 570', 1),
                   ('98763', 'Rowland, J', 'SFEN', 'SSW 555', 1),
                   ('98763', 'Rowland, J', 'SFEN', 'SSW 810', 4)]

        self.assertEqual(result3, actual3)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
