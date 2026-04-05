from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

db_config = {
    'host': 'localhost',
    'user': 'uttam',
    'password': 'Uttam@123',
    'database': 'studentsdb'
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add_student():
    name = request.form['name']
    email = request.form['email']
    course = request.form['course']
    address = request.form['address']
    phone = request.form['phone']
    

    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    query = '''
    INSERT INTO students (name, email, course, address, phone)
    VALUES (%s, %s, %s, %s, %s)
    '''
    values = (name, email, course, address, phone)

    cursor.execute(query, values)
    conn.commit()

    cursor.close()
    conn.close()

    return redirect('/students')

@app.route('/students')
def students():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template('students.html', students=data)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)