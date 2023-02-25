from flask import Flask,render_template,redirect,session,request
import random
import datetime
app = Flask(__name__)
app.secret_key = 'Ninja gold secret key'


@app.route('/')
def index():
    if 'total_gold' and 'activities' not in session:
        session['total_gold'] = 0
        session['activities'] = ''
    return render_template('index.html', messages = session['activities'])

@app.route('/process',methods=['POST'])
def process_money():

    location = request.form['property']
    time = datetime.datetime.now().strftime('%c')
    
    if location == 'farm':
        gold_count = random.randint(10,20)  
    elif location == 'cave':
        gold_count = random.randint(5,10)
    elif location == 'house':
        gold_count = random.randint(2,5)
    else:
        gold_count = random.randint(-50,50)
    session['total_gold'] += gold_count
    if gold_count >= 0:
        new_message = f"<p class='text-success'>Earned {gold_count} golds from {location}! {time}</p>"
        session['activities'] += new_message
    elif gold_count < 0:
        new_message = f"<p class='text-danger'>Entered {location} and lost {gold_count} gold {time}</p>"
        session['activities'] += new_message
    return redirect('/')

@app.route('/reset')
def reset_gold():
    session.clear()
    return redirect('/')



if __name__=='__main__':
    app.run(debug=True)