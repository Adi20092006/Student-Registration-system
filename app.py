from flask import Flask, render_template, request, redirect, url_for
from database import add_student, get_all_students

app = Flask(__name__)


@app.route("/")
def home():
    # Rendering Home page with route "/"

    return render_template("index.html")


@app.route("/register", methods=["POST"])
def register():
    # Posting the received data from the webpage into database using add_student function

    # Get data entered in the HTML form
    name = request.form["name"]
    roll_no = request.form["roll_no"]
    course = request.form["course"]
    email = request.form["email"]

    # Save data into MySQL
    add_student(name, roll_no, course, email)

    # After saving, redirect to the students page
    return redirect(url_for('students'))


@app.route("/students")
def students():
    # Displaying the data onto the students webpage

    student_list = get_all_students()

    return render_template(
        "students.html",
        students=student_list
    )


if __name__ == "__main__":
    app.run(debug=True)