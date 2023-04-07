from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'hello'

@app.route('/')
def index():
    if not "count" in session:
        session['count'] = 0
    num = session['count']
    print( num )
    return render_template('index.html', num= num)

@app.route('/count')
def count_visits():
    num = session['count']
    if 'count' in session:
        session[ 'count' ] += 1
    return render_template('count.html', num=num)

@app.route('/destroy_session')
def destroy_session():
    session['count'] = 0
    return redirect('/')

if __name__=='__main__':
    app.run(debug=True)
