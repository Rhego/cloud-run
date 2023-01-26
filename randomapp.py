from flask import Flask,render_template, request
from flask_mysqldb import MySQL
import requests
import jsonpickle
 
app = Flask(__name__)
 
app.config['MYSQL_HOST'] = '192.168.102.4'
app.config['MYSQL_USER'] = 'cloudrun'
app.config['MYSQL_PASSWORD'] = 'cloudrun'
app.config['MYSQL_DB'] = 'cloud_run_test'
 
mysql = MySQL(app)


@app.route('/')
def form():
     # api-endpoint
    URL = "http://192.168.111.15:9000"
    
    # location given here
    location = "delhi technological university"
    
    # defining a params dict for the parameters to be sent to the API
    PARAMS = {'address':location}
    
    # sending get request and saving the response as response object
    r = requests.get(url = URL, timeout=10)
    
# extracting data in json format
    print(r.status_code)
    
    return "GOOD "+ str(r.status_code )  + URL
 
@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'GET':
        return "Login via the login Form"
     
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        cursor = mysql.connection.cursor()
        cursor.execute(''' INSERT INTO users VALUES(%s,%s)''',(name,age))
        mysql.connection.commit()
        cursor.close()
        return f"Done!!"
 
app.run(debug=True, host='0.0.0.0', port=80)
