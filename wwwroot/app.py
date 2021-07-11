import pyrebase
from flask import *
import sqlite3
from flask import jsonify, render_template, request
app = Flask(__name__)

config = {
    "apiKey": "AIzaSyCTO7a4t_Jf4sN-ngRArL76PB8dVdSikyk",
    "authDomain": "ritunisquad.firebaseapp.com",
    "databaseURL": "https://ritunisquad.firebaseio.com",
    "projectId": "ritunisquad",
    "storageBucket": "ritunisquad.appspot.com",
    "messagingSenderId": "504972791037",
    "appId": "1:504972791037:web:58718efb815842ced38294",
    "measurementId": "G-LF5QWP2Z9H"
}
person ={'is_logged_in': False, 'email': ""}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db =firebase.database()

#Global variable


#Registracija uporabnika
@app.route("/register",methods=['GET','POST'])
def user_register():
    unsuc1 = 'Registration was unsucessful, plesse try again'
    unsuc2 = 'Problem with db'
    succesful = 'Registration was succesful'
    suc = False 
    if request.method == 'POST':
        name = request.form['userName']
        email = request.form['email']
        passw = request.form['pass']
        
        try:
            #Registriraj uporabnika
            user = auth.create_user_with_email_and_password(email,passw)
                       
        except:
            return render_template('register_user.html',us = unsuc1, suc = False)    
        try:
            #Pošlji potrditveni mail
            auth.send_email_verification(user['idToken'])
            data={'username':name,'email':email}
            db.child("user").push(data)
            return render_template('register_user.html',us = succesful, suc=True)  
        except:
            return render_template('register_user.html',us = unsuc2, suc = False)
    return render_template('register_user.html')


@app.route("/", methods=['GET','POST'])

def sign_up():
    unsuccesful = 'Please check your credentials'
    if request.method == 'POST':
        email = request.form['name']
        passw = request.form['pass']
        try:
            user= auth.sign_in_with_email_and_password(email, passw)
            global person            
            person["is_logged_in"]= True
            person["email"]= email
            pod =(auth.get_account_info(user['idToken']))
            for x in pod['users']:
                m = x['emailVerified']
            if m:
                return redirect('/user')
            else:
                return render_template('sign_up_user.html',us='Email ni potrjen')
            
            #return render_template('sign_up_user.html',us=pod)
            #return redirect('/user')
                
            

        except:
            return render_template('sign_up_user.html',us=unsuccesful) 
    return render_template('sign_up_user.html')

#When user decides to change his name
@app.route("/user/changeName", methods=['GET','POST'])
def changeName():
    if request.method == 'POST' and person["is_logged_in"]== True:
        
         name = request.form['ime']
         email=person["email"]
         try:
            
            people=db.child("user").get()
            for x in people.each():
                if (x.val()['email']==email):
                    db.child("user").child(x.key()).update({'username':name})
            return render_template('changeName.html',val=True )
         except:
            print("Ne dela")   

    return render_template('changeName.html')
    
#When user logs in it redirects him to this pae
@app.route("/user")
def main():
    global person
    if person['is_logged_in'] == True:
        email=person['email']
        people=db.child("user").get()
        for x in people.each():
            if (x.val()['email']==email):
                ime = x.val()['username']
        
        return render_template('main.html',name = ime)
    else:
         return redirect('/')

#Sign out user
@app.route("/user/sign_out")
def signout():
    
    person['is_logged_in']= False
    person['email']= ""
    auth.current_user = None
    auth.current_user = None
    return  redirect('/')   

#Change password      
@app.route("/user/change_password")
def changePassword():
    email=person["email"]
    auth.send_password_reset_email(email)
    return redirect("/user")

@app.route("/test")
def tellst():
    global person
    ime="nea dela"
    if person['is_logged_in'] == True:
       email=person['email']
       people=db.child("user").get()
       for x in people.each():
           if (x.val()['email']==email):
               ime = x.val()['username']
              #ime = jsonify(ime)
    return render_template('chat.html',ime=ime)

@app.route('/add_numbers')
def add_numbers():
    a = request.args.get('a', 0 ,type=int)
    b = request.args.get('b', 0 ,type=int)
    return jsonify(result=a +b)

if __name__ == '__main__':
    app.run(debug=True)    

