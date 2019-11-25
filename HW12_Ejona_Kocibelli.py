import sqlite3
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/instructors')
def instructor_summary():
    dbpath = r"C:\Users\Ejona's Surface\Desktop\MyAppDir\810_startup.db"
    try:
        db = sqlite3.connect(dbpath)
    except sqlite3.OperationalError:
        print(f"Error: Unable to open database at {dbpath}")
    else:
        with db:
            query = """select i.CWID, i.Name, i.Dept, g.Course, count(*) as students
                       from instructors i join grades g on i.CWID = g.InstructorCWID
                       group by i.Name, i.Dept, g.Course"""

            data = [{"CWID": CWID, "Name": Name, "Dept": Dept, "Course": Course, "students": students} for
                    CWID, Name, Dept, Course, students in db.execute(query)]

            return render_template('my_program.html', page_title="Stevens Institute of Technology",
                                   title="Stevens Repository", table_title="Instructor's Summary",
                                   instructors=data)


app.run(debug=True)
