from flask import *

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome Page for the user"

@app.route('/fact/<int:num>')
def facto(num):
    return render_template('factorial.html',n = num)

@app.route('/login',methods = ['POST'])
def login():
    uname = request.form['uname']
    passwr = request.form['pass']
    captcha = request.form['captcha'] 
    if uname == 'Jay':
        if passwr == 'pass':
            if captcha == 'Td4eva':
                return render_template('welcome.html')
            else:
                return "The captcha entered was invalid"
        else:
            return "Password is invalid"
    else:
        return "Wrong Username"
    

if __name__ == "__main__":
    app.run(debug=True)