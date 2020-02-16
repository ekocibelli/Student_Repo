FIRST DELIVERY: 

You've been hired by Stevens Institute of Technology to create a data repository of courses, students, and instructors.  The system will be used to help students track their required courses, the courses they have successfully completed, their grades,  GPA, etc.  The system will also be used by faculty advisors to help students to create study plans.  We will continue to add new features to this solution over the coming weeks so you'll want to think carefully about a good design and implementation. Your assignment this week is to begin to build the framework for your project and summarize student and instructor data.  You'll need to download three ascii, tab separated,  data files:
  1. students.txt (available from Canvas): Provides information about each student
  2. instructors.txt (available from Canvas):Provides information about each instructor
  3. grades.txt (available from Canvas): Specifies the student CWID, course, and grade for that course, and the instructor CWID.
  
Your assignment is to read the data from each of the three files and store it in a data structure that is easy to process to meet the following requirements:
Your solution should allow a single program to create repositories for different sets of data files, e.g. one set of files for Stevens, another for Columbia University, and a third for NYU. Each university will have different directories of data files.   Hint: you should define a class to hold all of the information for a specific university.
You may hardcode the names of each of the required "students.txt", "instructors.txt", and "grades.txt" files.   Your solution should accept the directory path where the three data files exist so you can easily create multiple sets of input files for testing.
Use your file reader generator from HW08 to read the students, instructors, and grades files into appropriate data structures or classes.
Use PrettyTable to generate and print a summary table of all of the students with their CWID, name, and a sorted list of the courses they've taken (as specified in the grades.txt file).  
Use PrettyTable to generate and print a summary table of each of the instructors who taught at least one course with their CWID, name, department, the course they've taught, and the number of students in each class. 
Implement automated tests to verify that the data in the prettytables matches the data from the input data files. 
You do NOT need to implement automated tests to catch all possible error conditions but your program should print relevant error messages when invalid or missing data is detected.
Your solution MAY print error messages and warnings to the user about inconsistent or bad data, e.g. a data file with the wrong number of fields or a grade for an unknown student or instructor.

SECOND DELIVERY:

This week you'll continue to add new features to data repository you created last week. One of the most popular features is knowing what classes have been completed when signing up for classes for next semester.  However, users point out that it would be nice if your system also reported the remaining required courses.
Each major has a set of required courses that are required of all students.  Furthermore, a student must earn a grade of at least a 'C' for a course to count toward graduation.  (Valid grades include 'A', 'A-', 'B+', 'B', 'B-', 'C+', and 'C') Any student earning less than a 'C' must repeat the course until earning at least a 'C'.
Along with a set of required courses that every student must complete successfully, each major defines a set of electives and each student must successfully at least one of the electives associated with that major.  Students may take more than one elective, but they must take at least one of the electives associated with their major.
As frequently happens in real life, the format of the data files has changed since last week.  You'll need to download new copies of the data files from Canvas. Good thing you used your file_reading_gen() from HW08 which makes it trivial for you to read the new data files with their new formats and possible headers.   If you didn't use your file_reading_gen(), then you should refactor your code to make use of your file_reading_gen() function.
You'll need to read the information about majors and use it to update your students summary table to add columns for "Remaining Required" and "Remaining electives" and then calculate the required courses that each student must take to graduate along with the remaining electives.  Note that students must take all of the required courses and at least one of the electives to graduate.
You should also include a new summary prettytable of majors including the name of the major, the required courses, and elective courses.

THIRD DELIVERY: 

Create a new SQLite database.
Use DataGrip to open your new SQLite database and import the four files into your database as separate tables. The files have a header row with the column names and the fields are separated by tabs. 
Run queries to answer the following questions.  
What is the name of the instructor with CWID='98763' 
What is the total number of instructors by department? 
What is the most frequent grade across all students and courses?
Show the student's name, CWID, and major along with the courses and grades each student received in that course for all grades. 
Show the names of students  who have grades for  'SSW 810'.  
Recreate the Instructor summary table from HW10, including the Instructor's CWID, name, department, course taught, and the number of students who took the course

FOURTH DELIVERY:

The Stevens community is very excited about the work you've been doing to gather information about students, classes, and instructors.  Your work is so popular that the community is asking for a website so everyone can see the results.
Your assignment is build a new web page to display a summary of each Instructor with her CWID, Name, Department, Course, and the number of students in the course.
Create a directory structure for your solution with a 'templates' subdirectory, and a base.html template.
Define a query using your SQLite database from Homework 11 that calculates the CWID, Name, Department, Course, and number of students.   The example from the lecture may be useful for this task.
Create a new template file for your new web page.  Start by understanding how it should look and then perhaps create an HTML with static data to test your HTML.
Update your static HTML to include Jinja2 variables and statements to use data passed with the render_template() call.
Create a Flask Python application to run your application.
Demonstrate that your code works properly by submitting a .zip file with all of the files from your solution plus a screen dump of your browser showing the output.
Update your GitHub repository to include a new branch with the web solution. 
