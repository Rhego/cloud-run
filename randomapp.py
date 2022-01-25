# randomapp.py
import random
import string
from flask import Flask
app = Flask(__name__)
@app.route('/')
def rannum():
    x = random.randint(5000770880, 9008800000)
    y = str(x)
    return y
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
