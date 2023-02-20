from flask import Flask,redirect
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/dojo')
def say_dojo():
    return 'Dojo!'

@app.route('/say/<string:name>')
def say_val(name):
    return 'Hi ' + name + '!'

@app.route('/repeat/<int:num>/<string:name>')
def repeat_val(name,num):
    return name * num 

# @app.route('/<string:text>')
# def fail(text):
#     return 'Sorry! No response from ' + text + ' Try again.'
    





if __name__ =='__main__':
    app.run(debug=True)