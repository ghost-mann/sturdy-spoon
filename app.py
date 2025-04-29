from flask import Flask, render_template, request, redirect
import datetime
app = Flask(__name__)

todo_items = []

@app.route('/', methods=['GET', 'POST'])
def index():
    # current date and time
    now = datetime.datetime.now()

    # format as HH:MM
    current_time = now.strftime("%Y-%m-%d %H:%M")
    # add tasks and refresh
    if request.method == 'POST':
        task = request.form.get('task')
        if task:
            todo_items.append(task)
        redirect('/')


    return render_template('index.html', current_time=current_time, todo_items=todo_items)

if __name__ == '__main__':
    app.run(debug=True)