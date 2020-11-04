from flask import Flask
import sqlite3
app2= Flask(__name__)

@app2.route('/rashid')
def hello_name(name):
    return 'Hello' + name
if __name__ == "__main__":
        app2.run(debug=True)