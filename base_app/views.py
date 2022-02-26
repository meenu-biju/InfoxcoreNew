from qrcode import *
import qrcode.image.svg
import qrcode
from xhtml2pdf import pisa
from django.core.files import File
from pyqrcode import QRCode
from django.http import HttpResponse
from django.template.loader import get_template
from datetime import *
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from base_app.models import *
from core import settings
import json
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.db.models.deletion import ProtectedError

# Create your views here.


#--------------------ADMIN MODULE--------------------------


def login(request):
    if request.method =='POST':
        if user_registration.objects.filter(email=request.POST['email'], password=request.POST['password'],designation_id=6).exists():
            
            member=user_registration.objects.get(email=request.POST['email'], password=request.POST['password'])
            request.session['Adm_id'] = member.designation_id
            request.session['usernamets1'] = member.fullname
            request.session['usernamehr2'] = member.branch_id
            request.session['usernametsid'] = member.id
            if request.session.has_key('Adm_id'):
                usernamets = request.session['Adm_id']
            if request.session.has_key('usernamets1'):
                usernamets1 = request.session['usernamets1']
            else:
                usernamets1 = "dummy"
            mem=user_registration.objects.filter(designation_id=usernamets) .filter(fullname=usernamets1)
            
            Num= project.objects.count()
            project_details = project.objects.all()

            Number = user_registration.objects.count()
            if request.session.has_key('Adm_id'):
                Adm_id = request.session['Adm_id']
        
            mem2 = user_registration.objects.filter(id=Adm_id)
            Admin1 = designation.objects.get(designation='Admin')
            Admin2 = user_registration.objects.filter(designation = Admin1)

            Trainer1 = designation.objects.get(designation='Trainer')
            num1=user_registration.objects.filter(designation=Trainer1).count()

            # return redirect('BRadmin_profiledash')
            return render(request,'BRadmin_profiledash.html',{'mem':mem ,'proj_det':project_details,'num':Num,'Admin1':Admin2,'mem2':mem2,'number':Number,'num1':num1})
        elif user_registration.objects.filter(email=request.POST['email'], password=request.POST['password'],designation_id=7).exists():
            
            member=user_registration.objects.get(email=request.POST['email'], password=request.POST['password'])
            request.session['Adm_id'] = member.designation_id
            request.session['usernamets1'] = member.fullname
            request.session['usernamehr2'] = member.branch_id
            request.session['usernametsid'] = member.id
            if request.session.has_key('Adm_id'):
                usernamets = request.session['Adm_id']
            if request.session.has_key('usernamets1'):
                usernamets1 = request.session['usernamets1']
            else:
                usernamets1 = "dummy"
            mem=user_registration.objects.filter(designation_id=usernamets) .filter(fullname=usernamets1)
            Num2= project.objects.count()
            Num = user_registration.objects.count()
            if request.session.has_key('Adm_id'):
                Adm_id = request.session['Adm_id']
        
            mem3 = user_registration.objects.filter(id=Adm_id)
            Manager1 = designation.objects.get(designation='Manager')
            Manager2 = user_registration.objects.filter(designation = Manager1)

            Trainer = designation.objects.get(designation='Trainer')
            num1=user_registration.objects.filter(designation=Trainer).count()
            return render(request,'MAN_profiledash.html',{'mem':mem,'Manager1':Manager2,'mem3':mem3,'num':Num,'num1':num1,'Num2':Num2})    
            
        else:
            message = "invalid username or password"
            return render(request ,'login.html',{'message':message})
    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')


def index(request):
    return render(request,"BRadmin_index.html")


def newdept(request):
    condent = department.objects.all()
    return render(request,'BRadmin_Department.html',{'condent':condent})

def add_dept(request):
    return render(request,"BRadmin_add_dept.html")

def add_deptsave(request):
    if request.method == 'POST':
        depart = request.POST['dept']
        a=department(department=depart)
        a.save()
        m="Successfully department added"
    return render(request,'BRadmin_add_dept.html',{'m':m})


def delete(request, id):
    
    m = department.objects.get(id=id)
    m.delete()
    # try:
    #     obj = get_object_or_404(department,id=id)
    #     obj.delete()
    #     return redirect('/base_app/newdept')
    # except ProtectedError:
    #      messages.error(request, "Sorry can't be deleted.") 
    #      return redirect('/base_app/newdept')
    return redirect('/base_app/newdept')
        
    

#safdhar
def upcoming(request):
    return render(request,'upcomingprojects.html')

def viewprojectform(request):
	if request.method == 'POST':
		sc1 = request.POST['Department']
		sc2 = request.POST['designation']
		sc3 = request.POST['projectname']
		sc4 = request.POST['discrip']
		sc5 = request.POST['start']
		sc6 = request.POST['end']
		
		
		progress=0
		catry = project_taskassign(project_id=sc3,
                                  description=sc4,
                                  startdate=sc5, enddate=sc6,extension='0',designation=sc2,department=sc1)
		catry.save()
	dept = department.objects.all()
	desig = designation.objects.all()
	proj = project.objects.all()
	return render(request,'viewprojects.html',{'desig':desig,'dept':dept,'project':proj})
def acceptedprojects(request):
	pro =project.objects.filter(status='Accepted')
	return render(request,'acceptedprojects.html',{'projects': pro})

def rejected(request):
	pro =project.objects.filter(status='Rejected')
	return render(request,'rejectedprojectes.html',{'projects': pro})

def createproject(request):
	if request.method == 'POST':
		sc1 = request.POST['Department']
		sc2 = request.POST['designation']
		sc3 = request.POST['projectname']
		sc4 = request.POST['discrip']
		sc5 = request.POST['start']
		sc6 = request.POST['end']
		ogo = request.FILES['img[]']
		print(sc5,sc6,ogo,sc1)
		progress=0
		catry = project(designation_id=sc2,department_id=sc1,project=sc3,
                                  description=sc4,
                                  startdate=sc5, enddate=sc6, files=ogo,progress=progress)
		catry.save()
	dept = department.objects.all()
	desig = designation.objects.all()	
	return render(request,'createproject.html',{'dept':dept,'desig':desig})
   


def upcomingpro(request):
	pro =project.objects.all()
	return render(request,'upcomingpro.html',{'projects': pro})

def seradmintraineedesi1(request):
    dept_id = request.GET.get('dept_id')
    Desig = designation.objects.filter(department_id=dept_id)
    print(Desig)
    return render(request, 'dropdown.html', {'Desig': Desig})

def seradmindesig(request):
	print("safdhar")
	dept_id = request.GET.get('dept_id')
	Desig = designation.objects.filter(department_id=dept_id)
	print(Desig)
	return render(request, 'giveprojectdropdown.html', {'Desig': Desig})


#nimisha
def BRadmin_tasks(request):
    return render(request,'BRadmin_tasks.html')

def BRadmin_givetask(request):
    if request.method == 'POST':
        sc1 = request.POST['Department']
        sc2 = request.POST['designation']
        sc3 = request.POST['projectname']
        sc4 = request.POST['discrip']
        sc5 = request.POST['start']
        sc6 = request.POST['end']
        ogo = request.FILES['img[]']
        print(sc1,sc2)
        progress=0
        catry = project_taskassign(description=sc4,files=ogo,
                                  startdate=sc5, enddate=sc6,extension='0',designation=sc2,department=sc1)
        catry.save()
    dept = department.objects.all()
    desig = designation.objects.all()
    proj = project.objects.all()
    emp = user_registration.objects.all()
    return render(request,'BRadmin_givetask.html',{'desig':desig,'dept':dept,'project':proj,'emp':emp})


def desi(request):   
    dept_id = request.GET.get('dept_id')
    Desig = designation.objects.filter(department_id=dept_id)
    print(Desig)
    return render(request, 'designation3.html', {'Desig': Desig})

def emp(request):   
    dept_id = request.GET.get('dept_id')
    desig_id = request.GET.get('desig_id')
    emp = user_registration.objects.filter(department_id=dept_id).filter(designation_id=desig_id)
    print(emp)
    return render(request, 'employee3.html', {'emp': emp})


def BRadmin_currenttasks(request):
	names =trainer_task.objects.filter(status='Progressing')
	return render(request,'BRadmin_currenttask.html',{'names': names})

def BRadmin_previoustasks(request):
	names =trainer_task.objects.filter(status='Completed')
	return render(request,'BRadmin_previoustasks.html',{'names': names})



#akhil p t

def BRadmin_Reportedissue(request):
    designations=designation.objects.all()
    return render(request, 'BRadmin_Reportedissue.html',{'designation':designations})

def BRadmin_ReportedissueShow(request,id):
    designations=designation.objects.get(id=id)
    user=user_registration.objects.filter(designation=designations)
    reported_issues=reported_issue.objects.all()
    return render(request,'BRadmin_ReportedissueShow.html',{'designation':designations,'reported_issue':reported_issues,'user_registration':user})

def BRadmin_ReportedissueShow1(request,id):
    reported_issues=reported_issue.objects.get(id=id)
    return render(request,'BRadmin_ReportedissueShow1.html',{'reported_issue':reported_issues}) 


#sharon

def BRadmin_python(request):
    project_details = project.objects.all()
    return render(request,'BRadmin_projects.html',{'proj_det':project_details})
def BRadmin_employees(request):
    project_details = project.objects.all()
    depart =department.objects.all()
    return render(request,'BRadmin_employees.html',{'proj_det':project_details,'department':depart})

def BRadmin_profiledash(request):
    Num= project.objects.count()
    project_details = project.objects.all()

    Number = user_registration.objects.count()
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
  
    mem = user_registration.objects.filter(id=Adm_id)
    Admin1 = designation.objects.get(designation='Admin')
    Admin2 = user_registration.objects.filter(designation = Admin1)

    Trainer1 = designation.objects.get(designation='Trainer')
    num1=user_registration.objects.filter(designation=Trainer1).count()
    return render(request,'BRadmin_profiledash.html',{'proj_det':project_details,'num':Num,'Admin1':Admin2,'mem':mem,'number':Number,'num1':num1})

def BRadmin_projects(request,id):
    Num= project.objects.filter(status='accepted').filter(department=id).count()
    project_details = project.objects.all()
    depart =department.objects.get(id=id)
    id=id
 
    # for i in project_details:
    #     if i.status == "rejected"  :  
    #         Num =Num-1
    #         break
    return render(request,'BRadmin_projects.html',{'proj_det':project_details,'num':Num,'department':depart,'id':id})
def BRadmin_proj_list(request,id):
    project_details = project.objects.filter(department=id)
    print (project_details.count())
    return render(request,'BRadmin_proj_list.html',{'proj_det':project_details})
def BRadmin_proj_det(request,id):
    project_details = project.objects.get(id=id)
    return render(request,'BRadmin_proj_det.html',{'proj_det':project_details})
def BRadmin_proj_mngrs(request,id):
    project_details = project.objects.get(id=id)
    return render(request,'BRadmin_proj_mngrs.html',{'proj_det':project_details})
def BRadmin_proj_mangrs1(request,id):
    project_details = project.objects.get(id=id) 
    return render(request,'BRadmin_proj_mangrs1.html',{'proj_det':project_details})
def BRadmin_proj_mangrs2(request,id):
    project_details = project.objects.get(id=id) 
    project_task = project_taskassign.objects.all()
    return render(request,'BRadmin_proj_mangrs2.html',{'proj_task':project_task,'proj_det':project_details})
def BRadmin_daily_report(request,id):
    project_task = project_taskassign.objects.get(id=id)
    tester =tester_status.objects.all()
    return render(request,'BRadmin_daily_report.html',{'proj_task':project_task,'test':tester,})
def BRadmin_developers(request,id):
    project_details = project.objects.get(id=id) 
    project_task = project_taskassign.objects.filter(tl_id = id)
    return render(request,'BRadmin_developers.html',{'proj_task':project_task,'proj_det':project_details})


#subeesh

def BRadmin_employees_new(request):
    project_details = project.objects.all()
    departments = department.objects.all()
    return render(request,'BRadmin_employees_show.html',{'project':project_details,'department':departments})

def BRadmin_python_new(request):
    project_details = project.objects.all()
    return render(request,'BRadmin_projects.html',{'project':project_details})

def BRadmin_projects_new(request, id):
    Num = project.objects.filter(status='accepted').filter(department=id).count()
    project_details = project.objects.all()
    departments = department.objects.get(id=id)
    id=id
    # for i in project_details:
    #     if i.progress == "in progress":  
    #         Num = Num-1
    #         break
    return render(request,'BRadmin_projects_show.html',{'project':project_details,'num':Num, 'department':departments,'id':id})
   


def BRadmin_proj_cmpltd_new(request, id):
    project_details=project.objects.filter(department=id)
    print (project_details.count())
    return render(request,'BRadmin_proj_cmpltd_show.html',{'project': project_details})


def BRadmin_cmpltd_proj_det_new(request, id):
    project_details = project.objects.get(id=id)

    return render(request,'BRadmin_cmpltd_proj_det_show.html',{'project': project_details})

def BRadmin_proj_mngrs_new(request, id):
    project_details = project.objects.get(id=id)
    return render(request,'BRadmin_proj_mngrs_show.html', {'project': project_details})

def BRadmin_proj_mangrs1_new(request,id):
    project_details = project.objects.get(id=id)
    return render(request,'BRadmin_proj_mangrs1_show.html', {'project': project_details})

def BRadmin_proj_mangrs2_new(request, id):
    project_details = project.objects.get(id=id)
    project_task = project_taskassign.objects.all()
    return render(request,'BRadmin_proj_mangrs2_show.html', {'project':project_details,'project_taskassign':project_task})

def BRadmin_developers_new(request, id):
    project_details = project.objects.get(id=id)
    project_task = project_taskassign.objects.filter(tl_id = id)
    return render(request,'BRadmin_developers_show.html', {'project':project_details,'project_taskassign':project_task})

def BRadmin_daily_report_new(request, id):
    project_task = project_taskassign.objects.get(id=id)
    tester = tester_status.objects.all()
    return render(request,'BRadmin_daily_report_show.html', {'project':project_task,'tester_status':tester})
    

# #anandhu

   
def BRadmin_department_new(request):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
    mem = user_registration.objects.filter(id=Adm_id)
    return render(request,'BRadmin_department_new.html',{'mem':mem})
def BRadmin_python(request):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
 
    mem = user_registration.objects.filter(id=Adm_id)
    return render(request,'BRadmin_python.html',{'mem':mem})
def BRadmin_projectman(request):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
    mem = user_registration.objects.filter(id=Adm_id)
    project_name = project.objects.all()
    Project_man= designation.objects.get(designation='Project manager')
    Project_man_data=user_registration.objects.filter(designation=Project_man)
    return render(request,'BRadmin_projectman.html',{'pro_man_data':Project_man_data,'mem':mem,'project_name':project_name})
def BRadmin_proname(request,id):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
 
    mem = user_registration.objects.filter(id=Adm_id)
    Project_man_data = user_registration.objects.get(id = id)
    return render(request,'BRadmin_proname.html',{'pro_man_data':Project_man_data,'mem':mem})
def BRadmin_proinvolve(request,id):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
 
    mem = user_registration.objects.filter(id=Adm_id)
    Pro_data = project.objects.filter(user_id = id)
    return render(request,'BRadmin_proinvolve.html',{'pro_data':Pro_data,'mem':mem})
def BRadmin_promanatten(request,id):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']    
    mem = user_registration.objects.get(id=id)
    id = id
    return render(request,'BRadmin_promanatten.html',{'mem':mem,'id':id})

def BRadmin_promanattensort(request,id):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
 
    mem = user_registration.objects.filter(id=Adm_id)
    if request.method == "POST":
        fromdate = request.POST.get('fromdate')
        todate = request.POST.get('todate') 
        mem1 = attendance.objects.filter(date__range=[fromdate,todate]).filter(user_id=id)
    return render(request, 'BRadmin_promanatten.html',{'mem1':mem1,'mem':mem})

def BRadmin_HRattendance(request,id):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
 
    mem = user_registration.objects.get(id=id)
    id = id
    return render(request,'BRadmin_HRattendance.html',{'mem':mem,'id':id})

def BRadmin_HRattendancesort(request,id):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
 
    mem = user_registration.objects.filter(id=Adm_id)
    if request.method == "POST":
        fromdate = request.POST.get('fromdate')
        todate = request.POST.get('todate') 
        mem1 = attendance.objects.filter(date__range=[fromdate,todate]).filter(user_id=id)        
    return render(request, 'BRadmin_HRattendance.html',{'mem1':mem1,'mem':mem}) 
           
def BRadmin_HRlist(request):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
 
    mem = user_registration.objects.filter(id = Adm_id)
    HR_man= designation.objects.get(designation ='HR')
    project_name = project.objects.all()
    HR_man_data = user_registration.objects.filter(designation=HR_man)
    return render(request,'BRadmin_HRlist.html',{'hr_man_data':HR_man_data,'mem':mem,'Project_name':project_name})
def BRadmin_HRprofile(request,id):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
 
    mem = user_registration.objects.filter(id=Adm_id)
    HR_man_data=user_registration.objects.get(id = id)
    return render(request,'BRadmin_HRprofile.html',{'hr_man_data':HR_man_data,'mem':mem})


def BRadmin_TLattendance(request,id):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
 
    mem = user_registration.objects.filter(id=Adm_id)
    id = id
    return render(request,'BRadmin_TLattendance.html',{'mem':mem,'id':id})

def BRadmin_TLattendancesort(request,id):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
 
    mem = user_registration.objects.get(id=id)
    if request.method == "POST":
        fromdate = request.POST.get('fromdate')
        todate = request.POST.get('todate') 
        mem1 = attendance.objects.filter(date__range=[fromdate,todate]).filter(user_id=id)          
    return render(request, 'BRadmin_TLattendance.html',{'mem1':mem1,'mem':mem})      
def BRadmin_TLip(request,id):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
 
    mem = user_registration.objects.filter(id=Adm_id)
    TL_data = project.objects.filter(user_id = id)
    return render(request,'BRadmin_TLip.html',{'tL_data': TL_data,'mem':mem})
def BRadmin_TLlist(request):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
    mem = user_registration.objects.filter(id=Adm_id)
    project_name = project.objects.all()
    Team_leader= designation.objects.get(designation='Team Leaders')
    Team_leader_data=user_registration.objects.filter(designation=Team_leader)
    return render(request,'BRadmin_TLlist.html',{'team_leader_data':Team_leader_data,'mem':mem,'project_name':project_name})
def BRadmin_TLprofile(request,id):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
 
    mem = user_registration.objects.filter(id=Adm_id)
    Team_leader_data=user_registration.objects.get(id = id)
    return render(request,'BRadmin_TLprofile.html',{'team_leader_data':Team_leader_data,'mem':mem})    



def BRadmin_dev_details(request):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
    mem = user_registration.objects.filter(id=Adm_id)
    project_name = project.objects.all()
    Developers= designation.objects.get(designation='developer')
    Developers_data=user_registration.objects.filter(designation=Developers) 
    return render(request,'BRadmin_dev_details.html',{'developers_data':Developers_data,'mem':mem,'project_name':project_name})
def BRadmin_dev_profile(request,id):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
 
    mem = user_registration.objects.filter(id=Adm_id)
    Developer_data=user_registration.objects.get(id = id)
    return render(request,'BRadmin_dev_profile.html',{'developer_data':Developer_data,'mem':mem})
def BRadmin_dev_involved(request,id):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
 
    mem = user_registration.objects.filter(id=Adm_id)
    Dev_data = project.objects.filter(user_id = id)
    return render(request,'BRadmin_dev_involved.html',{'dev_data':Dev_data,'mem':mem})
def BRadmin_dev_attendance(request,id):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
 
    mem = user_registration.objects.get(id=id)
    id = id
    return render(request,'BRadmin_dev_attendance.html',{'mem':mem,'id':id})     

def BRadmin_dev_attendancesort(request,id):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
    mem = user_registration.objects.filter(id=Adm_id)
    if request.method == "POST":
        fromdate = request.POST.get('fromdate')
        todate = request.POST.get('todate') 
        mem1 = attendance.objects.filter(date__range=[fromdate,todate]).filter(user_id = id)   
    return render(request, 'BRadmin_dev_attendance.html',{'mem1':mem1,'mem':mem})    

def page1(request):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
 
    mem = user_registration.objects.filter(id=Adm_id)
    return render(request,'BRadmin_page1.html',{'mem':mem})    
def page2(request):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
 
    mem = user_registration.objects.filter(id=Adm_id)
    return render(request,'BRadmin_page2.html',{'mem':mem}) 

#praveen

def BRadmin_trainerstable(request):
    Trainer = designation.objects.get(designation='Trainer')
    trainers_data=user_registration.objects.filter(designation=Trainer)
    topics=topic.objects.all()
    return render(request,'BRadmin_trainerstable.html',{'trainers_data':trainers_data,'topics':topics})
def BRadmin_Training(request,id):
    #team=create_team.objects.filter(user_id=id)
    #return render(request,'BRadmin_Training.html',{'team':team})
        #team=create_team.objects.all()
    user=user_registration.objects.filter(id=id)
    team=create_team.objects.all()
    return render(request,'BRadmin_Training.html',{'team':team,'user':user})
def BRadmin_trainingteam1(request,id):
    id=id
    Trainee = designation.objects.get(designation='Trainee')
    num=user_registration.objects.filter(designation=Trainee).filter(team=id).count()
    num1=topic.objects.filter(team=id).count()
    return render(request,'BRadmin_trainingteam1.html',{'id':id,'num':num,'num1':num1})
def BRadmin_traineestable(request,id):
    Trainee = designation.objects.get(designation='Trainee')
    trainees_data=user_registration.objects.filter(designation=Trainee).filter(team=id)
    return render(request,'BRadmin_traineestable.html',{'trainees_data':trainees_data}) 
def BRadmin_trainingprofile(request,id):
    trainees_data=user_registration.objects.get(id=id)
    #Trainee = designation.objects.get(designation='Trainee')
    #trainees_data=user_registration.objects.filter(designation=Trainee)
    user=user_registration.objects.get(id=id)
    num=trainer_task.objects.filter(user=user).filter(status='Completed').count()
    return render(request,'BRadmin_trainingprofile.html',{'trainees_data':trainees_data,'num':num})
def BRadmin_completedtasktable(request,id):
    user=user_registration.objects.get(id=id)
    task=trainer_task.objects.filter(user=user)
    return render(request,'BRadmin_completedtasktable.html',{'task_data':task})
def BRadmin_topictable(request,id):
    topics=topic.objects.filter(team=id)
    return render(request,'BRadmin_topictable.html',{'topics':topics})
    

#anwar

def BRadmin_View_Trainers(request):
    projectname=project.objects.all()
    trainer=designation.objects.get(designation='Trainer')
    userreg=user_registration.objects.filter(designation=trainer)
    return render(request,'BRadmin_View_Trainers.html', {'user_registration':userreg, 'project':projectname})

def BRadmin_View_Trainerprofile(request,id):
    userreg=user_registration.objects.get(id=id)
    return render(request,'BRadmin_View_Trainerprofile.html', {'user_registration':userreg})


def BRadmin_View_Currenttraineesoftrainer(request,id):
   
    user=user_registration.objects.filter(id=id)
    trainee=designation.objects.get(designation='Trainee')
    user2=user_registration.objects.filter(designation=trainee)
    
    return render(request,'BRadmin_View_Currenttraineesoftrainer.html',{'user_registration':user,'user_registration2':user2})

def BRadmin_View_Previoustraineesoftrainer(request,id):
   
    user=user_registration.objects.filter(id=id)
    trainee=designation.objects.get(designation='Trainee')
    user2=user_registration.objects.filter(designation=trainee)

    return render(request,'BRadmin_View_Previoustraineesoftrainer.html',{'user_registration':user,'user_registration2':user2})

def BRadmin_View_Currenttraineeprofile(request,id):
    userreg=user_registration.objects.get(id=id)
    return render(request,'BRadmin_View_Currenttraineeprofile.html', {'user_registration':userreg})

def BRadmin_View_Currenttraineetasks(request,id):
    # user=user_registration.objects.get(id=id)
    tasks=trainer_task.objects.filter(user=id)
    return render(request,'BRadmin_View_Currenttraineetasks.html',{'trainer_task':tasks})

def BRadmin_View_Currenttraineeattendance(request,id):
    usr=user_registration.objects.get(id=id)
    return render(request,'BRadmin_View_Currenttraineeattendance.html', {'user_registration':usr})




def BRadmin_View_Previoustraineeprofile(request,id):
    usr=user_registration.objects.get(id=id)
    return render(request,'BRadmin_View_Previoustraineeprofile.html', {'user_registration':usr})

def BRadmin_View_Previoustraineetasks(request,id):
    user=user_registration.objects.get(id=id)
    tasks=trainer_task.objects.filter(user=user)
    return render(request,'BRadmin_View_Previoustraineetasks.html',{'trainer_task':tasks})

def BRadmin_View_Previoustraineeattendance(request,id):
    usr=user_registration.objects.get(id=id)
    return render(request,'BRadmin_View_Previoustraineeattendance.html', {'user_registration':usr})




def BRadmin_View_Trainerattendance(request,id):
    usr=user_registration.objects.get(id=id)
    return render(request,'BRadmin_View_Trainerattendance.html', {'user_registration':usr})


def BRadmin_ViewTrainerattendancesort(request,id):
    # usr=user_registration.objects.get(id=id)
    if request.method == "POST":
        fromdate = request.POST.get('fromdate')
        todate = request.POST.get('todate') 
        adata =attendance.objects.filter(date__range=[fromdate,todate]).filter(user_id=id)
        
    return render(request,'BRadmin_View_Trainerattendance.html',{'adata':adata})



def BRadmin_ViewCurrenttraineeattendancesort(request,id):
    usr=user_registration.objects.get(id=id)
    if request.method == "POST":
        fromdate = request.POST.get('fromdate')
        todate = request.POST.get('todate') 
        adata =attendance.objects.filter(date__range=[fromdate,todate]).filter(user_id=id)
        
    return render(request,'BRadmin_View_Currenttraineeattendance.html',{'adata':adata,'user_registration':usr})

def BRadmin_ViewPrevioustraineeattendancesort(request,id):
    usr=user_registration.objects.get(id=id)
    if request.method == "POST":
        fromdate = request.POST.get('fromdate')
        todate = request.POST.get('todate') 
        adata = attendance.objects.filter(date__range=[fromdate,todate]).filter(user_id=id)
        
    return render(request,'BRadmin_View_Previoustraineeattendance.html',{'adata':adata,'user_registration':usr})


def BRadmin_dev_attendance(request):
    return render(request,'BRadmin_dev_attendance.html')           
def page1(request):
 
    dpt=department.objects.all()
    dsg=designation.objects.all()
    userreg=user_registration.objects.all()
    return render(request,'BRadmin_page1.html', {'department':dpt,'designation':dsg,'user_registration':userreg})  

def page3(request):
    
    if request.method == "POST":
        empname1=request.POST.get('empname')
        atten=attendance.objects.all()
    return render(request,'BRadmin_page3.html',{'atten':atten,'empname1':empname1}) 
   

def desi(request):   
    dept_id = request.GET.get('dept_id')
    departments=department.objects.all()
    Desig = designation.objects.filter(department_id=dept_id)
    return render(request, 'designation.html', {'Desig': Desig,'departments':departments})



def emp(request):   
    dept_id = request.GET.get('dept_id')
    desig_id = request.GET.get('desig_id')
    dept=department.objects.filter(id=dept_id)
    desi=designation.objects.filter(id=desig_id)
    user=user_registration.objects.all()
    print(dept)
    print(desi)
    return render(request, 'employee.html',{'user':user,'dept':dept,'desi':desi})

#-----------------END----------------------


#-------------------MANAGER MODULE-------------------------



#--------------------------- Anandhu ---------------------------


# def man_login(request):
#     if request.method =='POST':
#         if user_registration.objects.filter(email=request.POST['email'], password=request.POST['password'],designation_id=7).exists():
            
#             member=user_registration.objects.get(email=request.POST['email'], password=request.POST['password'])
#             request.session['Adm_id'] = member.designation_id
#             request.session['usernamets1'] = member.fullname
#             request.session['usernamehr2'] = member.branch_id
#             request.session['usernametsid'] = member.id
#             if request.session.has_key('Adm_id'):
#                 usernamets = request.session['Adm_id']
#             if request.session.has_key('usernamets1'):
#                 usernamets1 = request.session['usernamets1']
#             else:
#                 usernamets1 = "dummy"
#             mem=user_registration.objects.filter(designation_id=usernamets) .filter(fullname=usernamets1)
#             return render(request,'MAN_profiledash.html',{'mem':mem})
            
#         else:
#             message = "invalid username or password"
#             return render(request ,'MAN_Login.html',{'message':message})
#     return render(request, 'MAN_Login.html')

# def man_logout(request):
#     auth.logout(request)
#     return render(request, 'MAN_Login.html')



# def MAN_Login(request):
#     return render(request,'MAN_Login.html')

# def MAN_home(request):
#     if request.method =='POST':
#         if user_registration.objects.filter(email=request.POST['email'], password=request.POST['password']).exists():
#             member=user_registration.objects.get(email=request.POST['email'], password=request.POST['password'])
#             request.session['Adm_id'] = member.id
#             return render(request, 'MAN_sec.html', {'member':member})

#         else:
#             context={'msg':'Invalid uname or password'}
#             return render(request,'MAN_login.html',context)

def MAN_index(request):
    return render(request,'MAN_index.html')

def MAN_profiledash(request):
    Num2= project.objects.count()
    Num = user_registration.objects.count()
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
 
    mem = user_registration.objects.filter(id=Adm_id)
    Manager1 = designation.objects.get(designation='Manager')
    Manager2 = user_registration.objects.filter(designation = Manager1)

    Trainer = designation.objects.get(designation='Trainer')
    num1=user_registration.objects.filter(designation=Trainer).count()

    return render(request,'MAN_profiledash.html',{'Manager1':Manager2,'mem':mem,'num':Num,'num1':num1,'Num2':Num2})   

def MAN_employees(request):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
 
    mem = user_registration.objects.filter(id=Adm_id)
    return render(request,'MAN_employees.html',{'mem':mem})
def MAN_python(request):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
 
    mem = user_registration.objects.filter(id=Adm_id)
    return render(request,'MAN_python.html',{'mem':mem})
def MAN_projectman(request):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
    mem = user_registration.objects.filter(id=Adm_id)
    project_name = project.objects.all()
    Project_man= designation.objects.get(designation='Project manager')
    Project_man_data=user_registration.objects.filter(designation=Project_man)
    return render(request,'MAN_projectman.html',{'pro_man_data':Project_man_data,'mem':mem,'project_name':project_name})
def MAN_proname(request,id):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
 
    mem = user_registration.objects.filter(id=Adm_id)
    Project_man_data = user_registration.objects.get(id = id)
    return render(request,'MAN_proname.html',{'pro_man_data':Project_man_data,'mem':mem})
def MAN_proinvolve(request,id):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
 
    mem = user_registration.objects.filter(id=Adm_id)
    Pro_data = project.objects.filter(user_id = id)
    return render(request,'MAN_proinvolve.html',{'pro_data':Pro_data,'mem':mem})
def MAN_promanatten(request,id):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']    
    mem = user_registration.objects.get(id=id)
    id = id
    return render(request,'MAN_promanatten.html',{'mem':mem,'id':id})

def MAN_promanattensort(request,id):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
 
    mem = user_registration.objects.filter(id=Adm_id)
    if request.method == "POST":
        fromdate = request.POST.get('fromdate')
        todate = request.POST.get('todate') 
        mem1 = attendance.objects.filter(date__range=[fromdate,todate]).filter(user_id=id)
    return render(request, 'MAN_promanatten.html',{'mem1':mem1,'mem':mem})

def MAN_HRattendance(request,id):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
 
    mem = user_registration.objects.get(id=id)
    id = id
    return render(request,'MAN_HRattendance.html',{'mem':mem,'id':id})

def MAN_HRattendancesort(request,id):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
 
    mem = user_registration.objects.filter(id=Adm_id)
    if request.method == "POST":
        fromdate = request.POST.get('fromdate')
        todate = request.POST.get('todate') 
        mem1 = attendance.objects.filter(date__range=[fromdate,todate]).filter(user_id=id)        
    return render(request, 'MAN_HRattendance.html',{'mem1':mem1,'mem':mem}) 
           
def MAN_HRlist(request):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
 
    mem = user_registration.objects.filter(id = Adm_id)
    HR_man= designation.objects.get(designation ='HR manager')
    project_name = project.objects.all()
    HR_man_data = user_registration.objects.filter(designation=HR_man)
    return render(request,'MAN_HRlist.html',{'hr_man_data':HR_man_data,'mem':mem,'Project_name':project_name})
def MAN_HRprofile(request,id):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
 
    mem = user_registration.objects.filter(id=Adm_id)
    HR_man_data=user_registration.objects.get(id = id)
    return render(request,'MAN_HRprofile.html',{'hr_man_data':HR_man_data,'mem':mem})


def MAN_TLattendance(request,id):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
 
    mem = user_registration.objects.filter(id=Adm_id)
    id = id
    return render(request,'MAN_TLattendance.html',{'mem':mem,'id':id})

def MAN_TLattendancesort(request,id):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
 
    mem = user_registration.objects.get(id=id)
    if request.method == "POST":
        fromdate = request.POST.get('fromdate')
        todate = request.POST.get('todate') 
        mem1 = attendance.objects.filter(date__range=[fromdate,todate]).filter(user_id=id)          
    return render(request, 'MAN_TLattendance.html',{'mem1':mem1,'mem':mem})      
def MAN_TLip(request,id):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
 
    mem = user_registration.objects.filter(id=Adm_id)
    TL_data = project.objects.filter(user_id = id)
    return render(request,'MAN_TLip.html',{'tL_data': TL_data,'mem':mem})
def MAN_TLlist(request):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
    mem = user_registration.objects.filter(id=Adm_id)
    project_name = project.objects.all()
    Team_leader= designation.objects.get(designation='Team Leaders')
    Team_leader_data=user_registration.objects.filter(designation=Team_leader)
    return render(request,'MAN_TLlist.html',{'team_leader_data':Team_leader_data,'mem':mem,'project_name':project_name})
def MAN_TLprofile(request,id):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
 
    mem = user_registration.objects.filter(id=Adm_id)
    Team_leader_data=user_registration.objects.get(id = id)
    return render(request,'MAN_TLprofile.html',{'team_leader_data':Team_leader_data,'mem':mem})    



def MAN_dev_details(request):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
    mem = user_registration.objects.filter(id=Adm_id)
    project_name = project.objects.all()
    Developers= designation.objects.get(designation='Developers')
    Developers_data=user_registration.objects.filter(designation=Developers) 
    return render(request,'MAN_dev_details.html',{'developers_data':Developers_data,'mem':mem,'project_name':project_name})
def MAN_dev_profile(request,id):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
 
    mem = user_registration.objects.filter(id=Adm_id)
    Developer_data=user_registration.objects.get(id = id)
    return render(request,'MAN_dev_profile.html',{'developer_data':Developer_data,'mem':mem})
def MAN_dev_involved(request,id):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
 
    mem = user_registration.objects.filter(id=Adm_id)
    Dev_data = project.objects.filter(user_id = id)
    return render(request,'MAN_dev_involved.html',{'dev_data':Dev_data,'mem':mem})
def MAN_dev_attendance(request,id):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
 
    mem = user_registration.objects.get(id=id)
    id = id
    return render(request,'MAN_dev_attendance.html',{'mem':mem,'id':id})     

def MAN_dev_attendancesort(request,id):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
    mem = user_registration.objects.filter(id=Adm_id)
    if request.method == "POST":
        fromdate = request.POST.get('fromdate')
        todate = request.POST.get('todate') 
        mem1 = attendance.objects.filter(date__range=[fromdate,todate]).filter(user_id = id)   
    return render(request, 'MAN_dev_attendance.html',{'mem1':mem1,'mem':mem})    

def page1(request):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
 
    mem = user_registration.objects.filter(id=Adm_id)
    return render(request,'MAN_page1.html',{'mem':mem})    
def page2(request):
    if request.session.has_key('Adm_id'):
        Adm_id = request.session['Adm_id']
 
    mem = user_registration.objects.filter(id=Adm_id)
    return render(request,'MAN_page2.html',{'mem':mem}) 

    
#--------------------------- Anandhu view end ---------------------------

#-------------------MEENU------------------------

def man_newdept(request):
    condent = department.objects.all()
    return render(request,'man_Department.html',{'condent':condent})

def man_dept(request):
    return render(request,"man_add_dept.html")

def man_add_deptsave(request):
    if request.method == 'POST':
        depart = request.POST['dept']
        a=department(department=depart)
        a.save()
        m="Successfully department added"
    return render(request,'man_add_dept.html',{'m':m})


def man_delete(request, id):
    
    m = department.objects.get(id=id)
    m.delete()
    # try:
    #     obj = get_object_or_404(department,id=id)
    #     obj.delete()
    #     return redirect('/base_app/newdept')
    # except ProtectedError:
    #      messages.error(request, "Sorry can't be deleted.") 
    #      return redirect('/base_app/newdept')
    return redirect('/base_app/man_newdept')
        
    

#--------------------------- Anwar -------------------------------------


def MAN_View_Trainers(request):
    projectname=project.objects.all()
    trainer=designation.objects.get(designation='Trainer')
    userreg=user_registration.objects.filter(designation=trainer)
    return render(request,'MAN_View_Trainers.html', {'user_registration':userreg, 'project':projectname})

def MAN_View_Trainerprofile(request,id):
    userreg=user_registration.objects.get(id=id)
    return render(request,'MAN_View_Trainerprofile.html', {'user_registration':userreg})


def MAN_View_Currenttraineesoftrainer(request,id):
   
    user=user_registration.objects.filter(id=id)
    trainee=designation.objects.get(designation='Trainee')
    user2=user_registration.objects.filter(designation=trainee)
    
    return render(request,'MAN_View_Currenttraineesoftrainer.html',{'user_registration':user,'user_registration2':user2})

def MAN_View_Previoustraineesoftrainer(request,id):
   
    user=user_registration.objects.filter(id=id)
    trainee=designation.objects.get(designation='Trainee')
    user2=user_registration.objects.filter(designation=trainee)

    return render(request,'MAN_View_Previoustraineesoftrainer.html',{'user_registration':user,'user_registration2':user2})

def MAN_View_Currenttraineeprofile(request,id):
    userreg=user_registration.objects.get(id=id)
    return render(request,'MAN_View_Currenttraineeprofile.html', {'user_registration':userreg})

def MAN_View_Currenttraineetasks(request,id):
    # user=user_registration.objects.get(id=id)
    tasks=trainer_task.objects.filter(user=id)
    return render(request,'MAN_View_Currenttraineetasks.html',{'trainer_task':tasks})

def MAN_View_Currenttraineeattendance(request,id):
    usr=user_registration.objects.get(id=id)
    return render(request,'MAN_View_Currenttraineeattendance.html', {'user_registration':usr})




def MAN_View_Previoustraineeprofile(request,id):
    usr=user_registration.objects.get(id=id)
    return render(request,'MAN_View_Previoustraineeprofile.html', {'user_registration':usr})

def MAN_View_Previoustraineetasks(request,id):
    user=user_registration.objects.get(id=id)
    tasks=trainer_task.objects.filter(user=user)
    return render(request,'MAN_View_Previoustraineetasks.html',{'trainer_task':tasks})

def MAN_View_Previoustraineeattendance(request,id):
    usr=user_registration.objects.get(id=id)
    return render(request,'MAN_View_Previoustraineeattendance.html', {'user_registration':usr})




def MAN_View_Trainerattendance(request,id):
    usr=user_registration.objects.get(id=id)
    return render(request,'MAN_View_Trainerattendance.html', {'user_registration':usr})


def MAN_ViewTrainerattendancesort(request,id):
    # usr=user_registration.objects.get(id=id)
    if request.method == "POST":
        fromdate = request.POST.get('fromdate')
        todate = request.POST.get('todate') 
        adata =attendance.objects.filter(date__range=[fromdate,todate]).filter(user_id=id)
        
    return render(request,'MAN_View_Trainerattendance.html',{'adata':adata})



def MAN_ViewCurrenttraineeattendancesort(request,id):
    usr=user_registration.objects.get(id=id)
    if request.method == "POST":
        fromdate = request.POST.get('fromdate')
        todate = request.POST.get('todate') 
        adata =attendance.objects.filter(date__range=[fromdate,todate]).filter(user_id=id)
        
    return render(request,'MAN_View_Currenttraineeattendance.html',{'adata':adata,'user_registration':usr})

def MAN_ViewPrevioustraineeattendancesort(request,id):
    usr=user_registration.objects.get(id=id)
    if request.method == "POST":
        fromdate = request.POST.get('fromdate')
        todate = request.POST.get('todate') 
        adata = attendance.objects.filter(date__range=[fromdate,todate]).filter(user_id=id)
        
    return render(request,'MAN_View_Previoustraineeattendance.html',{'adata':adata,'user_registration':usr})







def MAN_dev_attendance(request):
    return render(request,'MAN_dev_attendance.html')           
def page_1(request):
 
    dpt=department.objects.all()
    print(dpt)
    dsg=designation.objects.all()
    userreg=user_registration.objects.all()
    return render(request,'MAN_page1.html', {'department':dpt,'designation':dsg,'user_registration':userreg})  



def page_3(request):
    
    if request.method == "POST":
        empname1=request.POST.get('empname')

        atten=attendance.objects.all()
    return render(request,'MAN_page3.html',{'atten':atten,'empname1':empname1}) 
   



def desi(request):   
    dept_id = request.GET.get('dept_id')
    departments=department.objects.all()
    Desig = designation.objects.filter(department_id=dept_id)
    return render(request, 'designation.html', {'Desig': Desig,'departments':departments})



def emp(request):   
    dept_id = request.GET.get('dept_id')
    desig_id = request.GET.get('desig_id')
    dept=department.objects.filter(id=dept_id)
    desi=designation.objects.filter(id=desig_id)
    user=user_registration.objects.filter(designation_id=desig_id)
    print(dept)
    print(desi)
    return render(request, 'employee.html',{'user':user,'dept':dept,'desi':desi})



#---------------------------anwar vies end --------------------------

#----- akhil-----

def MAN_Reportedissue(request):
    designations=designation.objects.all()
    return render(request, 'MAN_Reportedissue.html',{'designation':designations})

def MAN_ReportedissueShow(request,id):
    designations=designation.objects.get(id=id)
    user=user_registration.objects.filter(designation=designations)
    reported_issues=reported_issue.objects.all()
    return render(request,'MAN_ReportedissueShow.html',{'designation':designations,'reported_issue':reported_issues,'user_registration':user})

def MAN_ReportedissueShow1(request,id):
    reported_issues=reported_issue.objects.get(id=id)
    return render(request,'MAN_ReportedissueShow1.html',{'reported_issue':reported_issues}) 


#-------------




#-------praveen-----

def MAN_trainerstable(request):
    Trainer = designation.objects.get(designation='Trainer')
    trainers_data=user_registration.objects.filter(designation=Trainer)
    topics=topic.objects.all()
    return render(request,'MAN_trainerstable.html',{'trainers_data':trainers_data,'topics':topics})
def MAN_Training(request,id):
    #team=create_team.objects.filter(user_id=id)
    #return render(request,'BRadmin_Training.html',{'team':team})
        #team=create_team.objects.all()
    user=user_registration.objects.filter(id=id)
    team=create_team.objects.all()
    return render(request,'MAN_Training.html',{'team':team,'user':user})
def MAN_trainingteam1(request,id):
    id=id
    Trainee = designation.objects.get(designation='Trainee')
    num=user_registration.objects.filter(designation=Trainee).filter(team=id).count()
    num1=topic.objects.filter(team=id).count()
    return render(request,'MAN_trainingteam1.html',{'id':id,'num':num,'num1':num1})
def MAN_traineestable(request,id):
    Trainee = designation.objects.get(designation='Trainee')
    trainees_data=user_registration.objects.filter(designation=Trainee).filter(team=id)
    return render(request,'MAN_traineestable.html',{'trainees_data':trainees_data}) 
def MAN_trainingprofile(request,id):
    trainees_data=user_registration.objects.get(id=id)
    #Trainee = designation.objects.get(designation='Trainee')
    #trainees_data=user_registration.objects.filter(designation=Trainee)
    user=user_registration.objects.get(id=id)
    num=trainer_task.objects.filter(user=user).filter(status='Completed').count()
    return render(request,'MAN_trainingprofile.html',{'trainees_data':trainees_data,'num':num})
def MAN_completedtasktable(request,id):
    user=user_registration.objects.get(id=id)
    task=trainer_task.objects.filter(user=user)
    return render(request,'MAN_completedtasktable.html',{'task_data':task})
def MAN_topictable(request,id):
    topics=topic.objects.filter(team=id)
    return render(request,'MAN_topictable.html',{'topics':topics})

#---------end praveen------




#----------- sharon ---------

# current projects
def MAN_python2(request):
    project_details = project.objects.all()
    return render(request,'MAN_projects.html',{'proj_det':project_details})

def MAN_employees3(request):
    project_details = project.objects.all()
    depart =department.objects.all()
    return render(request,'MAN_employees3.html',{'proj_det':project_details,'department':depart})


def MAN_projects(request,id):
    Num= project.objects.filter(status='accepted').filter(department=id).count()
    num= project.objects.filter(status='completed').filter(department=id).count()
    project_details = project.objects.all()
    depart =department.objects.get(id=id)
    id=id
    return render(request,'MAN_projects.html',{'proj_det':project_details,'num':Num,'Num':num,'department':depart,'id':id})
 

def MAN_proj_list(request,id):
    project_details = project.objects.filter(department=id)
    print (project_details.count())
    return render(request,'MAN_proj_list.html',{'proj_det':project_details})

def MAN_proj_det(request,id):
    project_details = project.objects.get(id=id)
    return render(request,'MAN_proj_det.html',{'proj_det':project_details})

def MAN_proj_mngrs(request,id):
    project_details = project.objects.get(id=id)
    return render(request,'MAN_proj_mngrs.html',{'proj_det':project_details})

def MAN_proj_mangrs1(request,id):
    project_details = project.objects.get(id=id) 
    return render(request,'MAN_proj_mangrs1.html',{'proj_det':project_details})

def MAN_proj_mangrs2(request,id):
    project_details = project.objects.get(id=id) 
    project_task = project_taskassign.objects.all()
    return render(request,'MAN_proj_mangrs2.html',{'proj_task':project_task,'proj_det':project_details})

def MAN_daily_report(request,id): 
    project_task = project_taskassign.objects.get(id=id)
    tester =tester_status.objects.all()
    return render(request,'MAN_daily_report.html',{'proj_task':project_task,'test':tester,})

def MAN_developers(request,id):
    project_details = project.objects.get(id=id) 
    project_task = project_taskassign.objects.filter(tl_id = id)
    return render(request,'MAN_developers.html',{'proj_task':project_task,'proj_det':project_details})

#------ sharone end
#---subeeesh start----


def MAN_projects_new(request, id):
    num = project.objects.filter(status='completed').filter(department=id).count()
    project_details = project.objects.all()
    departments = department.objects.get(id=id)
    id=id
    return render(request,'MAN_projects_show.html',{'project':project_details,'Num':num, 'department':departments,'id':id})
   


def MAN_proj_cmpltd_new(request, id):
    project_details=project.objects.filter(department=id)
    print (project_details.count())
    return render(request,'MAN_proj_cmpltd_show.html',{'project': project_details})


def MAN_cmpltd_proj_det_new(request, id):
    project_details = project.objects.get(id=id)

    return render(request,'MAN_cmpltd_proj_det_show.html',{'project': project_details})

def MAN_proj_mngrs_new(request, id):
    project_details = project.objects.get(id=id)
    return render(request,'MAN_proj_mngrs_show.html', {'project': project_details})

def MAN_proj_mangrs1_new(request,id):
    project_details = project.objects.get(id=id)
    return render(request,'MAN_proj_mangrs1_show.html', {'project': project_details})

def MAN_proj_mangrs2_new(request, id):
    project_details = project.objects.get(id=id)
    project_task = project_taskassign.objects.all()
    return render(request,'MAN_proj_mangrs2_show.html', {'project':project_details,'project_taskassign':project_task})

def MAN_developers_new(request, id):
    project_details = project.objects.get(id=id)
    project_task = project_taskassign.objects.filter(tl_id = id)
    return render(request,'MAN_developers_show.html', {'project':project_details,'project_taskassign':project_task})

def MAN_daily_report_new(request, id):
    project_task = project_taskassign.objects.get(id=id)
    tester = tester_status.objects.all()
    return render(request,'MAN_daily_report_show.html', {'project':project_task,'tester_status':tester})

#--------subeesh end-----



#--------Nimisha--------

def MAN_tasks(request):
    return render(request,'MAN_tasks.html')

def MAN_givetask(request):
    if request.method == 'POST':
        sc1 = request.POST['Department']
        sc2 = request.POST['designation']
        sc3 = request.POST['projectname']
        sc4 = request.POST['discrip']
        sc5 = request.POST['start']
        sc6 = request.POST['end']
        ogo = request.FILES['img[]']
        print(sc1,sc2)
        progress=0
        catry = project_taskassign(description=sc4,files=ogo,
                                  startdate=sc5, enddate=sc6,extension='0',designation=sc2,department=sc1)
        catry.save()
    dept = department.objects.all()
    desig = designation.objects.all()
    proj = project.objects.all()
    emp = user_registration.objects.all()
    return render(request,'MAN_givetask.html',{'desig':desig,'dept':dept,'project':proj,'emp':emp})


def desi_task(request):   
    dept_id = request.GET.get('dept_id')
    Desig = designation.objects.filter(department_id=dept_id)
    print(Desig)
    return render(request, 'MAN_taskdesignation.html', {'Desig': Desig})

def emp_task(request):   
    dept_id = request.GET.get('dept_id')
    desig_id = request.GET.get('desig_id')
    emp = user_registration.objects.filter(department_id=dept_id).filter(designation_id=desig_id)
    print(emp)
    return render(request, 'MAN_taskemployee.html', {'emp': emp})


def MAN_currenttasks(request):
	names =trainer_task.objects.filter(status='Progressing')
	return render(request,'MAN_currenttask.html',{'names': names})

def MAN_previoustasks(request):
	names =trainer_task.objects.filter(status='Completed')
	return render(request,'MAN_previoustasks.html',{'names': names})


#--------nimisha end----------


#--------safdhar -----------

def MAN_upcoming(request):
    return render(request,'MAN_upcomingprojects.html')

def MAN_viewprojectform(request):
    if request.method == 'POST':
        sc1 = request.POST['Department']
        sc2 = request.POST['designation']
        sc3 = request.POST['projectname']
        sc4 = request.POST['discrip']
        sc5 = request.POST['start']
        sc6 = request.POST['end']
        
        print(sc1,sc2)
        progress=0
        catry = project_taskassign(project_id=sc3,
                                  description=sc4,
                                  startdate=sc5, enddate=sc6,extension='0',designation=sc2,department=sc1)
        catry.save()
    dept = department.objects.all()
    desig = designation.objects.all()
    proj = project.objects.all()
    return render(request,'MAN_viewprojects.html',{'desig':desig,'dept':dept,'project':proj})
def MAN_acceptedprojects(request):
    pro = project.objects.filter(status='Accepted')
    return render(request,'MAN_acceptedprojects.html',{'projects':pro})

def MAN_rejected(request):
    pro = project.objects.filter(status='Rejected')
    return render(request,'MAN_rejectedprojectes.html',{'projects':pro})

def MAN_createproject(request):
    if request.method == 'POST':
        sc1 = request.POST['Department']
        sc2 = request.POST['designation']
        sc3 = request.POST['projectname']
        sc4 = request.POST['discrip']
        sc5 = request.POST['start']
        sc6 = request.POST['end']
        ogo = request.FILES['img[]']
        print(sc5,sc6,ogo,sc1)
        progress=0
        catry = project(designation_id=sc2,department_id=sc1,project=sc3,
                                  description=sc4,
                                  startdate=sc5, enddate=sc6, files=ogo,progress=progress)
        catry.save()
    dept = department.objects.all()
    desig = designation.objects.all() 
 
    return render(request,'MAN_createproject.html',{'desig':desig,'dept':dept})

def MAN_upcomingprojectsview(request):
    pro =project.objects.all()
    return render(request,'MAN_upcomingprojectsview.html',{'projects': pro})

def MAN_seradmintraineedesi1(request):
    dept_id = request.GET.get('dept_id')
    Desig = designation.objects.filter(department_id=dept_id)
    print('safdhar')
    return render(request, 'MAN_createprojectdropdown.html', {'Desig': Desig})

def MAN_seradmindesig(request):
    print("safdhar")
    dept_id = request.GET.get('dept_id')
    Desig = designation.objects.filter(department_id=dept_id)
    print(Desig)
    return render(request, 'MAN_giveprojectdropdown.html', {'Desig': Desig})



#----------end----------