from flask import Flask, request, render_template
from core.waf_flask_middleware import detect_sql_injection
from database.mysql_connector import MySQLHandler

app = Flask(__name__)

@app.before_request
def before_request():
    detect_sql_injection()

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    if request.method == 'POST':
        username = request.form.get("username")
        db = MySQLHandler()
        try:
            sql = f"SELECT * FROM users WHERE username = '{username}'"
            result = db.query(sql)
        except Exception as e:
            result = str(e)
    return render_template("index.html", result=result)

if __name__ == '__main__':
    app.run(debug=True)
