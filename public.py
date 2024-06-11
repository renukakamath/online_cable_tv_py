from flask import *
from database import *

public=Blueprint('public',__name__)

@public.route('/')
def home():
    return render_template('home.html')

@public.route('/login',methods=['get','post'])
def login():
    if 'submit' in request.form:
        username=request.form['name']
        password=request.form['password']
        q="select * from tbl_login where username='%s'and password='%s'"%(username,password)
        res=select(q)
        if res:
            session['username']=res[0]['username']
            uname=session['username']
            if res[0]['type']=="admin":
                return redirect(url_for("admin.admin_home"))
            if res[0]['type']=="staff":
                 q="select * from tbl_staff  where username='%s'"%(uname)
                 res=select(q)
                 if res:
                    session['staff_id']=res[0]['staff_id']
                    staff_id=session['staff_id']
                    return redirect(url_for("staff.staff_home"))
            if res[0]['type']=="employer":
                q="select * from tbl_employer  where username='%s'"%(uname)
                res=select(q)
                if res:
                    session['emp_id']=res[0]['emp_id']
                    uname=session['emp_id']
              
                return redirect(url_for("employer.employer_home"))
            

        print(username,password)
    return render_template("login.html")

@public.route('/registration',methods=['get','post'])
def registration():
    if 'submit' in request.form:
        name=request.form['name']
        username=request.form['username']
        phone_no=request.form['phone_no']
        aadhar_no=request.form['aadhar_no']
        password=request.form['password']
        types=request.form['types']
        if types == "staff":
            q="insert into tbl_login values('%s','%s','musician',1)"%(username,password)
            insert(q)

            q="insert into tbl_staff values(null,'%s','%s','%s','%s','%s','%s',1)"%(username,name,username,phone_no,aadhar_no,password)
            insert(q)
            flash("successfully")

        elif types == "Employer":

            q="insert into tbl_login values('%s','%s','employer',1)"%(username,password)
            insert(q)

            q="insert into tbl_employer values(null,'%s','%s','%s','%s','%s','%s',1)"%(username,name,username,phone_no,aadhar_no,password)
            insert(q)
            flash("successfully")
        
            return redirect(url_for('public.login'))

    return render_template("registration.html")