from flask import Flask,render_template,session,request,redirect
app = Flask(__name__)
app.secret_key = 'Secret times'

@app.route('/')
def index():
    return render_template('survey.html')

@app.route('/process', methods=['POST'])
def process_form():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    return redirect('/submit')

@app.route('/submit')
def display_form_results():
    return render_template('submit.html')


@app.route('/home')
def home():
    return redirect('/')

    
if __name__=='__main__':
    app.run(debug=True)