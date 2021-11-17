from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    students = [
        {'first_name' : 'Michael', 'last_name' : 'Choi', 'age': 40},
        {'first_name' : 'John', 'last_name' : 'Supsupin', 'age': 45},
        {'first_name' : 'Mark', 'last_name' : 'Guillen', 'age': 50},
        {'first_name' : 'KB', 'last_name' : 'Tonel', 'age': 60}
    ]
    return render_template('index.html', students = students)

if __name__ == "__main__":
    app.run(debug=True)