from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'

todos = ['learn flask','activate venv','build app']

class TodoForm(FlaskForm):
    todo = StringField("Todo",validators = [DataRequired()])
    submit = SubmitField("Add")

@app.route('/', methods = ["GET","POST"])
def index():
    todos_form = TodoForm()
    if todos_form.validate_on_submit():
        new_todos = todos_form.todo.data
        todos.append(new_todos)
    return render_template('index.html', todos = todos, template_form = todos_form)
