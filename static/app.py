from flask import Flask, render_template
import os

app = Flask(
    __name__,
    template_folder=os.path.join(os.path.dirname(__file__), '..', 'templates'),
    static_folder=os.path.dirname(__file__)
)

data = dict()
reviews = ["Good product","bad Product","I like it"]
positive=2
negative=1

@app.route("/")
def index():
    data['reviews'] = reviews
    data['positive'] = positive
    data['negative'] = negative
    return render_template('index.html',data=data)

if __name__ == '__main__':
    app.run()