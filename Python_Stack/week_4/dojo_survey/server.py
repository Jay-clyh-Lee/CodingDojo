from flask import Flask, render_template, session, request, redirect

app = Flask(__name__)
app.secret_key=('secret')

locations = ["San Jose", "Seattle", "Los Angeles", "New York", "Palo Alto"]
languages = ["Python", "Java", "C++", "C#", "MySQL"]

@app.route('/')
def index():
    return render_template('index.html', locations = locations, languages = languages)

@app.route('/result')
def show_result():
    return render_template('result.html', data = session['data'])

@app.route('/process', methods=['POST'])
def process_info():
    session['data'] = request.form
    print(f'THE REQUEST FORM IS THIS: {request.form} TAKE A GOOD LOOK AT IT!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!====================')
    return redirect('/result')


if __name__ == "__main__":
    app.run(debug=True)