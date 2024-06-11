from flask import *
from database import *

musician=Blueprint('musician',__name__)



@musician.route('/musician_home')
def musician_home():
    return render_template('musician_home.html')

@musician.route('/browse_jobs')
def browse_jobs():
	data={}
	q="SELECT * FROM tbl_job INNER JOIN `tbl_employer` USING (`emp_id`) INNER JOIN `tbl_type` USING (type_id) INNER JOIN `tbl_genre` USING (`genre_id`) "
	res=select(q)
	data['updatejobs']=res
	return render_template('browse_jobs.html',data=data)


	return render_template('musician_home.html')



@musician.route('/ApplyApplication',methods=['post','get'])
def ApplyApplication():
	data={}



	if "submit" in request.form:
		name=request.form['name']
		job_id=request.args['job_id']
		msc_id=session['msc_id']
		
		q="insert into job_application values(null,'%s','%s','%s','Applyed')"%(name,job_id,msc_id)
		insert(q)
		return redirect(url_for('musician.ApplyApplication'))




	return render_template('ApplyApplication.html',data=data)



@musician.route('/musician_viewapplication')
def musician_viewapplication():
	
	data={}

	msc_id=session['msc_id']
	q="SELECT * FROM `job_application` INNER JOIN `tbl_job` USING (`job_id`) INNER JOIN `tbl_musician` USING (`msc_id`) where msc_id='%s' and status='Accept'"%(msc_id)
	res=select(q)
	data['updatejobs']=res

	return render_template('musician_viewapplication.html',data=data)


@musician.route('/musician_experiance',methods=['post','get'])
def musician_experiance():
	if "submit" in request.form:
		title=request.form['title']
		name=request.form['name']
		application_id=request.args['application_id']
		q="insert into tbl_experience values(null,'%s','%s',curdate(),'%s')"%(title,name,application_id)
		q=insert(q)
		return redirect(url_for('musician.musician_experiance'))

	return render_template('musician_experiance.html')



@musician.route('/employee_profile',methods=['post','get'])
def employee_profile():
	data={}
	msc_id=session['msc_id']




	q="SELECT * FROM `tbl_musician` where msc_id='%s'"%(uname)
	res=select(q)
	data['updateprofile']=res


	if "submit" in request.form:
		name=request.form['name']
		username=request.form['username']
		phone_no=request.args['phone_no']
		aadhar_no=request.args['aadhar_no']
		q="update tbl_musician set msc_name='%s' msc_email='%s' ,msc_no='%s',msc_aadhar='%s' where msc_id='%s'"%(uname)
		update(q)
		return redirect(url_for('musician.employee_profile'))




	return render_template('employee_profile.html',data=data)



	


