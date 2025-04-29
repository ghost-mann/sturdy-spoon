from flask import Flask, render_template
import datetime
app = Flask(__name__)

@app.route('/')
def index():
    # current date and time
    now = datetime.datetime.now()

    # format as HH:MM:SS
    current_time = now.strftime("%H:%M:%S")

    return render_template('index.html', current_time=current_time)

if __name__ == '__main__':
    app.run(debug=True)