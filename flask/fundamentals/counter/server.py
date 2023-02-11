from flask import Flask, render_template, session, redirect
app=Flask(__name__)
app.secret_key="this is my secret key"

@app.route('/')
def index():
    if 'count' not in session:
        session['count'] = 0
        return render_template('index.html')    
    else:
        session['count'] +=1
        return render_template('index.html')

@app.route('/destroy')
def destroy():
    session.clear()  
    return redirect('/')   
    
if __name__=="__main__":
    app.run(debug=True)