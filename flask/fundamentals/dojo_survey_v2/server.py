from flask import Flask,render_template,session,redirect,request
app=Flask (__name__)
app.secret_key = 'dojo secrets'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def form():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    session['dojo'] = request.form['dojo']
    return redirect('/result')

@app.route('/result')
def display_user():
    return render_template('user.html')

@app.route('/home')
def home():
    return redirect('/')




if __name__== '__main__':
    app.run(debug=True)