# Generated by Django 3.2.8 on 2022-02-19 09:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='branch_registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch_name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('branch_admin', models.CharField(max_length=100)),
                ('branch_type', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='create_team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('trainer', models.CharField(default='', max_length=200)),
                ('progress', models.IntegerField()),
                ('status', models.CharField(max_length=200)),
                ('team_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('branch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='departmentbranch', to='base_app.branch_registration')),
            ],
        ),
        migrations.CreateModel(
            name='designation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('branch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='designationbranch', to='base_app.branch_registration')),
            ],
        ),
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('startdate', models.DateField(blank=True, null=True)),
                ('enddate', models.DateField(blank=True, null=True)),
                ('files', models.FileField(blank=True, null=True, upload_to='images/')),
                ('progress', models.CharField(max_length=100)),
                ('user_reason', models.CharField(blank=True, max_length=100, null=True)),
                ('status', models.CharField(blank=True, max_length=100, null=True)),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='projectdepartment', to='base_app.department')),
                ('designation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='projectdesignation', to='base_app.designation')),
            ],
        ),
        migrations.CreateModel(
            name='project_taskassign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('startdate', models.DateField(blank=True, null=True)),
                ('enddate', models.DateField(blank=True, null=True)),
                ('files', models.FileField(blank=True, null=True, upload_to='images/')),
                ('extension', models.IntegerField()),
                ('reason', models.TextField(blank=True, null=True)),
                ('extension_status', models.CharField(blank=True, max_length=200, null=True)),
                ('tl_description', models.CharField(blank=True, max_length=200, null=True)),
                ('submitted_date', models.DateField(blank=True, null=True)),
                ('employee_files', models.FileField(blank=True, null=True, upload_to='images/')),
                ('employee_description', models.TextField(blank=True, null=True)),
                ('status', models.CharField(blank=True, max_length=200, null=True)),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='project_taskassignproject', to='base_app.project')),
            ],
        ),
        migrations.CreateModel(
            name='user_registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=240, null=True)),
                ('fathername', models.CharField(max_length=240, null=True)),
                ('mothername', models.CharField(max_length=240, null=True)),
                ('dateofbirth', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(max_length=240, null=True)),
                ('presentaddress1', models.CharField(max_length=240, null=True)),
                ('presentaddress2', models.CharField(max_length=240, null=True)),
                ('presentaddress3', models.CharField(max_length=240, null=True)),
                ('pincode', models.CharField(max_length=240, null=True)),
                ('district', models.CharField(max_length=240, null=True)),
                ('state', models.CharField(max_length=240, null=True)),
                ('country', models.CharField(max_length=240, null=True)),
                ('permanentaddress1', models.CharField(max_length=240, null=True)),
                ('permanentaddress2', models.CharField(max_length=240, null=True)),
                ('permanentaddress3', models.CharField(max_length=240, null=True)),
                ('permanentpincode', models.CharField(max_length=240, null=True)),
                ('permanentdistrict', models.CharField(max_length=240, null=True)),
                ('permanentstate', models.CharField(max_length=240, null=True)),
                ('permanentcountry', models.CharField(max_length=240, null=True)),
                ('mobile', models.CharField(max_length=240, null=True)),
                ('alternativeno', models.CharField(max_length=240, null=True)),
                ('email', models.EmailField(max_length=240, null=True)),
                ('password', models.CharField(max_length=240, null=True)),
                ('idproof', models.FileField(blank=True, null=True, upload_to='images/')),
                ('photo', models.FileField(blank=True, null=True, upload_to='images/')),
                ('attitude', models.PositiveIntegerField(default='')),
                ('creativity', models.PositiveIntegerField(default='')),
                ('workperformance', models.PositiveIntegerField(default='')),
                ('joiningdate', models.DateField(blank=True, null=True)),
                ('startdate', models.DateField(blank=True, null=True)),
                ('enddate', models.DateField(blank=True, null=True)),
                ('status', models.CharField(default='', max_length=240, null=True)),
                ('branch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='userregistrationbranch', to='base_app.branch_registration')),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='userregistrationdepartment', to='base_app.department')),
                ('designation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='userregistrationdesignation', to='base_app.designation')),
                ('team', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='userregistrationteam', to='base_app.create_team')),
            ],
        ),
        migrations.CreateModel(
            name='trainer_task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskname', models.CharField(max_length=240)),
                ('startdate', models.DateField(blank=True, null=True)),
                ('enddate', models.DateField(blank=True, null=True)),
                ('files', models.FileField(blank=True, null=True, upload_to='images/')),
                ('description', models.TextField(max_length=240)),
                ('user_description', models.TextField(max_length=240)),
                ('user_files', models.FileField(blank=True, null=True, upload_to='images/')),
                ('status', models.CharField(max_length=200)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='trainer_task_trainee', to='base_app.user_registration')),
            ],
        ),
        migrations.CreateModel(
            name='topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=240)),
                ('startdate', models.DateField(blank=True, null=True)),
                ('enddate', models.DateField(blank=True, null=True)),
                ('files', models.FileField(blank=True, null=True, upload_to='images/')),
                ('description', models.TextField()),
                ('review', models.TextField()),
                ('status', models.CharField(max_length=200)),
                ('team', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='topicteam', to='base_app.create_team')),
                ('trainer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='topictrainer', to='base_app.user_registration')),
            ],
        ),
        migrations.CreateModel(
            name='tester_status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('workdone', models.TextField(blank=True, max_length=200, null=True)),
                ('files', models.FileField(blank=True, null=True, upload_to='images/')),
                ('subtask', models.TextField(blank=True, max_length=200, null=True)),
                ('progress', models.IntegerField()),
                ('status', models.CharField(blank=True, max_length=200, null=True)),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='tester_statusproject', to='base_app.project')),
                ('task', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='tester_statustask', to='base_app.project_taskassign')),
                ('tester', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='tester_statustester', to='base_app.user_registration')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='tester_statususer', to='base_app.user_registration')),
            ],
        ),
        migrations.CreateModel(
            name='test_status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('workdone', models.TextField(null=True)),
                ('files', models.FileField(blank=True, null=True, upload_to='images/')),
                ('project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='test_statusproject', to='base_app.project')),
                ('taskname', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='test_statustaskname', to='base_app.user_registration')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='test_statususer', to='base_app.user_registration')),
            ],
        ),
        migrations.CreateModel(
            name='reported_issue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue', models.TextField()),
                ('reported_date', models.DateField(blank=True, null=True)),
                ('reply', models.TextField()),
                ('status', models.CharField(max_length=200)),
                ('reported_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='reported_issuereported_to', to='base_app.user_registration')),
                ('reporter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='reported_issuereporter', to='base_app.user_registration')),
            ],
        ),
        migrations.CreateModel(
            name='qualification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plustwo', models.CharField(max_length=240, null=True)),
                ('schoolaggregate', models.CharField(max_length=240, null=True)),
                ('schoolcertificate', models.FileField(blank=True, null=True, upload_to='images/')),
                ('ugdegree', models.CharField(max_length=240, null=True)),
                ('ugstream', models.CharField(max_length=240, null=True)),
                ('ugpassoutyr', models.CharField(max_length=240, null=True)),
                ('ugaggregrate', models.CharField(max_length=240, null=True)),
                ('backlogs', models.CharField(max_length=240, null=True)),
                ('ugcertificate', models.FileField(blank=True, null=True, upload_to='images/')),
                ('pg', models.CharField(max_length=240, null=True)),
                ('status', models.CharField(default='', max_length=100)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='qualificationuser', to='base_app.user_registration')),
            ],
        ),
        migrations.AddField(
            model_name='project_taskassign',
            name='tester',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='project_taskassign_tester', to='base_app.user_registration'),
        ),
        migrations.AddField(
            model_name='project_taskassign',
            name='tl',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='project_taskassigntl', to='base_app.user_registration'),
        ),
        migrations.AddField(
            model_name='project_taskassign',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='project_taskassignuser', to='base_app.user_registration'),
        ),
        migrations.AddField(
            model_name='project',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='projectuser', to='base_app.user_registration'),
        ),
        migrations.CreateModel(
            name='leave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_date', models.DateField(blank=True, null=True)),
                ('to_date', models.DateField(blank=True, null=True)),
                ('reason', models.TextField()),
                ('leave_status', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=200)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='leaveuser', to='base_app.user_registration')),
            ],
        ),
        migrations.CreateModel(
            name='internship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_date', models.DateField(blank=True, null=True)),
                ('fullname', models.CharField(max_length=200)),
                ('collegename', models.CharField(max_length=200)),
                ('reg_no', models.CharField(max_length=200)),
                ('course', models.CharField(max_length=200)),
                ('stream', models.CharField(max_length=200)),
                ('platform', models.CharField(max_length=200)),
                ('start_date', models.CharField(max_length=200)),
                ('end_date', models.CharField(max_length=200)),
                ('mobile', models.CharField(max_length=200)),
                ('alternative_no', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('attach_file', models.FileField(blank=True, null=True, upload_to='images/')),
                ('rating', models.CharField(max_length=200)),
                ('hrmanager', models.CharField(max_length=200)),
                ('guide', models.CharField(max_length=200)),
                ('qr', models.CharField(default='', max_length=200)),
                ('status', models.CharField(max_length=200)),
                ('branch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='internshipbranch', to='base_app.branch_registration')),
            ],
        ),
        migrations.CreateModel(
            name='extracurricular',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('internshipdetails', models.CharField(max_length=240, null=True)),
                ('internshipduration', models.CharField(max_length=240, null=True)),
                ('internshipcertificate', models.FileField(blank=True, null=True, upload_to='images/')),
                ('onlinetrainingdetails', models.CharField(max_length=240, null=True)),
                ('onlinetrainingduration', models.CharField(max_length=240, null=True)),
                ('onlinetrainingcertificate', models.FileField(blank=True, null=True, upload_to='images/')),
                ('projecttitle', models.CharField(max_length=240, null=True)),
                ('projectduration', models.CharField(max_length=240, null=True)),
                ('projectdescription', models.TextField(null=True)),
                ('projecturl', models.CharField(blank=True, default='', max_length=240, null=True)),
                ('skill1', models.CharField(blank=True, default='', max_length=240, null=True)),
                ('skill2', models.CharField(blank=True, default='', max_length=240, null=True)),
                ('skill3', models.CharField(blank=True, default='', max_length=240, null=True)),
                ('status', models.CharField(default='', max_length=240)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='extracurricularuser', to='base_app.user_registration')),
            ],
        ),
        migrations.CreateModel(
            name='attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(max_length=200)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='attendanceuser', to='base_app.user_registration')),
            ],
        ),
    ]