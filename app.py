from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="internship_tracker"
)

cursor = db.cursor()

@app.route('/')
def index():
    cursor.execute("SELECT * FROM applications")
    data = cursor.fetchall()
    return render_template("index.html", applications=data)

@app.route('/add', methods=['GET','POST'])
def add():
    if request.method == 'POST':
        company = request.form['company']
        status = request.form['status']
        notes = request.form['notes']

        sql = "INSERT INTO applications (company_name,status,notes) VALUES (%s,%s,%s)"
        val = (company,status,notes)

        cursor.execute(sql,val)
        db.commit()

        return redirect('/')

    return render_template("add.html")

if __name__ == "__main__":
    app.run(debug=True)