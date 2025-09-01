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
MAIN ACTIVITY.JAVA   CODE

import androidx.appcompat.app.AppCompatActivity;
import android.content.Intent;
import android.net.Uri;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

  public class MainActivity extends AppCompatActivity {

    TextView welcome;

    Button phone, sms, website;

    Intent i = new Intent();


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        phone = (Button)findViewById(R.id.b1);

        sms = (Button) findViewById(R.id.b2);

        website = (Button) findViewById(R.id.b3);

        phone.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                i.setAction(Intent.ACTION_DIAL);
                i.setData(Uri.parse("tel:9505061025"));
                startActivity(i);
            }
        });

        sms.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                i.setAction(Intent.ACTION_VIEW);
                i.setData(Uri.parse("sms:9505061025"));
                startActivity(i);

            }
        });

        website.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                i.setAction(Intent.ACTION_VIEW);
                i.setData(Uri.parse("https://www.cmrithyderabad.edu.in/"));
                startActivity(i);

            }
        });
    }
}
activity_main.xml   CODE
<?xml version="1.0" encoding="utf-8"?>
  <LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    android:background="#fff"
    tools:context=".MainActivity">

    <TextView
        android:id="@+id/tv1"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Menu options"
        android:textAlignment="center"
        android:textColor="#572623"
        android:textSize="40sp"
        android:textStyle="italic"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintEnd_toEndOf="parent"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintTop_toTopOf="parent" />

    <Button
        android:id="@+id/b1"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:layout_marginBottom="2dp"
        android:background="#FFF"
        android:text="Phone"
        android:textSize="25sp"
        android:textStyle="italic"
        android:textAllCaps="true"
        tools:ignore="TextContrastCheck" />
    <Button
    android:id="@+id/b2"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:layout_marginBottom="2dp"
    android:background="#FFF"
    android:text="SMS"
    android:textSize="25sp"
    android:textStyle="italic"
    android:textAllCaps="true"
    tools:ignore="TextContrastCheck" />
  <Button
    android:id="@+id/b3"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:layout_marginBottom="2dp"
    android:background="#FFF"
    android:text="Website"
    android:textSize="25sp"
    android:textStyle="italic"
    android:textAllCaps="true"
    tools:ignore="TextContrastCheck" />

  </LinearLayout>
