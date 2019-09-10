from flask import Flask, jsonify, abort, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, world!"

tasks = [
    {
        'id': 1,
        'title': 'buy Python',
        'description': '배고프다..',
        'done': False
    },
    {
        'id': 2,
        'title': 'Learn Python',
        'description': 'Need to find a good Python tutorial on the web',
        'done': False
    }
]

@app.route('/todo/api/v1/tasks/<int:task_id>', methods=['GET'])
def get_tasks(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task':task[0]})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not Found'}), 404)
if __name__ == '__main__':
    app.run(debug=True)
