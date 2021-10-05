from flask import Flask, render_template
# import the class from friend.py
from friend import Friend
app = Flask(__name__)
@app.route("/")
def index():
    # call the get all classmethod to get all friends
    friends = Friend.get_all()
    return render_template("index.html", friends=Friend)
            
if __name__ == "__main__":
    app.run(debug=True)

