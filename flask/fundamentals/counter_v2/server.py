from flask import Flask, render_template, session,request,redirect
app = Flask(__name__)
app.secret_key = 'Super secret key'

@app.route('/')
def home_page():
    if 'counter' not in session:
        session['counter'] = 0
        return render_template('counter.html')
    else:
        session['counter'] += 1
    return render_template('counter.html')

@app.route('/increment')
def increment():
    session['counter'] += 2
    return render_template('counter.html')


@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')


if __name__=='__main__':
    app.run(debug =True)