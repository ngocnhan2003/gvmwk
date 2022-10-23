from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/handler', methods=['GET', 'POST'])
def handle_push():
    if not request.json:
        abort(400)
    print("Request: {}".format(request.json))
    return jsonify({'status': 'ok'}), 200

if __name__ == '__main__':
    app.run()
