from . import views
from django.urls import re_path


urlpatterns=[ 
    re_path(r'^$',views.index,name='index'),
    re_path(r'^newdept$',views.newdept,name='newdept'),
    re_path(r'^add_dept$',views.add_dept,name='add_dept'),
    re_path(r'^add_deptsave$',views.add_deptsave,name='add_deptsave'),
    re_path(r'^delete/(?P<id>\d+)$', views.delete,name='delete'),
    re_path(r'^delete/(?P<id>\d+)/',views.delete, name='delete'),

    #safdhar

    re_path(r'^upcoming$', views.upcoming, name='upcoming'),
    re_path(r'^viewprojectform$', views.viewprojectform, name='viewprojectform'),
    re_path(r'^acceptedprojects$', views.acceptedprojects, name='acceptedprojects'),
    re_path(r'^rejected$', views.rejected, name='rejected'),
    re_path(r'^createproject$', views.createproject, name='createproject'),
    re_path(r'^upcomingpro$', views.upcomingpro, name='upcomingpro'),


   #nimisha
    re_path(r'^BRadmin_tasks$', views.BRadmin_tasks, name='BRadmin_tasks'),
    re_path(r'^BRadmin_givetask$', views.BRadmin_givetask, name='BRadmin_givetask'),
    re_path(r'^BRadmin_currenttasks$', views.BRadmin_currenttasks, name='BRadmin_currenttasks'),
    re_path(r'^BRadmin_previoustasks$', views.BRadmin_previoustasks, name='BRadmin_previoustasks'),

    #christin
    
#******************** new Internship************************************#
    re_path( r'^admin_intern_newreg', views.admin_intern_newreg, name='admin_intern_newreg'),
    re_path( r'^admin_intern_showreg', views.admin_intern_showreg, name='admin_intern_showreg'),
    re_path( r'^admin_intern_showdetails', views.admin_intern_showdetails, name='admin_intern_showdetails'),
    re_path( r'^admin_intern_detailupdate', views.admin_intern_detailupdate, name='admin_intern_detailupdate'),
    re_path( r'^admin_intern_delete', views.admin_intern_delete, name='admin_intern_delete'),
    re_path( r'^admin_intern_bydate', views.admin_intern_bydate, name='admin_intern_bydate'),
    re_path( r'^admin_intern_showbydate', views.admin_intern_showbydate, name='admin_intern_showbydate'),

    #******************leaveform***************************************#

    re_path( r'^admin_leaveform', views.admin_leaveform, name='admin_leaveform'),
    re_path( r'^admin_leave_delete', views.admin_leave_delete, name='admin_leave_delete'),
    re_path( r'^pdf', views.render_pdf_view, name='render_pdf_view'),

    #***************bibin leave*******************
    re_path(r'^leave$', views.leave, name='leave'),
    re_path(r'^admin_leave_form$', views.admin_leave_form, name='admin_leave_form'),

#************************Amal internship***********************

    re_path(r'^internshipregister$', views.internshipregister, name='internshipregister'),
    re_path(r'^internshipregister1$', views.internshipregister1, name='internshipregister1'),

#*******************************qrcode******************


    re_path(r'^admin_code$', views.admin_code, name='admin_code'),
    re_path(r'^qrcodenew$', views.qrcodenew, name='qrcodenew'),
    re_path(r'^BRadmin_registration$', views.BRadmin_registration, name='BRadmin_registration'),
    # re_path(r'^BRadmin_regupdatedetails', views.BRadmin_regupdatedetails, name='BRadmin_regupdatedetails'),
    re_path(r'^BRadmin_registration_update/(?P<id>\d+)$', views.BRadmin_registration_update, name='BRadmin_registration_update'),



 # akhil p t

   
    re_path(r'^BRadmin_Reportedissue$', views.BRadmin_Reportedissue, name='BRadmin_Reportedissue'),
    re_path(r'^BRadmin_ReportedissueShow/(?P<id>\d+)$', views.BRadmin_ReportedissueShow, name='BRadmin_ReportedissueShow'),
    re_path(r'^BRadmin_ReportedissueShow1/(?P<id>\d+)$', views.BRadmin_ReportedissueShow1, name='BRadmin_ReportedissueShow1'),


#subeesh
   
    re_path(r'^BRadmin_profiledash_new$', views.BRadmin_profiledash_new,name='BRadmin_profiledash_new'),
    re_path(r'^BRadmin_projects_new$', views.BRadmin_projects_new, name='BRadmin_projects_new'),
    re_path(r'^BRadmin_proj_cmpltd_new$', views.BRadmin_proj_cmpltd_new, name='BRadmin_proj_cmpltd_new'),
    # re_path(r'^BRadmin_proj_det$', views.BRadmin_proj_det, name='BRadmin_proj_det'),
    re_path(r'^BRadmin_cmpltd_proj_det_new/(?P<id>\d+)/$', views.BRadmin_cmpltd_proj_det_new, name='BRadmin_cmpltd_proj_det_new'),
    re_path(r'^BRadmin_proj_mngrs_new/(?P<id>\d+)/$', views.BRadmin_proj_mngrs_new, name='BRadmin_proj_mngrs_new'),
    re_path(r'^BRadmin_proj_mangrs1_new/(?P<id>\d+)/$', views.BRadmin_proj_mangrs1_new, name='BRadmin_proj_mangrs1_new'),
    re_path(r'^BRadmin_proj_mangrs2_new/(?P<id>\d+)/$', views.BRadmin_proj_mangrs2_new, name='BRadmin_proj_mangrs2_new'),
    re_path(r'^BRadmin_developers_new/(?P<id>\d+)/$', views.BRadmin_developers_new, name='BRadmin_developers_new'),
    re_path(r'^BRadmin_daily_report_new/(?P<id>\d+)/$', views.BRadmin_daily_report_new, name='BRadmin_daily_report_new'),

 #sharon
 # 
 # 
    re_path(r'^$', views.BRadmin_profiledash,name='BRadmin_profiledash'),
    re_path(r'^BRadmin_employees$', views.BRadmin_employees, name='BRadmin_employees'),
    re_path(r'^BRadmin_python$', views.BRadmin_python, name='BRadmin_python'),
    # re_path(r'^BRadmin_index$', views.BRadmin_index, name='BRadmin_index'),
    re_path(r'^BRadmin_projects/(?P<id>\d+)/$', views.BRadmin_projects, name='BRadmin_projects'),
    re_path(r'^BRadmin_proj_list/(?P<id>\d+)/$', views.BRadmin_proj_list, name='BRadmin_proj_list'),
    re_path(r'^BRadmin_proj_det/(?P<id>\d+)/$', views.BRadmin_proj_det, name='BRadmin_proj_det'),
    re_path(r'^BRadmin_proj_mngrs/(?P<id>\d+)/$', views.BRadmin_proj_mngrs, name='BRadmin_proj_mngrs'),
    re_path(r'^BRadmin_proj_mangrs1/(?P<id>\d+)/$', views.BRadmin_proj_mangrs1, name='BRadmin_proj_mangrs1'),
    re_path(r'^BRadmin_proj_mangrs2/(?P<id>\d+)/$', views.BRadmin_proj_mangrs2, name='BRadmin_proj_mangrs2'),  
    # re_path(r'^BRadmin_proj_cmpltd$', views.BRadmin_proj_cmpltd, name='BRadmin_proj_cmpltd'),
    # re_path(r'^BRadmin_cmpltd_proj_det$', views.BRadmin_cmpltd_proj_det, name='BRadmin_cmpltd_proj_det'),
    re_path(r'^BRadmin_daily_report/(?P<id>\d+)/$', views.BRadmin_daily_report, name='BRadmin_daily_report'),
    re_path(r'^BRadmin_developers/(?P<id>\d+)/$', views.BRadmin_developers, name='BRadmin_developers'),
   
]