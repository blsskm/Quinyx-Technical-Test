from flask import Flask, render_template, request
import requests

app = Flask(__name__)

i = 0

@app.route('/')
def index():
    respond = requests.get('http://api.icndb.com/jokes/random/')
    while i <= 10:
        print (respond.content)
        i = i + 1
    return

if __name__ == "__main__":
    app.run(debug=True)



