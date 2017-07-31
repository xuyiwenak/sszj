from flask import Flask
app = Flask(__name__)

@app.route('/<user_name>')
def hello_world(user_name):
    return 'Hello %s!' % user_name

if __name__ == '__main__':
    app.run(host='0.0.0.0')
