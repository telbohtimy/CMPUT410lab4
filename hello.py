from flask import Flask
app= Flask(__name__)


@app.route('/hello')
def hello():
    return '<h1>Hello Flask!</h1>'

@app.route('/bye')
def bye():
    return '<h1>Bye bye Flask!</h1>'



if __name__=='__main__':
    app.run()