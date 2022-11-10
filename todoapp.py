import TodoItem
from flask import Flask, render_template, request, redirect
app = Flask(__name__)


todo_list = []


@app.route('/')
def route_1():
    return render_template('index.html', todo_list=todo_list)


@app.route('/submit', methods=['GET', 'POST'])
def route_2():
    task = request.form.get("task")
    email = request.form.get("email")
    priority = request.form.get("priority")

    if priority is None or email is None or task is None:
        return redirect('/')

    todo_list.append(TodoItem.TodoItem(task, email, priority))

    return redirect('/')


@app.route('/clear', methods=['GET', 'POST'])
def route_3():
    todo_list.clear()
    return redirect('/')


if __name__ == '__main__':
    app.run()


