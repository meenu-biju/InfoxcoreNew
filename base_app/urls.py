from . import views
from django.urls import re_path


urlpatterns=[ 
    re_path(r'^$',views.login,name='login'),
    re_path(r'^logout$',views.logout,name='logout'),
    re_path(r'^index$',views.index,name='index'),
    re_path(r'^newdept$',views.newdept,name='newdept'),
    re_path(r'^add_dept$',views.add_dept,name='add_dept'),
    re_path(r'^add_deptsave$',views.add_deptsave,name='add_deptsave'),
    re_path(r'^delete/(?P<id>\d+)$', views.delete,name='delete'),

   #safdhar
    re_path(r'^upcoming$', views.upcoming, name='upcoming'),
    re_path(r'^viewprojectform$', views.viewprojectform, name='viewprojectform'),
    re_path(r'^acceptedprojects$', views.acceptedprojects, name='acceptedprojects'),
    re_path(r'^rejected$', views.rejected, name='rejected'),
    re_path(r'^createproject$', views.createproject, name='createproject'),
    re_path(r'^upcomingpro$', views.upcomingpro, name='upcomingpro'),
    re_path(r'^seradmintraineedesi1$', views.seradmintraineedesi1, name='seradmintraineedesi1'),
    re_path(r'^seradmindesig$', views.seradmindesig, name='seradmindesig'),
    

    

   #nimisha
    re_path(r'^BRadmin_tasks$', views.BRadmin_tasks, name='BRadmin_tasks'),
    re_path(r'BRadmin_givetask$', views.BRadmin_givetask, name='BRadmin_givetask'),
    re_path(r'^BRadmin_currenttasks$', views.BRadmin_currenttasks, name='BRadmin_currenttasks'),
    re_path(r'^BRadmin_previoustasks$', views.BRadmin_previoustasks, name='BRadmin_previoustasks'),
    re_path(r'emp$', views.emp, name='emp'),
    re_path(r'desi$', views.desi, name='desi'),

 # akhil p t

   
    re_path(r'^BRadmin_Reportedissue$', views.BRadmin_Reportedissue, name='BRadmin_Reportedissue'),
    re_path(r'^BRadmin_ReportedissueShow/(?P<id>\d+)$', views.BRadmin_ReportedissueShow, name='BRadmin_ReportedissueShow'),
    re_path(r'^BRadmin_ReportedissueShow1/(?P<id>\d+)$', views.BRadmin_ReportedissueShow1, name='BRadmin_ReportedissueShow1'),



 #sharon


    re_path(r'^BRadmin_profiledash$', views.BRadmin_profiledash,name='BRadmin_profiledash'),
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


    #subeesh
    # re_path(r'^BRadmin_profiledash_new$', views.BRadmin_profiledash_new,name='BRadmin_profiledash_new'),
    re_path(r'^BRadmin_employees_new$', views.BRadmin_employees_new, name='BRadmin_employees_new'),
    re_path(r'^BRadmin_python_new$', views.BRadmin_python_new, name='BRadmin_python_new'),
    re_path(r'^BRadmin_projects_new/(?P<id>\d+)$', views.BRadmin_projects_new, name='BRadmin_projects_new'),
    re_path(r'^BRadmin_proj_cmpltd_new/(?P<id>\d+)$', views.BRadmin_proj_cmpltd_new, name='BRadmin_proj_cmpltd_new'),
    # re_path(r'^BRadmin_proj_det$', views.BRadmin_proj_det, name='BRadmin_proj_det'),
    re_path(r'^BRadmin_cmpltd_proj_det_new/(?P<id>\d+)/$', views.BRadmin_cmpltd_proj_det_new, name='BRadmin_cmpltd_proj_det_new'),
    re_path(r'^BRadmin_proj_mngrs_new/(?P<id>\d+)/$', views.BRadmin_proj_mngrs_new, name='BRadmin_proj_mngrs_new'),
    re_path(r'^BRadmin_proj_mangrs1_new/(?P<id>\d+)/$', views.BRadmin_proj_mangrs1_new, name='BRadmin_proj_mangrs1_new'),
    re_path(r'^BRadmin_proj_mangrs2_new/(?P<id>\d+)/$', views.BRadmin_proj_mangrs2_new, name='BRadmin_proj_mangrs2_new'),
    re_path(r'^BRadmin_developers_new/(?P<id>\d+)/$', views.BRadmin_developers_new, name='BRadmin_developers_new'),
    re_path(r'^BRadmin_daily_report_new/(?P<id>\d+)/$', views.BRadmin_daily_report_new, name='BRadmin_daily_report_new'),

 
#    #anandhu
    re_path(r'^BRadmin_department_new$', views.BRadmin_department_new, name='BRadmin_department_new'),
    re_path(r'^BRadmin_python$', views.BRadmin_python, name='BRadmin_python'),
    re_path(r'^BRadmin_projectman$', views.BRadmin_projectman, name='BRadmin_projectman'),
    re_path(r'^BRadmin_proname/(?P<id>\d+)$', views.BRadmin_proname, name='BRadmin_proname'),
    re_path(r'^BRadmin_proinvolve/(?P<id>\d+)$', views.BRadmin_proinvolve, name='BRadmin_proinvolve'),
    re_path(r'^BRadmin_promanatten/(?P<id>\d+)/$', views.BRadmin_promanatten, name='BRadmin_promanatten'),
    re_path(r'^BRadmin_promanattensort/(?P<id>\d+)/$', views.BRadmin_promanattensort, name='BRadmin_promanattensort'),


    re_path(r'^BRadmin_HRattendance/(?P<id>\d+)/$', views.BRadmin_HRattendance, name='BRadmin_HRattendance'),
    re_path(r'^BRadmin_HRattendancesort/(?P<id>\d+)/$', views.BRadmin_HRattendancesort, name='BRadmin_HRattendancesort'),
    re_path(r'^BRadmin_HRlist$', views.BRadmin_HRlist, name='BRadmin_HRlist'),
    re_path(r'^BRadmin_HRprofile/(?P<id>\d+)$', views.BRadmin_HRprofile, name='BRadmin_HRprofile'),
    
    re_path(r'^BRadmin_TLattendance/(?P<id>\d+)/$', views.BRadmin_TLattendance, name='BRadmin_TLattendance'),
    re_path(r'^BRadmin_TLattendancesort/(?P<id>\d+)/$', views.BRadmin_TLattendancesort, name='BRadmin_TLattendancesort'),
    re_path(r'^BRadmin_TLip/(?P<id>\d+)$', views.BRadmin_TLip, name='BRadmin_TLip'),
    re_path(r'^BRadmin_TLlist$', views.BRadmin_TLlist, name='BRadmin_TLlist'),
    re_path(r'^BRadmin_TLprofile/(?P<id>\d+)$', views.BRadmin_TLprofile, name='BRadmin_TLprofile'),


    re_path(r'^BRadmin_dev_details$',views.BRadmin_dev_details,name='BRadmin_dev_details'),
    re_path(r'^BRadmin_dev_profile/(?P<id>\d+)$',views.BRadmin_dev_profile,name='BRadmin_dev_profile'),
    re_path(r'^BRadmin_dev_involved/(?P<id>\d+)$',views.BRadmin_dev_involved,name='BRadmin_dev_involved'),
    re_path(r'^BRadmin_dev_attendance/(?P<id>\d+)/$',views.BRadmin_dev_attendance,name='BRadmin_dev_attendance'),
    re_path(r'^BRadmin_dev_attendancesort/(?P<id>\d+)/$', views.BRadmin_dev_attendancesort, name='BRadmin_dev_attendancesort'),
    re_path(r'^BRadmin_page1$',views.page1,name='page1'),
    re_path(r'^BRadmin_page2$',views.page2,name='page2'),

    #praveen

    re_path(r'^BRadmin_trainerstable$', views.BRadmin_trainerstable,name='BRadmin_trainerstable'),
    re_path(r'^BRadmin_Training/(?P<id>\d+)$', views.BRadmin_Training,name='BRadmin_Training'),
    re_path(r'^BRadmin_trainingteam1/(?P<id>\d+)$', views.BRadmin_trainingteam1,name='BRadmin_trainingteam1'),
    re_path(r'^BRadmin_traineestable/(?P<id>\d+)$', views.BRadmin_traineestable,name='BRadmin_traineestable'),
    re_path(r'^BRadmin_trainingprofile/(?P<id>\d+)$', views.BRadmin_trainingprofile,name='BRadmin_trainingprofile'),
    re_path(r'^BRadmin_completedtasktable/(?P<id>\d+)$', views.BRadmin_completedtasktable,name='BRadmin_completedtasktable'),
    re_path(r'^BRadmin_topictable/(?P<id>\d+)$', views.BRadmin_topictable,name='BRadmin_topictable'),

    #anwar
    re_path(r'^BRadmin_View_Trainers$', views.BRadmin_View_Trainers, name='BRadmin_View_Trainers'),
    re_path(r'^BRadmin_View_Trainerprofile/(?P<id>\d+)$', views.BRadmin_View_Trainerprofile, name='BRadmin_View_Trainerprofile'),
    re_path(r'^BRadmin_View_Currenttraineesoftrainer/(?P<id>\d+)/$', views.BRadmin_View_Currenttraineesoftrainer, name='BRadmin_View_Currenttraineesoftrainer'),
    re_path(r'^BRadmin_View_Previoustraineesoftrainer/(?P<id>\d+)/$', views.BRadmin_View_Previoustraineesoftrainer, name='BRadmin_View_Previoustraineesoftrainer'),
    re_path(r'^BRadmin_View_Currenttraineeprofile/(?P<id>\d+)$', views.BRadmin_View_Currenttraineeprofile, name='BRadmin_View_Currenttraineeprofile'),
    re_path(r'^BRadmin_View_Currenttraineetasks/(?P<id>\d+)$', views.BRadmin_View_Currenttraineetasks, name='BRadmin_View_Currenttraineetasks'),
    re_path(r'^BRadmin_View_Currenttraineeattendance/(?P<id>\d+)$', views.BRadmin_View_Currenttraineeattendance, name='BRadmin_View_Currenttraineeattendance'),
    re_path(r'^BRadmin_View_Previoustraineesoftrainer$', views.BRadmin_View_Previoustraineesoftrainer, name='BRadmin_View_Previoustraineesoftrainer'),
    re_path(r'^BRadmin_View_Previoustraineeprofile/(?P<id>\d+)$', views.BRadmin_View_Previoustraineeprofile, name='BRadmin_View_Previoustraineeprofile'),
    re_path(r'^BRadmin_View_Previoustraineetasks/(?P<id>\d+)$', views.BRadmin_View_Previoustraineetasks, name='BRadmin_View_Previoustraineetasks'),
    re_path(r'^BRadmin_View_Previoustraineeattendance/(?P<id>\d+)$', views.BRadmin_View_Previoustraineeattendance, name='BRadmin_View_Previoustraineeattendance'),
    re_path(r'^BRadmin_View_Trainerattendance/(?P<id>\d+)$', views.BRadmin_View_Trainerattendance, name='BRadmin_View_Trainerattendance'),
    re_path(r'^BRadmin_ViewTrainerattendancesort/(?P<id>\d+)/$', views.BRadmin_ViewTrainerattendancesort, name='BRadmin_ViewTrainerattendancesort'),
    re_path(r'^BRadmin_ViewCurrenttraineeattendancesort/(?P<id>\d+)/$', views.BRadmin_ViewCurrenttraineeattendancesort, name='BRadmin_ViewCurrenttraineeattendancesort'),
    re_path(r'^BRadmin_ViewPrevioustraineeattendancesort/(?P<id>\d+)/$', views.BRadmin_ViewPrevioustraineeattendancesort, name='BRadmin_ViewPrevioustraineeattendancesort'),
    re_path(r'^BRadmin_dev_attendance$',views.BRadmin_dev_attendance,name='BRadmin_dev_attendance'),
    re_path(r'^BRadmin_page1$',views.page1,name='page1'),
    re_path(r'^BRadmin_page3$',views.page3,name='page3'),
    re_path(r'^desi$',views.desi,name='desi'),
    re_path(r'^emp$',views.emp,name='emp'),


    #---------------END-------------

    # re_path(r'^$', views.man_login,name='man_login'),
    # re_path(r'^man_login$', views.man_login,name='man_login'),
    # re_path(r'^man_logout$', views.man_logout,name='man_logout'),


    # re_path(r'^MAN_home$', views.MAN_home,name='MAN_home'),
    re_path(r'^MAN_profiledash$', views.MAN_profiledash,name='MAN_profiledash'),
    re_path(r'^MAN_index$', views.MAN_index, name='MAN_index'),
    re_path(r'^MAN_employees$', views.MAN_employees, name='MAN_employees'),
    re_path(r'^MAN_python$', views.MAN_python, name='MAN_python'),
    re_path(r'^MAN_projectman$', views.MAN_projectman, name='MAN_projectman'),
    re_path(r'^MAN_proname/(?P<id>\d+)$', views.MAN_proname, name='MAN_proname'),
    re_path(r'^MAN_proinvolve/(?P<id>\d+)$', views.MAN_proinvolve, name='MAN_proinvolve'),
    re_path(r'^MAN_promanatten/(?P<id>\d+)/$', views.MAN_promanatten, name='MAN_promanatten'),
    re_path(r'^MAN_promanattensort/(?P<id>\d+)/$', views.MAN_promanattensort, name='MAN_promanattensort'),


    re_path(r'^MAN_HRattendance/(?P<id>\d+)/$', views.MAN_HRattendance, name='MAN_HRattendance'),
    re_path(r'^MAN_HRattendancesort/(?P<id>\d+)/$', views.MAN_HRattendancesort, name='MAN_HRattendancesort'),
    re_path(r'^MAN_HRlist$', views.MAN_HRlist, name='MAN_HRlist'),
    re_path(r'^MAN_HRprofile/(?P<id>\d+)$', views.MAN_HRprofile, name='MAN_HRprofile'),
    
    re_path(r'^MAN_TLattendance/(?P<id>\d+)/$', views.MAN_TLattendance, name='MAN_TLattendance'),
    re_path(r'^MAN_TLattendancesort/(?P<id>\d+)/$', views.MAN_TLattendancesort, name='MAN_TLattendancesort'),
    re_path(r'^MAN_TLip/(?P<id>\d+)$', views.MAN_TLip, name='MAN_TLip'),
    re_path(r'^MAN_TLlist$', views.MAN_TLlist, name='MAN_TLlist'),
    re_path(r'^MAN_TLprofile/(?P<id>\d+)$', views.MAN_TLprofile, name='MAN_TLprofile'),


    re_path(r'^MAN_dev_details$',views.MAN_dev_details,name='MAN_dev_details'),
    re_path(r'^MAN_dev_profile/(?P<id>\d+)$',views.MAN_dev_profile,name='MAN_dev_profile'),
    re_path(r'^MAN_dev_involved/(?P<id>\d+)$',views.MAN_dev_involved,name='MAN_dev_involved'),
    re_path(r'^MAN_dev_attendance/(?P<id>\d+)/$',views.MAN_dev_attendance,name='MAN_dev_attendance'),
    re_path(r'^MAN_dev_attendancesort/(?P<id>\d+)/$', views.MAN_dev_attendancesort, name='MAN_dev_attendancesort'),
    re_path(r'^MAN_page1$',views.page1,name='page1'),
    re_path(r'^MAN_page2$',views.page2,name='page2'),


#---------------------------  ^ anandhu ----   

#-----------------------MEENU--------------------
    re_path(r'^man_newdept$',views.man_newdept,name='man_newdept'),
    re_path(r'^man_dept$',views.man_dept,name='man_dept'),
    re_path(r'^man_add_deptsave$',views.man_add_deptsave,name='man_add_deptsave'),
    re_path(r'^man_delete/(?P<id>\d+)$', views.man_delete,name='man_delete'),
# -------------------------- anwar-------------------


    re_path(r'^MAN_View_Trainers$', views.MAN_View_Trainers, name='MAN_View_Trainers'),
    re_path(r'^MAN_View_Trainerprofile/(?P<id>\d+)$', views.MAN_View_Trainerprofile, name='MAN_View_Trainerprofile'),


    re_path(r'^MAN_View_Currenttraineesoftrainer/(?P<id>\d+)/$', views.MAN_View_Currenttraineesoftrainer, name='MAN_View_Currenttraineesoftrainer'),

    re_path(r'^MAN_View_Previoustraineesoftrainer/(?P<id>\d+)/$', views.MAN_View_Previoustraineesoftrainer, name='MAN_View_Previoustraineesoftrainer'),


    re_path(r'^MAN_View_Currenttraineeprofile/(?P<id>\d+)$', views.MAN_View_Currenttraineeprofile, name='MAN_View_Currenttraineeprofile'),

    re_path(r'^MAN_View_Currenttraineetasks/(?P<id>\d+)$', views.MAN_View_Currenttraineetasks, name='MAN_View_Currenttraineetasks'),

    re_path(r'^MAN_View_Currenttraineeattendance/(?P<id>\d+)$', views.MAN_View_Currenttraineeattendance, name='MAN_View_Currenttraineeattendance'),

    re_path(r'^MAN_View_Previoustraineesoftrainer$', views.MAN_View_Previoustraineesoftrainer, name='MAN_View_Previoustraineesoftrainer'),

    re_path(r'^MAN_View_Previoustraineeprofile/(?P<id>\d+)$', views.MAN_View_Previoustraineeprofile, name='MAN_View_Previoustraineeprofile'),

    re_path(r'^MAN_View_Previoustraineetasks/(?P<id>\d+)$', views.MAN_View_Previoustraineetasks, name='MAN_View_Previoustraineetasks'),

    re_path(r'^MAN_View_Previoustraineeattendance/(?P<id>\d+)$', views.MAN_View_Previoustraineeattendance, name='MAN_View_Previoustraineeattendance'),

    re_path(r'^MAN_View_Trainerattendance/(?P<id>\d+)$', views.MAN_View_Trainerattendance, name='MAN_View_Trainerattendance'),

    re_path(r'^MAN_ViewTrainerattendancesort/(?P<id>\d+)/$', views.MAN_ViewTrainerattendancesort, name='MAN_ViewTrainerattendancesort'),


    re_path(r'^MAN_ViewCurrenttraineeattendancesort/(?P<id>\d+)/$', views.MAN_ViewCurrenttraineeattendancesort, name='MAN_ViewCurrenttraineeattendancesort'),

    re_path(r'^MAN_ViewPrevioustraineeattendancesort/(?P<id>\d+)/$', views.MAN_ViewPrevioustraineeattendancesort, name='MAN_ViewPrevioustraineeattendancesort'),







    re_path(r'^MAN_dev_attendance$',views.MAN_dev_attendance,name='MAN_dev_attendance'),
    re_path(r'^MAN_page_1$',views.page_1,name='page_1'),
    re_path(r'^MAN_page_3$',views.page_3,name='page_3'),

    re_path(r'^desi$',views.desi,name='desi'),
    re_path(r'^emp$',views.emp,name='emp'),


#---------------------------- anwar end- ---------------

#-------- akhil---
    re_path(r'^MAN_Reportedissue$', views.MAN_Reportedissue, name='MAN_Reportedissue'),

    re_path(r'^MAN_ReportedissueShow/(?P<id>\d+)/$', views.MAN_ReportedissueShow, name='MAN_ReportedissueShow'),
    re_path(r'^MAN_ReportedissueShow1/(?P<id>\d+)/$', views.MAN_ReportedissueShow1, name='MAN_ReportedissueShow1'),



#------------ end
#-----praveeen----

    re_path(r'^MAN_trainerstable/$', views.MAN_trainerstable,name='MAN_trainerstable'),
    re_path(r'^MAN_Training/(?P<id>\d+)/$', views.MAN_Training,name='MAN_Training'),
    re_path(r'^MAN_trainingteam1/(?P<id>\d+)/$', views.MAN_trainingteam1,name='MAN_trainingteam1'),
    re_path(r'^MAN_traineestable/(?P<id>\d+)/$', views.MAN_traineestable,name='MAN_traineestable'),
    re_path(r'^MAN_trainingprofile/(?P<id>\d+)/$', views.MAN_trainingprofile,name='MAN_trainingprofile'),
    re_path(r'^MAN_completedtasktable/(?P<id>\d+)/$', views.MAN_completedtasktable,name='MAN_completedtasktable'),
    re_path(r'^MAN_topictable/(?P<id>\d+)/$', views.MAN_topictable,name='MAN_topictable'),

#------end praveeen----

#---sharoon------


   
    re_path(r'^MAN_employees3$', views.MAN_employees3, name='MAN_employees3'),
    re_path(r'^MAN_python$', views.MAN_python, name='MAN_python'),
    re_path(r'^MAN_projects/(?P<id>\d+)/$', views.MAN_projects, name='MAN_projects'),
    re_path(r'^MAN_proj_list/(?P<id>\d+)/$', views.MAN_proj_list, name='MAN_proj_list'),
    re_path(r'^MAN_proj_det/(?P<id>\d+)/$', views.MAN_proj_det, name='MAN_proj_det'),
    re_path(r'^MAN_proj_mngrs/(?P<id>\d+)/$', views.MAN_proj_mngrs, name='MAN_proj_mngrs'),
    re_path(r'^MAN_proj_mangrs1/(?P<id>\d+)/$', views.MAN_proj_mangrs1, name='MAN_proj_mangrs1'),
    re_path(r'^MAN_proj_mangrs2/(?P<id>\d+)/$', views.MAN_proj_mangrs2, name='MAN_proj_mangrs2'),  
    re_path(r'^MAN_daily_report/(?P<id>\d+)/$', views.MAN_daily_report, name='MAN_daily_report'),
    re_path(r'^MAN_developers/(?P<id>\d+)/$', views.MAN_developers, name='MAN_developers'),

#-------end sharon----
# ----subeesh-------

    re_path(r'^MAN_proj_cmpltd_new/(?P<id>\d+)$', views.MAN_proj_cmpltd_new, name='MAN_proj_cmpltd_new'),
    re_path(r'^MAN_cmpltd_proj_det_new/(?P<id>\d+)/$', views.MAN_cmpltd_proj_det_new, name='MAN_cmpltd_proj_det_new'),
    re_path(r'^MAN_proj_mngrs_new/(?P<id>\d+)/$', views.MAN_proj_mngrs_new, name='MAN_proj_mngrs_new'),
    re_path(r'^MAN_proj_mangrs1_new/(?P<id>\d+)/$', views.MAN_proj_mangrs1_new, name='MAN_proj_mangrs1_new'),
    re_path(r'^MAN_proj_mangrs2_new/(?P<id>\d+)/$', views.MAN_proj_mangrs2_new, name='MAN_proj_mangrs2_new'),
    re_path(r'^MAN_developers_new/(?P<id>\d+)/$', views.MAN_developers_new, name='MAN_developers_new'),
    re_path(r'^MAN_daily_report_new/(?P<id>\d+)/$', views.MAN_daily_report_new, name='MAN_daily_report_new'),


#----end----------


#-----nimisha-------

    re_path(r'^MAN_tasks$', views.MAN_tasks, name='MAN_tasks'),
    re_path(r'MAN_givetask$', views.MAN_givetask, name='MAN_givetask'),
    re_path(r'^MAN_currenttasks$', views.MAN_currenttasks, name='MAN_currenttasks'),
    re_path(r'^MAN_previoustasks$', views.MAN_previoustasks, name='MAN_previoustasks'),
    re_path(r'emp_task$', views.emp_task, name='emp_task'),
    re_path(r'desi_task$', views.desi_task, name='desi_task'),   

#----end----------
#--------safdhar-------
    re_path(r'^MAN_upcoming$', views.MAN_upcoming, name='MAN_upcoming'),

    re_path(r'^MAN_viewprojectform$', views.MAN_viewprojectform, name='MAN_viewprojectform'),
    re_path(r'^MAN_acceptedprojects$', views.MAN_acceptedprojects, name='MAN_acceptedprojects'),
    re_path(r'^MAN_rejected$', views.MAN_rejected, name='MAN_rejected'),
    re_path(r'^MAN_upcomingprojectsview$', views.MAN_upcomingprojectsview, name='MAN_upcomingprojectsview'),
  
    re_path(r'^MAN_createproject$', views.MAN_createproject, name='MAN_createproject'),
    
    re_path(r'^MAN_seradmintraineedesi1$', views.MAN_seradmintraineedesi1, name='MAN_seradmintraineedesi1'),
    re_path(r'^MAN_seradmindesig$', views.MAN_seradmindesig, name='MAN_seradmindesig'),



#----end----------


    

]