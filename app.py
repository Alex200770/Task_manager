from flask import Flask, render_template
from models import get_tasks


app = Flask(__name__, template_folder='./template')


@app.route('/')  # https://my-site.com
def index():
    tasks = get_tasks()
    return render_template('index.html')


if __name__ == '__main__': #python3 app.py
    app.run(debug=True, port=5001)
