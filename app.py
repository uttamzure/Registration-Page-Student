from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Database configuration
db_config = {
    'host': 'localhost',   # ✅ FIXED
    'user': 'uttam',
    'password': '1234',
    'database': 'studentsdb'
}

@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        course = request.form['course']
        address = request.form['address']
        contact = request.form.get('contact')  # ✅ SAFE

        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        query = '''
        INSERT INTO students (name, email, phone, course, address, contact)
        VALUES (%s, %s, %s, %s, %s, %s)
        '''
        values = (name, email, phone, course, address, contact)

        cursor.execute(query, values)
        conn.commit()

        cursor.close()
        conn.close()

        return 'Student Registered Successfully!'
    return render_template('index.html')

@app.route('/students')
def students():
    return render_template('students.html', data=students_data)

if __name__ == "__main__":
    app.run(debug=True)