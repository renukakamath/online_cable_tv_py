from flask import *
from database import *

admin=Blueprint('admin',__name__)



@admin.route('/admin_home')
def admin_home():
    return render_template('admin_home.html')

@admin.route('/musician_view')
def musician_view():
    data={}
    q="select * from tbl_musician"
    res=select(q)
    data['viewm']=res
    if "action" in request.args:
          action=request.args['action']
          msc_id=request.args['msc_id']

    else:
          action=None
    if action=="inactive":
          q="update tbl_musician set msc_status='0' where msc_id='%s'"%(msc_id)
          update(q)
          flash("successfully")
          return redirect(url_for("admin.musician_view"))
    if action=="active":
          s="update tbl_musician set msc_status='1' where msc_id='%s'"%(msc_id)
          update(s)
          flash("successfully")
          return redirect(url_for("admin.musician_view"))
    return render_template('musician_view.html',data=data)

@admin.route('/employer_view')
def employer_view():
    data={}
    q="select * from tbl_employer"
    res=select(q)
    data['viewe']=res
    if "action" in request.args:
          action=request.args['action']
          emp_id=request.args['emp_id']

    else:
          action=None
    if action=="inactive":
          q="update tbl_employer set emp_status='0' where emp_id='%s'"%(emp_id)
          update(q)
          flash("successfully")
          return redirect(url_for("admin.employer_view"))
    if action=="active":
          s="update tbl_employer set emp_status='1' where emp_id='%s'"%(emp_id)
          update(s)
          flash("successfully")
          return redirect(url_for("admin.employer_view"))
    return render_template('employer_view.html',data=data)

@admin.route('/genre',methods=['get','post'])
def genre():
    if 'submit' in request.form:
        name=request.form['name']
        q="insert into tbl_genre values(null,'%s',1)"%(name)
        insert(q)
        flash("successfully")
        return redirect(url_for("admin.genre"))
    return render_template('genre.html')



@admin.route('/channelsadd')
def channelsadd():
  if "submit" in request.form:
    name=request.form['name']
    rate=request.form['rate']
    q="insert into tbl_channel values(null,'%s','%s','1')"%(name,rate)
    insert(q)
  return render_template('channelsadd.html')


@admin.route('/channelview')
def channelview():
      data={}
      q="select * from tbl_channel"
      res=select(q)
      data['viewt']=res
      if "action" in request.args:
            action=request.args['action']
            type_id=request.args['type_id']

      else:
            action=None
      if action=="inactive":
            q="update tbl_channel set type_status='0' where type_id='%s'"%(type_id)
            update(q)
            flash("successfully")
            return redirect(url_for("admin.channelview"))
      if action=="active":
            s="update tbl_channel set type_status='1' where type_id='%s'"%(type_id)
            update(s)
            flash("successfully")
            return redirect(url_for("admin.channelview")) 
      return render_template('channelview.html',data=data)



    
    

@admin.route('/type',methods=['get','post'])
def type():
    if 'submit' in request.form:
        name=request.form['name']
        q="insert into tbl_type values(null,'%s',1)"%(name)
        insert(q)
        flash("successfully")
        return redirect(url_for("admin.type"))
    return render_template('type.html')

@admin.route('/type_view')
def type_view():
      data={}
      q="select * from tbl_type"
      res=select(q)
      data['viewt']=res
      if "action" in request.args:
            action=request.args['action']
            type_id=request.args['type_id']

      else:
            action=None
      if action=="inactive":
            q="update tbl_type set type_status='0' where type_id='%s'"%(type_id)
            update(q)
            flash("successfully")
            return redirect(url_for("admin.type_view"))
      if action=="active":
            s="update tbl_type set type_status='1' where type_id='%s'"%(type_id)
            update(s)
            flash("successfully")
            return redirect(url_for("admin.type_view")) 
      return render_template('type_view.html',data=data) 

@admin.route('/genre_view')
def genre_view():
      data={}
      q="select * from tbl_genre"
      res=select(q)
      data['viewg']=res
      if "action" in request.args:
            action=request.args['action']
            genre_id=request.args['genre_id']

      else:
            action=None
      if action=="inactive":
            q="update tbl_genre set genre_status='0' where genre_id='%s'"%(genre_id)
            update(q)
            flash("successfully")
            return redirect(url_for("admin.genre_view"))
      if action=="active":
            s="update tbl_genre set genre_status='1' where genre_id='%s'"%(genre_id)
            update(s)
            flash("successfully")
            return redirect(url_for("admin.genre_view"))
      return render_template('genre_view.html',data=data)

@admin.route('/type_update',methods=['get','post'])
def type_update():
      data={}
      
      type_id=request.args['type_id']
      q="select * from tbl_type where type_id='%s'"%(type_id)
      res=select(q)
      data['up']=res
      
        
      if 'update' in request.form:
        name=request.form['name']
        q="update tbl_type set type_name='%s' where type_id='%s'"%(name,type_id)
        update(q)
        flash("successfully")
        return redirect(url_for("admin.type_view"))
      return render_template('type_update.html',data=data)

@admin.route('/genre_update',methods=['get','post'])
def genre_update():
      data={}
      
      genre_id=request.args['genre_id']
      q="select * from tbl_genre where genre_id='%s'"%(genre_id)
      res=select(q)
      data['up']=res
      
        
      if 'update' in request.form:
        name=request.form['name']
        q="update tbl_genre set genre_name='%s' where genre_id='%s'"%(name,genre_id)
        update(q)
        flash("successfully")
        return redirect(url_for("admin.genre_view"))
      return render_template('genre_update.html',data=data)


@admin.route('/admin_viewapplication',methods=['post','get'])
def admin_viewapplication():
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

    return redirect(url_for('admin.admin_viewapplication'))


  if action=='reject':
    q="update job_application set status='Reject' where application_id='%s'"%(api)
    update(q)
    return redirect(url_for('admin.admin_viewapplication'))


  return render_template('admin_viewapplication.html',data=data)











