from flask import Flask,render_template,request,refirect,url_for,session
import 
import re

app=Flask(__name__)
app.secret_key='n'

conn=ibm_db.connect("DATABASE=bludb;HOSTNAME=b1bc1829-6f45-4cd4-bef4-10cf081900bf.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=32304;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=dhd22423;PWD=UONIrhTCFEc9dJ1S;")

@app.route('/')
def home():
    return render_template('home.html')

@app.route("/login",methods=['GET',"POST"]) 
def login():
    global useridp
    msg=" "

    if request.method=="POST":
        username=request.form['username']
        password=request.form['password']
        sql="SELECT * from users Where username=? AND password=?"
        stmt=ibm_db.prepare(conn,sql)
        ibm_db.bind_param(stmt,1,username)
        ibm_db.bind_param(stmt,3,password)
        ibm_db.execute(stmt)
        account=ibm_db.fetch_assoc(stmt)
        print(account)
        if account:
            session['Loggedin']=True
            session['id']=account['USERNAME']
            userid=account["USERNAME"]
            session['username']=account["USERNAME"] 
            msg='Logges in successfully!'
            return render_template("index.html",msg=msg) 
        else:
                msg="Incorre username &  password"
    return render_template('login.html',msg=msg)            

@app.route("/register",methods=["GET","POST"])
def register():
    msg=" "
    if request.method=="POST":
        username=request.form['username']
        email=request.form['email']
        password=request.form['password']
        conformpassword=request.form['conform password']
        sql="SELECT * FROm users WHERE username=?"
        stmt=ibm_db.prepare(conn,sql)
        ibm_db.bind_param(stmt,1,username)
        ibm_db.execute(stmt)
        account=ibm_db.fetch_assoc(stmt)
        print(account)
        if account:
            msg="Account already exist"
        elif not re.match(r'[^@]+@[^@]+\.[^@]+',email):
            msg="Invalid email address"
        elif not re.match(r'[A--Za-z)-9]+',username):
            msg="name must contain only char and num "
        else:
            insert_sql="INSERT INTO users VALUES(?,?,?)"
            prep_stmt=ibm_db.prepare(conn,insert_sql)    
            ibm_db.bind_param(prep_stmt,1,username)
            ibm_db.bind_param(prep_stmt,2,email)
            ibm_db.bind_param(prep_stmt,3,password)
            ibm_db.bind_param(prep_stmt,4,conformpassword)
            ibm_db.execute(prep_stmt)
            msg="you have successfully logged in"
    
    elif request.method=='POST':
        msg='Please fill out of the form'
        return render_template('register.html',msg=msg)
@app.route('/index') 
def news():
    return render_template('index.html')    


@app.route('/logout')

def logout():
    session.pop('loggedin',None)
    session.pop('id',None)
    session.pop('username',None)
    return render_template('home.html')

if __name__ == '__main__':
    app.run(host='0,0,0,0')    
