# ad-week10
ad week10
App.py code
from flask import Flask, request,render_template
app=Flask(_name_)
 @app.route('/')
def hello_world():
   return render_template("login.html")
database={'cmrit':'123','mallareddy':'abc','hyd':'abc'}
 
@app.route('/form_login',methods=['POST','GET'])
def login():
    name1=request.form['Username']
    pwd=request.form['Password']
 
    if name1 not in database:
     return render_template('login.html',info='Invaild User')
    else:
       if database[name1]!=pwd:
        return render_template('login.html',info='Invaild Password')
       else:
        return render_template('home.html',name=name1)
    if _name=='_main':
        app.run()
week11
Login.html  code  


<!DOCTYPEhtml>
<html lang="en">
    <head>
    <meta charset="UTF-8">
    <title>Login page</title>
</head>
<body bgcolor="orange">
    <form action="/form_login" method="post">
        <h2></h2>Username:<br>
        <input type="text"name='Username'>
        <br> Password:<br>
        <input name='Password'>
        <br>
        <input type="Submit"value="Login">
    </form>
    <h1> {{info}}</h1>
</body>
</html>
Home.html             code  


<!DOCTYPEhtml>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Home</title>
</head>
<body bgcolor="teal">
  <br>
  <h1 align="center">
     Welcome {{name}}
  </h1>
</body>
</html>
App.py code
from flask import Flask, request,render_template
app=Flask(_name_)
 @app.route('/')
def hello_world():
   return render_template("login.html")
database={'cmrit':'123','mallareddy':'abc','hyd':'abc'}
 
@app.route('/form_login',methods=['POST','GET'])
def login():
    name1=request.form['Username']
    pwd=request.form['Password']
 
    if name1 not in database:
     return render_template('login.html',info='Invaild User')
    else:
       if database[name1]!=pwd:
        return render_template('login.html',info='Invaild Password')
       else:
        return render_template('home.html',name=name1)
    if _name=='_main':
        app.run()
