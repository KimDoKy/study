from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    kwargs = {}
    kwargs['thing'] = request.args.get('thing')
    kwargs['height'] = request.args.get('height')
    kwargs['color'] = request.args.get('color')
    return render_template('home.html', **kwargs)

app.run(host='localhost', port=5000)
