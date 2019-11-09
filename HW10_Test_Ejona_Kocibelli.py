import unittest
from HW10_Ejona_Kocibelli import Student, Instructor, Repository, Major


class TestContainer(unittest.TestCase):
    def setUp(self):
        self.test_path = r"C:\Users\Ejona's Surface\PycharmProjects\ssw810"
        self.repo = Repository(self.test_path, True)

    def test_instructor_pretty_table(self):
        """verify that instructor_pretty_table get the right information and prints out the right information from the
                instructor.txt file"""
        result1 = []
        for instructor in self.repo._instructors.values():
            for row in instructor.instructor_info():
                result1.append(row)

        actual1 = [('98765', 'Einstein, A', 'SFEN', 'SSW 567', 4),
                   ('98765', 'Einstein, A', 'SFEN', 'SSW 540', 3),
                   ('98764', 'Feynman, R', 'SFEN', 'SSW 564', 3),
                   ('98764', 'Feynman, R', 'SFEN', 'SSW 687', 3),
                   ('98764', 'Feynman, R', 'SFEN', 'CS 501', 1),
                   ('98764', 'Feynman, R', 'SFEN', 'CS 545', 1),
                   ('98763', 'Newton, I', 'SFEN', 'SSW 555', 1),
                   ('98763', 'Newton, I', 'SFEN', 'SSW 689', 1),
                   ('98760', 'Darwin, C', 'SYEN', 'SYS 800', 1),
                   ('98760', 'Darwin, C', 'SYEN', 'SYS 750', 1),
                   ('98760', 'Darwin, C', 'SYEN', 'SYS 611', 2),
                   ('98760', 'Darwin, C', 'SYEN', 'SYS 645', 1)]

        self.assertEqual(result1, actual1)

    def test_student_pretty_table(self):
        """verify that student_pretty_table get the right information and prints out the right information from the
        students.txt file"""
        result = [student.student_info() for student in self.repo._students.values()]
        actual = [['10103', 'Baldwin, C', 'SFEN', {'SSW 567', 'SSW 687', 'SSW 564', 'CS 501'}, {'SSW 555', 'SSW 540'},
                   None], ['10115', 'Wyatt, X', 'SFEN', {'SSW 567', 'CS 545', 'SSW 687', 'SSW 564'},
                           {'SSW 555', 'SSW 540'}, None], ['10172', 'Forbes, I', 'SFEN', {'SSW 567', 'SSW 555'},
                                                           {'SSW 564', 'SSW 540'}, {'CS 513', 'CS 545', 'CS 501'}],
                  ['10175', 'Erickson, D', 'SFEN',
                   {'SSW 567', 'SSW 687', 'SSW 564'}, {'SSW 555', 'SSW 540'}, {'CS 513', 'CS 545', 'CS 501'}],
                  ['10183', 'Chapman, O', 'SFEN', {'SSW 689'}, {'SSW 567', 'SSW 555', 'SSW 564', 'SSW 540'},
                   {'CS 513', 'CS 545', 'CS 501'}], ['11399', 'Cordova, I', 'SYEN', {'SSW 540'},
                                                     {'SYS 612', 'SYS 800', 'SYS 671'}, None],
                  ['11461', 'Wright, U', 'SYEN',
                   {'SYS 611', 'SYS 750', 'SYS 800'}, {'SYS 612', 'SYS 671'}, {'SSW 565', 'SSW 810', 'SSW 540'}],
                  ['11658', 'Kelly, P', 'SYEN', None, {'SYS 612', 'SYS 800', 'SYS 671'},
                   {'SSW 565', 'SSW 810', 'SSW 540'}], ['11714', 'Morton, A', 'SYEN', {'SYS 611', 'SYS 645'},
                                                        {'SYS 612', 'SYS 800', 'SYS 671'},
                                                        {'SSW 565', 'SSW 810', 'SSW 540'}],
                  ['11788', 'Fuller, E', 'SYEN', {'SSW 540'}, {'SYS 612', 'SYS 800', 'SYS 671'}, None]]
        self.assertEqual(result, actual)

    def test_major_pretty_table(self):
        """verify that major_pretty_table get the right information and prints out the right information from the
        majors.txt file"""
        result2 = [major.major_info() for major in self.repo._majors.values()]
        actual2 = [['SFEN', {'SSW 540', 'SSW 567', 'SSW 555', 'SSW 564'}, {'CS 513', 'CS 545', 'CS 501'}],
                  ['SYEN', {'SYS 612', 'SYS 671', 'SYS 800'}, {'SSW 565', 'SSW 810', 'SSW 540'}]]
        self.assertEqual(result2, actual2)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)