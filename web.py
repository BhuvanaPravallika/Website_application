from flask import Flask,render_template,request
web=Flask(__name__)
@web.route('/')
def about_Page():
    return render_template('about.html')
@web.route('/Registration')
def Registaration_Page():
    return render_template('Registration.html')
@web.route('/login')
def login_page():
    return render_template('login.html')
@web.route('/check',methods=['POST'])
def collect_Data():
    n=request.form['fname']
    p=request.form['password']
    result='data collected successfully'
    return(render_template('login.html',result))
if __name__=="__main__":
    web.run(debug=True)