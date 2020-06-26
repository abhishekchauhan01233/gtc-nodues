from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission

# Create your models here.
class studentdata(models.Model):
    courses = (
        ('BCA','BCA'),
        ('BBA','BBA'),
        ('MBA','MBA'),
        ('BTech','BTech'),
        ('MTech','MTech'),
        ('Diploma','Diploma'),
    )

    branches = (
        ('CSE','CSE'),
        ('CE','CE'),
        ('ME','ME'),
        ('EE','EE'),
        ('ECE','ECE'),
        ('Auto','Auto'),
        ('BBA','BBA'),
        ('BCA','BCA'),
        ('MBA','MBA'),
    )

    semesters = (
        ('1st','1st'),
        ('2nd','2nd'),
        ('3rd','3rd'),
        ('4th','4th'),
        ('5th','5th'),
        ('6th','6th'),
        ('7th','7th'),
        ('8th','8th')
    )

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    course = models.CharField(max_length=50, choices=courses)
    branch = models.CharField(max_length=20, choices=branches)
    sem = models.CharField(max_length=20, choices=semesters)
    x = models.CharField(max_length=50)
    rollno = models.CharField(max_length=20)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    fname = models.CharField(max_length=50)
    phone = models.BigIntegerField()
    email = models.EmailField(max_length=100, blank=False)
    approval_status = models.CharField(max_length=200)

    def __str__(self):
        return self.user.username
    
class library(models.Model):
    courses = (
        ('BCA','BCA'),
        ('BBA','BBA'),
        ('MBA','MBA'),
        ('BTech','BTech'),
        ('MTech','MTech'),
        ('Diploma','Diploma'),
    )

    branches = (
        ('CSE','CSE'),
        ('CE','CE'),
        ('ME','ME'),
        ('M&A','M&A'),
        ('EE','EE'),
        ('ECE','ECE'),
        ('EPS','EPS'),
        ('Auto','Auto'),
        ('BBA','BBA'),
        ('BCA','BCA'),
        ('MBA','MBA'),
    )

    semesters = (
        ('1st','1st'),
        ('2nd','2nd'),
        ('3rd','3rd'),
        ('4th','4th'),
        ('5th','5th'),
        ('6th','6th'),
        ('7th','7th'),
        ('8th','8th')
    )

    payment_status = (
        ('Dues','dues'),
        ('Nodues','nodues')
    )

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    course = models.CharField(max_length=50, choices=courses)
    branch = models.CharField(max_length=20, choices=branches)
    sem = models.CharField(max_length=20, choices=semesters)
    rollno = models.CharField(max_length=20)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    fname = models.CharField(max_length=50)
    phone = models.BigIntegerField()
    email = models.EmailField(max_length=100, blank=False)
    status  = models.CharField(max_length=20, choices=payment_status)
    amount = models.CharField(max_length=500)
    transaction = models.CharField(max_length=100)
    receipt = models.CharField(max_length=100)
    approval_status = models.CharField(max_length=200)

    def __str__(self):
        return self.rollno
    
class exams(models.Model):
    courses = (
        ('BCA','BCA'),
        ('BBA','BBA'),
        ('MBA','MBA'),
        ('BTech','BTech'),
        ('MTech','MTech'),
        ('Diploma','Diploma'),
    )

    branches = (
        ('CSE','CSE'),
        ('CE','CE'),
        ('ME','ME'),
        ('M&A','M&A'),
        ('EE','EE'),
        ('ECE','ECE'),
        ('EPS','EPS'),
        ('Auto','Auto'),
        ('BBA','BBA'),
        ('BCA','BCA'),
        ('MBA','MBA'),
    )

    semesters = (
        ('1st','1st'),
        ('2nd','2nd'),
        ('3rd','3rd'),
        ('4th','4th'),
        ('5th','5th'),
        ('6th','6th'),
        ('7th','7th'),
        ('8th','8th')
    )

    payment_status = (
        ('Dues','dues'),
        ('Nodues','nodues')
    )

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    course = models.CharField(max_length=50, choices=courses)
    branch = models.CharField(max_length=20, choices=branches)
    sem = models.CharField(max_length=20, choices=semesters)
    rollno = models.CharField(max_length=20)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    fname = models.CharField(max_length=50)
    phone = models.BigIntegerField()
    email = models.EmailField(max_length=100, blank=False)
    status  = models.CharField(max_length=20, choices=payment_status)
    amount = models.CharField(max_length=500)
    transaction = models.CharField(max_length=100)
    receipt = models.CharField(max_length=100)
    approval_status = models.CharField(max_length=200)

    def __str__(self):
        return self.rollno

class accounts(models.Model):
    courses = (
        ('BCA','BCA'),
        ('BBA','BBA'),
        ('MBA','MBA'),
        ('BTech','BTech'),
        ('MTech','MTech'),
        ('Diploma','Diploma'),
    )

    branches = (
        ('CSE','CSE'),
        ('CE','CE'),
        ('ME','ME'),
        ('M&A','M&A'),
        ('EE','EE'),
        ('ECE','ECE'),
        ('EPS','EPS'),
        ('Auto','Auto'),
        ('BBA','BBA'),
        ('BCA','BCA'),
        ('MBA','MBA'),
    )

    semesters = (
        ('1st','1st'),
        ('2nd','2nd'),
        ('3rd','3rd'),
        ('4th','4th'),
        ('5th','5th'),
        ('6th','6th'),
        ('7th','7th'),
        ('8th','8th')
    )

    payment_status = (
        ('Dues','dues'),
        ('Nodues','nodues')
    )

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    course = models.CharField(max_length=50, choices=courses)
    branch = models.CharField(max_length=20, choices=branches)
    sem = models.CharField(max_length=20, choices=semesters)
    rollno = models.CharField(max_length=20)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    fname = models.CharField(max_length=50)
    phone = models.BigIntegerField()
    email = models.EmailField(max_length=100, blank=False)
    status  = models.CharField(max_length=20, choices=payment_status)
    amount = models.CharField(max_length=500)
    transaction = models.CharField(max_length=100)
    receipt = models.CharField(max_length=100)
    approval_status = models.CharField(max_length=200)

    def __str__(self):
        return self.rollno

class transport(models.Model):
    courses = (
        ('BCA','BCA'),
        ('BBA','BBA'),
        ('MBA','MBA'),
        ('BTech','BTech'),
        ('MTech','MTech'),
        ('Diploma','Diploma'),
    )

    branches = (
        ('CSE','CSE'),
        ('CE','CE'),
        ('ME','ME'),
        ('M&A','M&A'),
        ('EE','EE'),
        ('EPS','EPS'),
        ('Auto','Auto'),
        ('ECE','ECE'),
        ('BBA','BBA'),
        ('BCA','BCA'),
        ('MBA','MBA'),
    )

    semesters = (
        ('1st','1st'),
        ('2nd','2nd'),
        ('3rd','3rd'),
        ('4th','4th'),
        ('5th','5th'),
        ('6th','6th'),
        ('7th','7th'),
        ('8th','8th')
    )

    payment_status = (
        ('Dues','dues'),
        ('Nodues','nodues')
    )

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    course = models.CharField(max_length=50, choices=courses)
    branch = models.CharField(max_length=20, choices=branches)
    sem = models.CharField(max_length=20, choices=semesters)
    rollno = models.CharField(max_length=20)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    fname = models.CharField(max_length=50)
    phone = models.BigIntegerField()
    email = models.EmailField(max_length=100, blank=False)
    status  = models.CharField(max_length=20, choices=payment_status)
    amount = models.CharField(max_length=500)
    transaction = models.CharField(max_length=100)
    receipt = models.CharField(max_length=100)
    approval_status = models.CharField(max_length=200)

    def __str__(self):
        return self.rollno

class hostel(models.Model):
    courses = (
        ('BCA','BCA'),
        ('BBA','BBA'),
        ('MBA','MBA'),
        ('BTech','BTech'),
        ('MTech','MTech'),
        ('Diploma','Diploma'),
    )

    branches = (
        ('CSE','CSE'),
        ('CE','CE'),
        ('ME','ME'),
        ('M&A','M&A'),
        ('EE','EE'),
        ('ECE','ECE'),
        ('EPS','EPS'),
        ('Auto','Auto'),
        ('BBA','BBA'),
        ('BCA','BCA'),
        ('MBA','MBA'),
    )

    semesters = (
        ('1st','1st'),
        ('2nd','2nd'),
        ('3rd','3rd'),
        ('4th','4th'),
        ('5th','5th'),
        ('6th','6th'),
        ('7th','7th'),
        ('8th','8th')
    )

    payment_status = (
        ('Dues','dues'),
        ('Nodues','nodues')
    )

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    course = models.CharField(max_length=50, choices=courses)
    branch = models.CharField(max_length=20, choices=branches)
    sem = models.CharField(max_length=20, choices=semesters)
    rollno = models.CharField(max_length=20)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    fname = models.CharField(max_length=50)
    phone = models.BigIntegerField()
    email = models.EmailField(max_length=100, blank=False)
    status  = models.CharField(max_length=20, choices=payment_status)
    amount = models.CharField(max_length=500)
    transaction = models.CharField(max_length=100)
    receipt = models.CharField(max_length=100)
    approval_status = models.CharField(max_length=200)

    def __str__(self):
        return self.rollno

class HOD_CSE(models.Model):
    courses = (
        ('BCA','BCA'),
        ('BTech','BTech'),
        ('MTech','MTech'),
    )

    branches = (
        ('CSE','CSE'),
    )

    semesters = (
        ('1st','1st'),
        ('2nd','2nd'),
        ('3rd','3rd'),
        ('4th','4th'),
        ('5th','5th'),
        ('6th','6th'),
        ('7th','7th'),
        ('8th','8th')
    )

    payment_status = (
        ('Dues','dues'),
        ('Nodues','nodues')
    )

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    course = models.CharField(max_length=50, choices=courses)
    branch = models.CharField(max_length=20, choices=branches)
    sem = models.CharField(max_length=20, choices=semesters)
    rollno = models.CharField(max_length=20)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    fname = models.CharField(max_length=50)
    phone = models.BigIntegerField()
    email = models.EmailField(max_length=100, blank=False)
    approval_status = models.CharField(max_length=200)

    def __str__(self):
        return self.rollno

class HOD_ECE(models.Model):
    courses = (
        ('BTech','BTech'),
        ('MTech','MTech'),
        ('Diploma','Diploma'),
    )

    branches = (
        ('EE','EE'),
        ('ECE','ECE'),
        ('EPS','EPS')
    )

    semesters = (
        ('1st','1st'),
        ('2nd','2nd'),
        ('3rd','3rd'),
        ('4th','4th'),
        ('5th','5th'),
        ('6th','6th'),
        ('7th','7th'),
        ('8th','8th')
    )

    payment_status = (
        ('Dues','dues'),
        ('Nodues','nodues')
    )

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    course = models.CharField(max_length=50, choices=courses)
    branch = models.CharField(max_length=20, choices=branches)
    sem = models.CharField(max_length=20, choices=semesters)
    rollno = models.CharField(max_length=20)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    fname = models.CharField(max_length=50)
    phone = models.BigIntegerField()
    email = models.EmailField(max_length=100, blank=False)
    approval_status = models.CharField(max_length=200)

    def __str__(self):
        return self.rollno
    
class HOD_ME(models.Model):
    courses = (
        ('BTech','BTech'),
        ('MTech','MTech'),
        ('Diploma','Diploma'),
    )

    branches = (
        ('ME','ME'),
        ('M&A','M&A')
    )

    semesters = (
        ('1st','1st'),
        ('2nd','2nd'),
        ('3rd','3rd'),
        ('4th','4th'),
        ('5th','5th'),
        ('6th','6th'),
        ('7th','7th'),
        ('8th','8th')
    )

    payment_status = (
        ('Dues','dues'),
        ('Nodues','nodues')
    )

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    course = models.CharField(max_length=50, choices=courses)
    branch = models.CharField(max_length=20, choices=branches)
    sem = models.CharField(max_length=20, choices=semesters)
    rollno = models.CharField(max_length=20)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    fname = models.CharField(max_length=50)
    phone = models.BigIntegerField()
    email = models.EmailField(max_length=100, blank=False)
    approval_status = models.CharField(max_length=200)

    def __str__(self):
        return self.rollno

class HOD_AUTO(models.Model):
    courses = (
        ('Diploma','Diploma'),
    )

    branches = (
        ('Auto','Auto'),
    )

    semesters = (
        ('1st','1st'),
        ('2nd','2nd'),
        ('3rd','3rd'),
        ('4th','4th'),
        ('5th','5th'),
        ('6th','6th'),
        ('7th','7th'),
        ('8th','8th')
    )

    payment_status = (
        ('Dues','dues'),
        ('Nodues','nodues')
    )

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    course = models.CharField(max_length=50, choices=courses)
    branch = models.CharField(max_length=20, choices=branches)
    sem = models.CharField(max_length=20, choices=semesters)
    rollno = models.CharField(max_length=20)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    fname = models.CharField(max_length=50)
    phone = models.BigIntegerField()
    email = models.EmailField(max_length=100, blank=False)
    approval_status = models.CharField(max_length=200)

    def __str__(self):
        return self.rollno
    
class HOD_CIVIL(models.Model):
    courses = (
        ('BTech','BTech'),
        ('Diploma','Diploma'),
    )

    branches = (
        ('CE','CE'),
    )

    semesters = (
        ('1st','1st'),
        ('2nd','2nd'),
        ('3rd','3rd'),
        ('4th','4th'),
        ('5th','5th'),
        ('6th','6th'),
        ('7th','7th'),
        ('8th','8th')
    )

    payment_status = (
        ('Dues','dues'),
        ('Nodues','nodues')
    )

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    course = models.CharField(max_length=50, choices=courses)
    branch = models.CharField(max_length=20, choices=branches)
    sem = models.CharField(max_length=20, choices=semesters)
    rollno = models.CharField(max_length=20)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    fname = models.CharField(max_length=50)
    phone = models.BigIntegerField()
    email = models.EmailField(max_length=100, blank=False)
    approval_status = models.CharField(max_length=200)

    def __str__(self):
        return self.rollno

class HOD_1ST_YEAR(models.Model):
    courses = (
        ('BCA','BCA'),
        ('BBA','BBA'),
        ('BTech','BTech'),
        ('Diploma','Diploma'),
    )

    branches = (
        ('CSE','CSE'),
        ('CE','CE'),
        ('ME','ME'),
        ('Auto','Auto'),
        ('EE','EE'),
        ('ECE','ECE'),
        ('BBA','BBA'),
        ('BCA','BCA'),
    )

    semesters = (
        ('1st','1st'),
        ('2nd','2nd'),
    )

    payment_status = (
        ('Dues','dues'),
        ('Nodues','nodues')
    )

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    course = models.CharField(max_length=50, choices=courses)
    branch = models.CharField(max_length=20, choices=branches)
    sem = models.CharField(max_length=20, choices=semesters)
    rollno = models.CharField(max_length=20)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    fname = models.CharField(max_length=50)
    phone = models.BigIntegerField()
    email = models.EmailField(max_length=100, blank=False)
    approval_status = models.CharField(max_length=200)

    def __str__(self):
        return self.rollno
    
class HOD_MANAGEMENT(models.Model):
    courses = (
        ('BBA','BBA'),
        ('MBA','MBA'),
    )

    branches = (
        ('BBA','BBA'),
        ('MBA','MBA'),
    )

    semesters = (
        ('1st','1st'),
        ('2nd','2nd'),
        ('3rd','3rd'),
        ('4th','4th'),
        ('5th','5th'),
        ('6th','6th'),
    )

    payment_status = (
        ('Dues','dues'),
        ('Nodues','nodues')
    )

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    course = models.CharField(max_length=50, choices=courses)
    branch = models.CharField(max_length=20, choices=branches)
    sem = models.CharField(max_length=20, choices=semesters)
    rollno = models.CharField(max_length=20)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    fname = models.CharField(max_length=50)
    phone = models.BigIntegerField()
    email = models.EmailField(max_length=100, blank=False)
    approval_status = models.CharField(max_length=200)

    def __str__(self):
        return self.rollno