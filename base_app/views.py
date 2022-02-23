from qrcode import *
import qrcode.image.svg
import qrcode
from xhtml2pdf import pisa
from django.core.files import File
from pyqrcode import QRCode
from django.http import HttpResponse
from django.template.loader import get_template
from datetime import *
from django.shortcuts import redirect, render
from django.http import HttpResponse
from base_app.models import *
from core import settings
import json


# Create your views here.

def index(request):
    # Num= project.objects.count()
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
    return redirect('/base_app/newdept')



#safdhar
def upcoming(request):
    return render(request,'BRadmin_upcomingprojects.html')

def viewprojectform(request):
	if request.method == 'POST':
		sc1 = request.POST['Department']
		sc2 = request.POST['designation']
		sc3 = request.POST['projectname']
		sc4 = request.POST['discrip']
		sc5 = request.POST['start']
		sc6 = request.POST['end']
		ogo = request.FILES['img[]']
		print(sc3,sc6,ogo,sc1)
		progress=0
		catry = project_taskassign(project_id=sc3,
                                  description=sc4,
                                  startdate=sc5, enddate=sc6, files=ogo,extension='0',designation=sc2,department=sc1)
		catry.save()
	dept = department.objects.all()
	desig = designation.objects.all()
	proj = project.objects.all()
	return render(request,'BRadmin_viewprojects.html',{'desig':desig,'dept':dept,'project':proj})
def acceptedprojects(request):
	pro =project.objects.filter(status='Accepted')
	return render(request,'BRadmin_acceptedprojects.html',{'projects': pro})

def rejected(request):
	pro =project.objects.filter(status='Rejected')
	return render(request,'BRadmin_rejectedprojectes.html',{'projects': pro})

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
	return render(request,'BRadmin_createproject.html',{'dept':dept,'desig':desig})
   


def upcomingpro(request):
	pro =project.objects.all()
	return render(request,'BRadmin_upcomingpro.html',{'projects': pro})



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
		print(sc3,sc6,ogo,sc1)
		progress=0
		catry = project_taskassign(project_id =sc3,
                                  description=sc4,
                                  startdate=sc5, enddate=sc6, files=ogo,extension='0',designation=sc2,department=sc1)
		catry.save()
	dept = department.objects.all()
	desig = designation.objects.all()
	proj = project.objects.all()
	emp = user_registration.objects.all()
	return render(request,'BRadmin_givetask.html',{'desig':desig,'dept':dept,'project':proj,'emp':emp})

def BRadmin_currenttasks(request):
	names =trainer_task.objects.filter(status='Progressing')
	return render(request,'BRadmin_currenttasks.html',{'names': names})

def BRadmin_previoustasks(request):
	names =trainer_task.objects.filter(status='Completed')
	return render(request,'BRadmin_previoustasks.html',{'names': names})


#christin

def admin_intern_newreg(request):
    return render(request, 'admin_intern_newreg.html')

def admin_intern_showreg(request):
    newdata = internship.objects.order_by('-id')
    return render(request, 'admin_intern_showreg.html', {'newdata': newdata})


def admin_intern_showdetails(request):
    id=request.GET.get('id')
    empid=internship.objects.filter(id=id)
    return render(request, 'admin_intern_showdetails.html', {'mem':empid})

def admin_intern_detailupdate(request):
    id=request.GET.get('id')

    if request.method == "POST":
        mem = internship.objects.get(id=id)
        mem.reg_date = request.POST.get("regdate")
        mem.fullname = request.POST.get("fullname")
        mem.collegename = request.POST.get("college")
        mem.reg_no = request.POST.get("regno")
        mem.course = request.POST.get("course")
        mem.stream = request.POST.get("stream")
        mem.platform = request.POST.get("platform")
        mem.start_date = request.POST.get("startdate")
        mem.end_date = request.POST.get("enddate")
        mem.mobile = request.POST.get("mobile")
        mem.alternative_no = request.POST.get("altmob")
        mem.email = request.POST.get("email")
        # mem.profile_pic = request.POST.get("propic")
        # mem.attach_file = request.POST.get("attach")
        mem.rating = request.POST.get("rating")
        mem.hrmanager = request.POST.get("hrmanager")
        mem.guide = request.POST.get("guide")
        mem.save()
        return redirect('admin_intern_showreg')
    else:
        newdata = internship.objects.get(id = id)
        return render(request, 'admin_intern_showreg.html', {'mem': newdata})

def admin_intern_delete(request):
    id=request.GET.get('id')
    mem = internship.objects.get(id=id)
    mem.delete()
    newdata = internship.objects.order_by('-id')
    return render(request, 'admin_intern_showreg.html', {'newdata': newdata})

def admin_intern_bydate(request):
    newdata = internship.objects.all().values('reg_date').distinct()
    return render(request, 'admin_intern_bydate.html', {'newdata': newdata})

def admin_intern_showbydate(request):
    reg_date=request.GET.get('reg_date')
    empid=internship.objects.filter(reg_date=reg_date)
    return render(request, 'admin_intern_showreg.html', {'newdata':empid})



def render_pdf_view(request):
    id=request.GET.get('id')
    date = datetime.now()   
    mem = internship.objects.get(id=id)
    template_path = 'pdf.html'
    context = {'mem': mem,
    'media_url':settings.MEDIA_URL,
    'date':date
    }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    #response['Content-Disposition'] = 'attachment; filename="certificate.pdf"'
    response['Content-Disposition'] = 'filename="certificate.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    


    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response




    #*************************bibin leave**********************

def leave(request):
    return render(request, 'admin_leaveform.html')

def admin_leave_form(request):
    a = leave()
    if request.method == "POST":
        a.name = request.POST.get('name')
        a.branch = request.POST.get('branch')
        a.Designation = request.POST.get('designation')
        a.leavefrom = request.POST.get('from')
        a.leaveto = request.POST.get('to')
        a.halforfull = request.POST.get('haful')
        a.reason = request.POST.get('reason')
        a.save()
        return redirect('leave')
    else:
        return render(request, 'admin_leaveform.html')  

def admin_leaveform(request):
    leaves = leave.objects.all()
    return render(request, 'admin_leaveform.html', {'leaves':leaves})

def admin_leave_delete(request):
    id = request.GET.get('id')
    mem = leave.objects.get(id=id)
    mem.delete()
    return redirect(admin_leaveform)



#*****************************Amal internship*************


def internshipregister1(request):
    return render(request,'internshipregister.html')

def internshipregister(request):
    a=internship()
    
    if request.method=="POST":
        a.fullname = request.POST.get('name')
        a.collegename = request.POST.get('college_name')
        a.reg_no = request.POST.get('reg_no')
        a.course = request.POST.get('course')
        a.stream = request.POST.get('stream')
        a.platform = request.POST.get('platform')
        a.start_date = request.POST.get('start_date')
        a.end_date = request.POST.get('end_date')
        a.mobile = request.POST.get('mobile')
        a.alternative_no = request.POST.get('alternative_no')
        a.email = request.POST.get('email')
        a.profile_pic = request.FILES['profile_pic']
        a.attach_file = request.FILES['attach_file']
        a.reg_date=datetime.now()
        if (a.end_date<a.start_date):
            
            return render(request,'internshipregister.html',{'a':a})
               
            
        else:

            a.save()
            qr = make("https://managezone.in/app/admin_code?id=" + str(a.id))
            qr.save(settings.MEDIA_ROOT + "\\" +str(a.id) + ".png")
            with open(settings.MEDIA_ROOT + "\\" + str(a.id) + ".png", "rb") as reopen:
                    djangofile = File(reopen)
                    a.qr = djangofile
                    #college1.image = request.FILES['image']
                    #college1.idproof = request.FILES['idproof']
                    a.save()
            return render(request,'internshipregister.html',{'a':a})
        
        

    else:
        return render(request,'internshipregister.html')




#*****************************qrcode**********************
def qr(request):
    context = {}
    if request.method == "POST":
        factory = qrcode.image.svg.SvgImage
        img = qrcode.make(request.POST.get("name"), image_factory=factory, box_size=10)
        #img = regdetails.objects.get(id=request.POST.get('name'))
        stream = BytesIO()
        img.save(stream)
        context["svg"] = stream.getvalue().decode()
    return render(request,'qr.html',context)



def admin_code(request):
    id=request.GET.get('id')

    empid=internship.objects.filter(id=id)
    context = {
        'mem':empid,
        'media_url':settings.MEDIA_URL
        }
    return render(request, 'admin_code.html', context)

def qrcodenew(request):
    img = make(settings.LOCALROOT + name)
    img.save(settings.MEDIA_ROOT + "\\" + name + ".png")
    return redirect('admin_code')


#-----------REGISTRATION

def BRadmin_registration(request):
    return render(request,'BRadmin_registration.html')

def BRadmin_registration_update(request,id):
    if request.method == "POST":
        a = user_registration.objects.get(id=id)
        b = qualification.objects.get(user=id)
        c = extracurricular.objects.get(user=id)
        a.fullname = request.POST['fname']
        a.fathername = request.POST['fathername']
        a.mothername = request.POST['mothername']
        a.dateofbirth = request.POST['dob']
        a.gender = request.POST['gender']
        a.presentaddress1 = request.POST['address1']
        a.presentaddress2  =  request.POST['address2']
        a.presentaddress3 =  request.POST['address3']
        a.pincode = request.POST['pincode']
        a.district  =  request.POST['district']
        a.state  =  request.POST['state']
        a.country  =  request.POST['country']
        a.permanentaddress1 = request.POST['paddress1']
        a.permanentaddress2  =  request.POST['paddress2']
        a.permanentaddress3  =  request.POST['paddress3']
        a.permanentpincode = request.POST['ppincode']
        a.permanentdistrict  =  request.POST['pdistrict']
        a.permanentstate  =  request.POST['pstate']
        a.permanentcountry =  request.POST['pcountry']
        a.mobile = request.POST['mobile']
        a.alternativeno = request.POST['alternative']
        a.email = request.POST['email']
        a.password= request.POST['password']
        a.branch_id = request.POST['branch']
        #a.photo = request.FILES['photo']
        #a.idproof = request.FILES['idproof']
        a.save()

        
        b.plustwo = request.POST.get('plustwo')
        b.school = request.POST['school']
        b.schoolaggregate = request.POST['aggregate']
        #b.schoolcertificate = request.FILES['cupload']
        b.ugdegree = request.POST['degree']
        b.ugstream = request.POST['stream']
        b.ugpassoutyr = request.POST['passoutyear']
        b.ugaggregrate = request.POST['aggregate1']
        b.backlogs = request.POST['supply']
        #b.ugcertificate = request.FILES['cupload1']
        b.pg = request.POST['pg']
        b.save()

        
        c.internshipdetails = request.POST['details']
        c.internshipduration = request.POST['duration']
        c.internshipcertificate = request.POST['certificate']
        c.onlinetrainingdetails = request.POST['details1']
        c.onlinetrainingduration = request.POST['duration1']
        c.onlinetrainingcertificate= request.POST['certificate1']
        c.projecttitle = request.POST['title']
        c.projectduration = request.POST['duration2']
        c.projectdescription = request.POST['description']
        c.projecturl = request.POST['url']
        c.skill1 = request.POST['skill1']
        c.skill2 = request.POST['skill2']
        c.skill3 = request.POST['skill3']
        c.save()
        # return redirect('BRadmin_registration')
        return render(request,'BRadmin_registration_update.html')


# def BRadmin_regupdatedetails(request,id):
   
#         return redirect('BRadmin_registration')    



#akhil p t

def BRadmin_profiledash(request):
    return render(request,'BRadmin_profiledash.html')

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



#Subeesh

def BRadmin_profiledash_new(request):
     Num = project.objects.count()
     project_details = project.objects.all()
    
     return render(request,'BRadmin_profile_dash.html',{'project':project_details,'num':Num})



def BRadmin_projects_new(request):
    Num = project.objects.count()
    project_details = project.objects.all()
    for i in project_details:
        if i.progress == "in progress":  
            Num = Num-1
            break
    return render(request,'BRadmin_projects_show.html',{'project':project_details,'num':Num})
   


def BRadmin_proj_cmpltd_new(request):
    project_details=project.objects.all()
    return render(request,'BRadmin_proj_cmpltd_show.html',{'project': project_details})

# def BRadmin_proj_det(request):
#     return render(request,'BRadmin_proj_det.html')

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

#sharon
# 
# 
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
    return render(request,'BRadmin_profiledash.html',{'proj_det':project_details,'num':Num})

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

    