from flask import *
from database import *

employer=Blueprint('employer',__name__)



@employer.route('/employer_home')
def employer_home():
    return render_template('employer_home.html')

@employer.route('/job_postings',methods=['post','get'])
def job_postings():
	data={}
	q="select * from tbl_type"
	res=select(q)
	data['type']=res
	q="select * from tbl_genre"
	res=select(q)
	data['tbl_genre']=res


	


	if "submit" in request.form:
		jt=request.form['job_title']
		hd=request.form['job_desc']
		typ=request.form['type']
		gen=request.form['gen']
		rat=request.form['job_rate']
		jd=request.form['job_duration']
		jl=request.form['job_location']

		emp_id=session['emp_id']
		q="insert into tbl_job values(null ,'%s','%s','%s','%s','%s','%s','%s','%s','1')"%(emp_id,jt,hd,typ,gen,rat,jd,jl)
		insert(q)


	return render_template('job_postings.html',data=data)


@employer.route('/view_job_postings')
def view_job_postings():
	data={}
	q="SELECT * FROM tbl_job INNER JOIN `tbl_employer` USING (`emp_id`) INNER JOIN `tbl_type` USING (type_id) INNER JOIN `tbl_genre` USING (`genre_id`) "
	res=select(q)
	data['jobb']=res

	if "action" in request.args:
		action=request.args['action']
		job_id=request.args['job_id']

	else:
		action=None

	if action=="inactive":
		q="update tbl_job set job_status='0' where job_id='%s'"%(job_id)
		update(q)

		return redirect(url_for('employer.view_job_postings'))


	if action=="active":
		q="update tbl_job set job_status='1' where job_id='%s'"%(job_id)
		update(q)
		return redirect(url_for('employer.view_job_postings'))


	


	return render_template('view_job_postings.html',data=data)


@employer.route('/updatejob',methods=['post','get'])
def updatejob():
	data={}

	job_id=request.args['job_id']


	q="SELECT * FROM tbl_job INNER JOIN `tbl_employer` USING (`emp_id`) INNER JOIN `tbl_type` USING (type_id) INNER JOIN `tbl_genre` USING (`genre_id`) where job_id='%s'"%(job_id)
	res=select(q)
	data['updatejobs']=res



	if "submit" in request.form:
		jt=request.form['job_title']
		hd=request.form['job_desc']
		typ=request.form['type']
		gen=request.form['gen']
		rat=request.form['job_rate']
		jd=request.form['job_duration']
		jl=request.form['job_location']

		emp_id=session['emp_id']
		q="update tbl_job set job_title='%s',job_desc='%s' ,type_id='%s',genre_id='%s',job_rate='%s',job_duration='%s',job_location='%s' where job_id='%s' "%(jt,hd,typ,gen,rat,jd,jl,job_id)
		update(q)
		return redirect(url_for('employer.view_job_postings'))



	return render_template('updatejob.html',data=data)


@employer.route('/employee_viewapplication',methods=['post','get'])
def employee_viewapplication():
	data={}




	q="SELECT * FROM `job_application` INNER JOIN `tbl_job` USING (`job_id`) INNER JOIN `tbl_musician` USING (`msc_id`)"
	res=select(q)
	data['updatejobs']=res


	if "action" in request.args:
		api=request.args['application_id']
		action=request.args['action']

	else:
		action=None


	if action=='accept':
		q="update job_application set status='Accept' where application_id='%s'"%(api)
		update(q)

		return redirect(url_for('employer.employee_viewapplication'))


	if action=='reject':
		q="update job_application set status='Reject' where application_id='%s'"%(api)
		update(q)
		return redirect(url_for('employer.employee_viewapplication'))


	return render_template('employee_viewapplication.html',data=data)


@employer.route('/employee_profile',methods=['post','get'])
def employee_profile():
	data={}
	uname=session['emp_id']




	q="SELECT * FROM `tbl_employer` where emp_id='%s'"%(uname)
	res=select(q)
	data['updateprofile']=res


	if "submit" in request.form:
		name=request.form['name']
		username=request.form['username']
		phone_no=request.args['phone_no']
		aadhar_no=request.args['aadhar_no']
		q="update tbl_employer set emp_name='%s' emp_email='%s' ,emp_no='%s',emp_aadhar='%s' where emp_id='%s'"%(uname)
		update(q)
		return redirect(url_for('employer.employee_profile'))




	return render_template('employee_profile.html',data=data)




