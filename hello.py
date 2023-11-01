#!/usr/bin/env python3
# Note that for Mac, you have to use port 8000 (cuz OS takes 5000 and 7000 already) => See last line in code.
# Note: if you get "content-type" isn't JSON error, you just have to specify it as a header in your curl command.

# Post: curl -v -X PUT localhost:8000/todos/3 -H "Content-Type: application/json" -d "task=profit more"
# Put: curl -v -X PUT -H "Content-Type: application/json" -d '{"task": "profit more"}' localhost:8000/todos/3

# HTTPIE COMMANDS:
# http :8000/todos == curl localhost:8000/todos
# http HEAD :8000/todos == Gives you the head of the request.
# http POST :8000/todos task="Try HTTPIE" => Posts a task (defaults to JSON format already for you) with the content "Try HTTPIE".
 

from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument("task")

TODOs = {
    1: {"task": "build an API"},
    2: {"task": "?????"},
    3: {"task": "profit"},
}


def abort_if_todo_not_found(todo_id):
    if todo_id not in TODOs:
        abort(404, message="TODO {} does not exist".format(todo_id))


def add_todo(todo_id):
    args = parser.parse_args()
    todo = {"task": args["task"]}
    TODOs[todo_id] = todo
    return todo


class Todo(Resource):
    """
    Shows a single TODO item and lets you delete a TODO item.
    """

    def get(self, todo_id):
        abort_if_todo_not_found(todo_id)
        return TODOs[todo_id]

    def delete(self, todo_id):
        abort_if_todo_not_found(todo_id)
        del TODOs[todo_id]
        return "", 204

    def put(self, todo_id):
        return add_todo(todo_id), 201


class TodoList(Resource):
    """
    Shows a list of all TODOs and lets you POST to add new tasks.
    """

    def get(self):
        return TODOs

    def post(self):
        todo_id = max(TODOs.keys()) + 1
        return add_todo(todo_id), 201


api.add_resource(Todo, "/todos/<int:todo_id>")
api.add_resource(TodoList, "/todos")

if __name__ == "__main__":
    app.run(port=8000, debug=True)
