from flask import Flask, escape, request, render_template, url_for

app = Flask(__name__)
print('started')

@app.route('/')
def front_page():
    return render_template('index.html')