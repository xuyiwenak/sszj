from flask import Flask
app = Flask(__name__)

@app.route('/<stat_cmd>')
def data_stat(stat_cmd):
    return 'Execute %s!' % stat_cmd

if __name__ == '__main__':
    app.run(host='0.0.0.0')
