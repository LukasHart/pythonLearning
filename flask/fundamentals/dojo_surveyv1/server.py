from flask import Flask, render_template, redirect, session,request
app=Flask(__name__)
app.secret_key = 'secrets'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def form():
    session['name'] = request.form['name']
    session['locations'] = request.form['locations']
    session['languages'] = request.form['languages']
    session['comment'] = request.form['comment']
    return redirect('/result')

@app.route('/result')
def display_user():
    return render_template('user.html')



if __name__=='__main__':
    app.run(debug=True)