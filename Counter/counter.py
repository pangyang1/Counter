from flask import Flask, session,render_template,request,redirect
app = Flask(__name__)
app.secret_key = "secret"

@app.route('/')
def home():
    if 'count' not in session:
        session['count'] = 0
    session['count'] +=1
    return render_template('home.html')
@app.route('/add2')
def add():
    session['count'] +=1
    return redirect('/')


@app.route('/reset')
def reset():
    session['count'] =0
    return redirect('/')

app.run(debug=True)
