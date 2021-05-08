# app.py
# KELOMPOK 1 ARM 2 (CATUR WARDANA, YEYEN KARUNIA, BAGUS SADEWA, AKBAR HENDRAWAN)
from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from flask_mysqldb import MySQL, MySQLdb
import bcrypt
import json
import random, datetime, time




app = Flask(__name__)
app.config['SECRET_KEY'] = "^A%DJAJU^JJ123"
app.config['MYSQL_HOST'] = 'caturwardana.mysql.pythonanywhere-services.com'
app.config['MYSQL_USER'] = 'caturwardana'
app.config['MYSQL_PASSWORD'] = 'catur1234'
app.config['MYSQL_DB'] = 'caturwardana$industrial_control_system'
app.config['MYSQL_PORT'] = 3306
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)






@app.route('/')
def home():
    return render_template("home.html")

@app.route('/homemanagement')
def homemanagement():
    return render_template("homemanagement.html")

@app.route('/homeadmin')
def homeadmin():
    return render_template("homeadmin.html")

@app.route('/account_login')
def account_login():
    return render_template("accountlogin.html")

@app.route('/account_register')
def account_register():
    return render_template("accountregister.html")

# Akun Admin
@app.route('/login_admin', methods=["GET", "POST"])
def login_admin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password'].encode('utf-8')

        curl = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        curl.execute("SELECT * FROM users_admin WHERE email=%s", (email,))
        user = curl.fetchone()
        curl.close()

        if user:
            if bcrypt.hashpw(password, user["password"].encode('utf-8')) == user["password"].encode('utf-8'):
                session['name'] = user['name']
                session['email'] = user['email']
                return render_template("homeadmin.html")
            else:
                return "Error password and email not match"
        else:
            return "Error user not found"
    else:
        return render_template("loginadmin.html")


@app.route('/register_admin', methods=["GET", "POST"])
def register_admin():
    if request.method == 'GET':
        return render_template("registeradmin.html")
    else:
        name = request.form['name']
        email = request.form['email']
        otp = request.form['otp']
        password = request.form['password'].encode('utf-8')
        hash_password = bcrypt.hashpw(password, bcrypt.gensalt())
       
        if otp == 'kelompok1':
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO users_admin (name, email, password) VALUES (%s,%s,%s)",
                        (name, email, hash_password,))
            mysql.connection.commit()
            session['name'] = request.form['name']
            session['email'] = request.form['email']
            return redirect(url_for('homeadmin'))
        else:
            return render_template("otpsalah.html")
# end akun admin

# Akun users management
@app.route('/login_management', methods=["GET", "POST"])
def login_management():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password'].encode('utf-8')

        curl = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        curl.execute("SELECT * FROM users_management WHERE email=%s", (email,))
        user = curl.fetchone()
        curl.close()

        if user:
            if bcrypt.hashpw(password, user["password"].encode('utf-8')) == user["password"].encode('utf-8'):
                session['name'] = user['name']
                session['email'] = user['email']
                return render_template("homemanagement.html")
            else:
                return "Error password and email not match"
        else:
            return "Error user not found"
    else:
        return render_template("loginmanagement.html")


@app.route('/register_management', methods=["GET", "POST"])
def register_management():
    if request.method == 'GET':
        return render_template("registermanagement.html")
    else:
        name = request.form['name']
        email = request.form['email']
        otp = request.form['otp']
        password = request.form['password'].encode('utf-8')
        hash_password = bcrypt.hashpw(password, bcrypt.gensalt())
        if otp == 'kelompok1':
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO users_management (name, email, password) VALUES (%s,%s,%s)",
                        (name, email, hash_password,))
            mysql.connection.commit()
            session['name'] = request.form['name']
            session['email'] = request.form['email']
            return redirect(url_for('homemanagement'))
        else:
            return render_template("otpsalah.html")
# end akun users management

@app.route('/logout', methods=["GET", "POST"])
def logout():
    session.clear()
    return render_template("home.html")


#render template
@app.route('/dashboardadmin')
def dashboardadmin():
    return render_template('dashboardadmin.html')

@app.route('/dashboardmanagement')
def dashboardmanagement():
    return render_template('dashboardmanagement.html')

# js dashboard 
@app.route('/jsmotor', methods= ['POST', 'GET'])
def jsmotor():
    curmotor = mysql.connection.cursor()
    curmotor.execute("SELECT * FROM motor")
    rvmotor = curmotor.fetchall()
    return jsonify(rvmotor=rvmotor)

@app.route('/jshvac', methods= ['POST', 'GET'])
def jshvac():
    curhvac = mysql.connection.cursor()
    curhvac.execute("SELECT * FROM hvac")
    rvhvac = curhvac.fetchall()
    return jsonify(rvhvac=rvhvac)

@app.route('/jspompa', methods= ['POST', 'GET'])
def jspompa():
    curpompa = mysql.connection.cursor()
    curpompa.execute("SELECT * FROM pompa")
    rvpompa = curpompa.fetchall()
    return jsonify(rvpompa=rvpompa)

#js clear log
@app.route('/clearlog', methods=["GET"])
def clearlog():
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM motor")
    cur.execute("DELETE FROM hvac")
    cur.execute("DELETE FROM pompa")
    mysql.connection.commit()
    return ('', 204)

#js clear log app
@app.route('/clearlogapp', methods=["GET", "POST"])
def clearlogapp():
    logic = request.form['logic']
    if logic == '1':
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM motor")
        cur.execute("DELETE FROM hvac")
        cur.execute("DELETE FROM pompa")
        mysql.connection.commit()
    return ('', 204)

#motor on
@app.route('/motoron', methods=["GET"])
def motoron():
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM motor")
    for i in range(10):
        now = datetime.datetime.now()
        date_time = now.strftime("%d/%m/%Y %H:%M:%S")
        time.sleep(3)
        temperature = random.randint(50,70)
        status = "ON"

        cur.execute("INSERT INTO motor (datetime, status, temperature) VALUES (%s, %s, %s)", (date_time, status, temperature))
        mysql.connection.commit()
    return ('', 204)

#motor on app
@app.route('/motoronapp', methods=["GET", "POST"])
def motoronapp():
    logic = request.form['logic']
    if logic == '1':
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM motor")
        for i in range(10):
            now = datetime.datetime.now()
            date_time = now.strftime("%d/%m/%Y %H:%M:%S")
            time.sleep(3)
            temperature = random.randint(50,70)
            status = "ON"

            cur.execute("INSERT INTO motor (datetime, status, temperature) VALUES (%s, %s, %s)", (date_time, status, temperature))
            mysql.connection.commit()
    return ('', 204)

#motor off
@app.route('/motoroff', methods=["GET"])
def motoroff():
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM motor")
    for i in range(10):
        now = datetime.datetime.now()
        date_time = now.strftime("%d/%m/%Y %H:%M:%S")
        time.sleep(3)
        temperature = random.randint(20,26)
        status = "OFF"

        cur.execute("INSERT INTO motor (datetime, status, temperature) VALUES (%s, %s, %s)", (date_time, status, temperature))
        mysql.connection.commit()
    return ('', 204)

#motor off app
@app.route('/motoroffapp', methods=["GET", "POST"])
def motoroffapp():
    logic = request.form['logic']
    if logic == '1':
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM motor")
        for i in range(10):
            now = datetime.datetime.now()
            date_time = now.strftime("%d/%m/%Y %H:%M:%S")
            time.sleep(3)
            temperature = random.randint(20,26)
            status = "OFF"

            cur.execute("INSERT INTO motor (datetime, status, temperature) VALUES (%s, %s, %s)", (date_time, status, temperature))
            mysql.connection.commit()
    return ('', 204)

#hvac on
@app.route('/hvacon', methods=["GET"])
def hvacon():
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM hvac")
    for i in range(10):
        now = datetime.datetime.now()
        date_time = now.strftime("%d/%m/%Y %H:%M:%S")
        time.sleep(3)
        temperature = random.randint(50,70)
        status = "ON"

        cur.execute("INSERT INTO hvac (datetime, status, temperature) VALUES (%s, %s, %s)", (date_time, status, temperature))
        mysql.connection.commit()
    return ('', 204)

#hvac on app
@app.route('/hvaconapp', methods=["GET", "POST"])
def hvaconapp():
    logic = request.form['logic']
    if logic == '1':
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM hvac")
        for i in range(10):
            now = datetime.datetime.now()
            date_time = now.strftime("%d/%m/%Y %H:%M:%S")
            time.sleep(3)
            temperature = random.randint(50,70)
            status = "ON"

            cur.execute("INSERT INTO hvac (datetime, status, temperature) VALUES (%s, %s, %s)", (date_time, status, temperature))
            mysql.connection.commit()
    return ('', 204)

#hvac off
@app.route('/hvacoff', methods=["GET"])
def hvacoff():
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM hvac")
    for i in range(10):
        now = datetime.datetime.now()
        date_time = now.strftime("%d/%m/%Y %H:%M:%S")
        time.sleep(3)
        temperature = random.randint(20,26)
        status = "OFF"

        cur.execute("INSERT INTO hvac (datetime, status, temperature) VALUES (%s, %s, %s)", (date_time, status, temperature))
        mysql.connection.commit()
    return ('', 204)

#hvac off app
@app.route('/hvacoffapp', methods=["GET", "POST"])
def hvacoffapp():
    logic = request.form['logic']
    if logic == '1':
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM hvac")
        for i in range(10):
            now = datetime.datetime.now()
            date_time = now.strftime("%d/%m/%Y %H:%M:%S")
            time.sleep(3)
            temperature = random.randint(20,26)
            status = "OFF"

            cur.execute("INSERT INTO hvac (datetime, status, temperature) VALUES (%s, %s, %s)", (date_time, status, temperature))
            mysql.connection.commit()
    return ('', 204)

#pompa on
@app.route('/pompaon', methods=["GET"])
def pompaon():
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM pompa")
    for i in range(10):
        now = datetime.datetime.now()
        date_time = now.strftime("%d/%m/%Y %H:%M:%S")
        time.sleep(3)
        temperature = random.randint(50,70)
        status = "ON"

        cur.execute("INSERT INTO pompa (datetime, status, temperature) VALUES (%s, %s, %s)", (date_time, status, temperature))
        mysql.connection.commit()
    return ('', 204)

#pompa on app
@app.route('/pompaonapp', methods=["GET", "POST"])
def pompaonapp():
    logic = request.form['logic']
    if logic == '1':
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM pompa")
        for i in range(10):
            now = datetime.datetime.now()
            date_time = now.strftime("%d/%m/%Y %H:%M:%S")
            time.sleep(3)
            temperature = random.randint(50,70)
            status = "ON"

            cur.execute("INSERT INTO pompa (datetime, status, temperature) VALUES (%s, %s, %s)", (date_time, status, temperature))
            mysql.connection.commit()
    return ('', 204)

#pompa off
@app.route('/pompaoff', methods=["GET"])
def pompaoff():
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM pompa")
    for i in range(10):
        now = datetime.datetime.now()
        date_time = now.strftime("%d/%m/%Y %H:%M:%S")
        time.sleep(3)
        temperature = random.randint(20,26)
        status = "OFF"

        cur.execute("INSERT INTO pompa (datetime, status, temperature) VALUES (%s, %s, %s)", (date_time, status, temperature))
        mysql.connection.commit()
    return ('', 204)

#pompa off app
@app.route('/pompaoffapp', methods=["GET", "POST"])
def pompaoffapp():
    logic = request.form['logic']
    if logic == '1':
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM pompa")
        for i in range(10):
            now = datetime.datetime.now()
            date_time = now.strftime("%d/%m/%Y %H:%M:%S")
            time.sleep(3)
            temperature = random.randint(20,26)
            status = "OFF"

            cur.execute("INSERT INTO pompa (datetime, status, temperature) VALUES (%s, %s, %s)", (date_time, status, temperature))
            mysql.connection.commit()
    return ('', 204)

#allon
@app.route('/allon', methods=["GET"])
def allon():
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM motor")
    cur.execute("DELETE FROM hvac")
    cur.execute("DELETE FROM pompa")
    for i in range(10):
        now = datetime.datetime.now()
        date_time = now.strftime("%d/%m/%Y %H:%M:%S")
        time.sleep(3)
        temperature1 = random.randint(50,70)
        temperature2 = random.randint(50,70)
        temperature3 = random.randint(50,70)
        status = "ON"

        cur.execute("INSERT INTO motor (datetime, status, temperature) VALUES (%s, %s, %s)", (date_time, status, temperature1))
        cur.execute("INSERT INTO hvac (datetime, status, temperature) VALUES (%s, %s, %s)", (date_time, status, temperature2))
        cur.execute("INSERT INTO pompa (datetime, status, temperature) VALUES (%s, %s, %s)", (date_time, status, temperature3))
        mysql.connection.commit()
    return ('', 204)

#alloff
@app.route('/alloff', methods=["GET"])
def alloff():
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM motor")
    cur.execute("DELETE FROM hvac")
    cur.execute("DELETE FROM pompa")
    for i in range(10):
        now = datetime.datetime.now()
        date_time = now.strftime("%d/%m/%Y %H:%M:%S")
        time.sleep(3)
        temperature1 = random.randint(20,27)
        temperature2 = random.randint(20,27)
        temperature3 = random.randint(20,27)
        status = "OFF"

        cur.execute("INSERT INTO motor (datetime, status, temperature) VALUES (%s, %s, %s)", (date_time, status, temperature1))
        cur.execute("INSERT INTO hvac (datetime, status, temperature) VALUES (%s, %s, %s)", (date_time, status, temperature2))
        cur.execute("INSERT INTO pompa (datetime, status, temperature) VALUES (%s, %s, %s)", (date_time, status, temperature3))
        mysql.connection.commit()
    return ('', 204)


#appmotor
@app.route('/appmotor')
def appmotor():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM motor")
    #row_headers=[x[0] for x in cur.description] 
    rv = cur.fetchall()
    cur.close()
    return render_template('appmotor.html', appmotor=rv)

#apphvac
@app.route('/apphvac')
def apphvac():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM hvac")
    #row_headers=[x[0] for x in cur.description] 
    rv = cur.fetchall()
    cur.close()
    return render_template('apphvac.html', apphvac=rv)

#apppompa
@app.route('/apppompa')
def apppompa():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM pompa")
    #row_headers=[x[0] for x in cur.description] 
    rv = cur.fetchall()
    cur.close()
    return render_template('apppompa.html', apppompa=rv)

#if __name__ == '__main__':
#    app.secret_key = "^A%DJAJU^JJ123"
#    app.run(debug=True)
#    #app.run(host='0.0.0.0', debug=True)
