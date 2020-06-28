from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q, Count
from django.db import transaction
import threading
from .models import studentdata, library, accounts, exams, transport, hostel, HOD_CSE, HOD_ECE, HOD_CIVIL, HOD_AUTO, HOD_1ST_YEAR, HOD_MANAGEMENT, HOD_ME

def register(request):
    if request.user.is_authenticated:
        return redirect('/student/')

    else:
        if request.POST.get('adminsave'):
            return redirect('/admin/')

        elif request.method == 'POST':
            course = request.POST.get('course')
            branch = request.POST.get('branch')
            sem = request.POST.get('semester')
            rollno = request.POST.get('rollno')
            firstname = request.POST.get('firstname')
            lastname = request.POST.get('lastname')
            fname = request.POST.get('fname')
            pass1 = request.POST.get('password1')
            pass2 = request.POST.get('password2')
            phone = request.POST.get('phone')
            email = request.POST.get('email')

            if (pass1==pass2):
                if User.objects.filter(username=rollno).exists():
                    messages.error(request, "User with this Roll Number already exists")
                    return redirect('/')
                else:
                    user = User.objects.create_user(username=rollno, password=pass1, email=email, first_name=firstname, last_name=lastname)
                    user.save()
                    a = studentdata.objects.create(user=user,course=course,branch=branch, sem=sem, rollno=rollno, firstname=firstname, lastname=lastname,fname=fname, phone=phone, email=email)
                    b = library.objects.create(user=user,course=course,branch=branch, sem=sem, rollno=rollno, firstname=firstname, lastname=lastname,fname=fname, phone=phone, email=email)
                    c = accounts.objects.create(user=user,course=course,branch=branch, sem=sem, rollno=rollno, firstname=firstname, lastname=lastname,fname=fname, phone=phone, email=email)
                    d = exams.objects.create(user=user,course=course,branch=branch, sem=sem, rollno=rollno, firstname=firstname, lastname=lastname,fname=fname, phone=phone, email=email)
                    e = transport.objects.create(user=user,course=course,branch=branch, sem=sem, rollno=rollno, firstname=firstname, lastname=lastname,fname=fname, phone=phone, email=email)
                    f = hostel.objects.create(user=user,course=course,branch=branch, sem=sem, rollno=rollno, firstname=firstname, lastname=lastname,fname=fname, phone=phone, email=email)
                    a.save()
                    b.save()
                    c.save()
                    d.save()
                    e.save()
                    f.save()

                    if (sem == '1st' or sem=='2nd'):
                        g = HOD_1ST_YEAR.objects.create(user=user,course=course,branch=branch, sem=sem, rollno=rollno, firstname=firstname, lastname=lastname,fname=fname, phone=phone, email=email)
                        g.save()
                        return redirect('/login/')
                    
                    elif (branch == 'CSE' or branch == 'BCA') and (sem == '3rd' or sem == '4th' or sem == '5th' or sem == '6th' or sem == '7th' or sem == '8th'):
                        g = HOD_CSE.objects.create(user=user,course=course,branch=branch, sem=sem, rollno=rollno, firstname=firstname, lastname=lastname,fname=fname, phone=phone, email=email)
                        g.save()
                        return redirect('/login/')
                    
                    elif (branch =='ECE' or branch == 'EPS' or branch =='EE') and (sem == '3rd' or sem == '4th' or sem == '5th' or sem == '6th' or sem == '7th' or sem == '8th'):
                        g = HOD_ECE.objects.create(user=user,course=course,branch=branch, sem=sem, rollno=rollno, firstname=firstname, lastname=lastname,fname=fname, phone=phone, email=email)
                        g.save()
                        return redirect('/login/')

                    elif (branch=='M&A' or branch == 'ME') and (sem == '3rd' or sem == '4th' or sem == '5th' or sem == '6th' or sem == '7th' or sem == '8th'):
                        g = HOD_ME.objects.create(user=user,course=course,branch=branch, sem=sem, rollno=rollno, firstname=firstname, lastname=lastname,fname=fname, phone=phone, email=email)
                        g.save()
                        return redirect('/login/')
                    
                    elif (branch =='CE') and (sem == '3rd' or sem == '4th' or sem == '5th' or sem == '6th' or sem == '7th' or sem == '8th'):
                        g = HOD_CIVIL.objects.create(user=user,course=course,branch=branch, sem=sem, rollno=rollno, firstname=firstname, lastname=lastname,fname=fname, phone=phone, email=email)
                        g.save()
                        return redirect('/login/')

                    elif (branch =='Auto') and (sem == '3rd' or sem == '4th' or sem == '5th' or sem == '6th' or sem == '7th' or sem == '8th'):
                        g = HOD_AUTO.objects.create(user=user,course=course,branch=branch, sem=sem, rollno=rollno, firstname=firstname, lastname=lastname,fname=fname, phone=phone, email=email)
                        g.save()
                        return redirect('/login/')
                    
                    elif (branch=='MBA' or branch == 'BBA') and (sem == '3rd' or sem == '4th' or sem == '5th' or sem == '6th' or sem == '7th' or sem == '8th'):
                        g = HOD_MANAGEMENT.objects.create(user=user,course=course,branch=branch, sem=sem, rollno=rollno, firstname=firstname, lastname=lastname,fname=fname, phone=phone, email=email)
                        g.save()
                        return redirect('/login/')

            messages.error(request, "Password1 and Password2 did not match")
            return redirect('/')
    
        else:
            return render(request, 'main/register.html')

def login(request):
    if request.user.is_authenticated:
        return redirect('/student/')
    else:
        if request.method == "POST":
            rollno = request.POST.get('rollno')
            password = request.POST.get('password')

            user = auth.authenticate(username=rollno, password=password)
            
            if (rollno =='library') or (rollno == 'exams') or (rollno == 'accounts') or (rollno == 'transport') or (rollno == 'hostel') or (rollno == 'hod'):
                messages.error(request, "You have to login from the admin panel")
                return redirect('/login/')
            
            elif user is not None:
                auth.login(request, user)
                return redirect('/erp/')

            messages.error(request, "Invalid Credentials")
            return redirect('/login/')

        else:
            return render(request, 'main/login.html')

@login_required(login_url='/login/')
def erp(request):
    user = request.user
    userid = user.id

    data = studentdata.objects.get(user_id=userid)

    if request.POST.get('next'):
        return redirect('/student/')

    return render(request, 'main/erp.html', {'data':data})

@login_required(login_url='/login/')
def student(request):
    hod2(request)
    user = request.user
    userid = user.id

    data = studentdata.objects.get(user_id=userid)

    if request.POST.get('lsave'):
        return redirect('/library')
    
    elif request.POST.get('asave'):
        return redirect('/accounts')
    
    elif request.POST.get('esave'):
        return redirect('/exams')
    
    elif request.POST.get('tsave'):
        return redirect('/transport')
    
    elif request.POST.get('hsave'):
        return redirect('/hostel')
    
    elif request.POST.get('hosave'):
        return redirect('/hod')

    elif request.POST.get('losave'):
        auth.logout(request)
        return redirect('/login')

    return render(request, 'main/student.html', {'data':data})

@login_required(login_url='/login/')
def Library(request):
    user = request.user
    userid = user.id

    if request.POST.get('save'):
        status = request.POST.get('status')
        lib = library.objects.get(user_id=userid)
        lib.status = status
        lib.save()
        return redirect('student')

    return render(request, 'main/library.html')

@login_required(login_url='/login/')
def Library_Payment(request):
    user = request.user
    userid = user.id

    if request.POST.get('save'):
        amount_pending = request.POST.get('amount_pending')
        amount_paid = request.POST.get('amount_paid')
        transaction = request.POST.get('transaction')
        date = request.POST.get('date')
        books = request.POST.get('no._of_books')

        lib = library.objects.get(user_id=userid)
        lib.amount_pending = amount_pending
        lib.amount_paid = amount_paid
        lib.transaction = transaction
        lib.date = date
        lib.no_of_books = books
        lib.save()
        return redirect('student')

    return render(request, 'main/library_payment.html')

@login_required(login_url='/login/')
def Accounts(request):
    user = request.user
    userid = user.id

    if request.POST.get('save'):
        status = request.POST.get('status')
        account = accounts.objects.get(user_id=userid)
        account.status = status
        account.save()
        return redirect('student')
        
    return render(request, 'main/accounts.html')

@login_required(login_url='/login/')
def Accounts_Payment(request):
    user = request.user
    userid = user.id

    if request.POST.get('save'):
        amount_pending = request.POST.get('amount_pending')
        amount_paid = request.POST.get('amount_paid')
        transaction = request.POST.get('transaction')
        date = request.POST.get('date')

        account = accounts.objects.get(user_id=userid)
        account.amount_pending = amount_pending
        account.amount_paid = amount_paid
        account.transaction = transaction
        account.date = date
        account.save()
        return redirect('student')

    return render(request, 'main/payment.html')

@login_required(login_url='/login/')
def Exams(request):
    user = request.user
    userid = user.id

    if request.POST.get('save'):
        status = request.POST.get('status')
        exam = exams.objects.get(user_id=userid)
        exam.status = status
        exam.save()
        return redirect('student')
        
    return render(request, 'main/exams.html')

@login_required(login_url='/login/')
def Exams_Payment(request):
    user = request.user
    userid = user.id

    if request.POST.get('save'):
        amount_pending = request.POST.get('amount_pending')
        amount_paid = request.POST.get('amount_paid')
        transaction = request.POST.get('transaction')
        date = request.POST.get('date')

        exam = exams.objects.get(user_id=userid)
        exam.amount_pending = amount_pending
        exam.amount_paid = amount_paid
        exam.transaction = transaction
        exam.date = date
        exam.save()
        return redirect('student')

    return render(request, 'main/payment.html')

@login_required(login_url='/login/')
def Transport(request):
    user = request.user
    userid = user.id

    if request.POST.get('save'):
        status = request.POST.get('status')
        trans = transport.objects.get(user_id=userid)
        trans.status = status
        trans.save()
        return redirect('student')
        
    return render(request, 'main/transport.html')

@login_required(login_url='/login/')
def Transport_Payment(request):
    user = request.user
    userid = user.id

    if request.POST.get('save'):
        amount_pending = request.POST.get('amount_pending')
        amount_paid = request.POST.get('amount_paid')
        transaction = request.POST.get('transaction')
        date = request.POST.get('date')

        trans = transport.objects.get(user_id=userid)
        trans.amount_pending = amount_pending
        trans.amount_paid = amount_paid
        trans.transaction = transaction
        trans.date = date
        trans.save()
        return redirect('student')

    return render(request, 'main/payment.html')

@login_required(login_url='/login/')
def Hostel(request):
    user = request.user
    userid = user.id

    if request.POST.get('save'):
        status = request.POST.get('status')
        hos = hostel.objects.get(user_id=userid)
        hos.status=status
        hos.save()
        return redirect('student')
        
    return render(request, 'main/hostel.html')

@login_required(login_url='/login/')
def Hostel_Payment(request):
    user = request.user
    userid = user.id

    if request.POST.get('save'):
        amount_pending = request.POST.get('amount_pending')
        amount_paid = request.POST.get('amount_paid')
        transaction = request.POST.get('transaction')
        date = request.POST.get('date')

        hos = hostel.objects.get(user_id=userid)
        hos.amount_pending = amount_pending
        hos.amount_paid = amount_paid
        hos.transaction = transaction
        hos.date = date
        hos.save()
        return redirect('student')

    return render(request, 'main/payment.html')

@login_required(login_url='/login/')
def hod(request):
    user = request.user
    userid = user.id

    data = studentdata.objects.get(user_id=userid)

    if (data.sem == '1st' or data.sem == '2nd'):
        data2 = HOD_1ST_YEAR.objects.get(user_id=userid)
        lib = library.objects.get(user_id=userid)
        exam = exams.objects.get(user_id=userid)
        account = accounts.objects.get(user_id=userid)
        transport_ = transport.objects.get(user_id=userid)
        hostel_ = hostel.objects.get(user_id=userid)

        data2.approval_library = lib.approval_status
        data2.approval_exams = exam.approval_status
        data2.approval_accounts = account.approval_status
        data2.approval_transport = transport_.approval_status
        data2.approval_hostel = hostel_.approval_status
        data2.save() 
        if request.POST.get('save'):
            return redirect('student')

    elif (data.branch == 'CSE' or data.branch == 'BCA'):
        data2 = HOD_CSE.objects.get(user_id=userid)
        lib = library.objects.get(user_id=userid)
        exam = exams.objects.get(user_id=userid)
        account = accounts.objects.get(user_id=userid)
        transport_ = transport.objects.get(user_id=userid)
        hostel_ = hostel.objects.get(user_id=userid)

        data2.approval_library = lib.approval_status
        data2.approval_exams = exams.approval_status
        data2.approval_accounts = accounts.approval_status
        data2.approval_transport = transport_.approval_status
        data2.approval_hostel = hostel_.approval_status
        data2.save() 
        if request.POST.get('save'):
            return redirect('student')
    
    elif (data.branch == 'ECE' or data.branch == 'EE' or data.branch == 'EPS'):
        data2 = HOD_ECE.objects.get(user_id=userid)
        lib = library.objects.get(user_id=userid)
        exam = exams.objects.get(user_id=userid)
        account = accounts.objects.get(user_id=userid)
        transport_ = transport.objects.get(user_id=userid)
        hostel_ = hostel.objects.get(user_id=userid)

        data2.approval_library = lib.approval_status
        data2.approval_exams = exams.approval_status
        data2.approval_accounts = accounts.approval_status
        data2.approval_transport = transport_.approval_status
        data2.approval_hostel = hostel_.approval_status
        data2.save() 
        if request.POST.get('save'):
            return redirect('student')

    elif (data.branch == 'M&A' or data.branch == 'ME'):
        data2 = HOD_ME.objects.get(user_id=userid)
        lib = library.objects.get(user_id=userid)
        exam = exams.objects.get(user_id=userid)
        account = accounts.objects.get(user_id=userid)
        transport_ = transport.objects.get(user_id=userid)
        hostel_ = hostel.objects.get(user_id=userid)

        data2.approval_library = lib.approval_status
        data2.approval_exams = exams.approval_status
        data2.approval_accounts = accounts.approval_status
        data2.approval_transport = transport_.approval_status
        data2.approval_hostel = hostel_.approval_status
        data2.save() 
        if request.POST.get('save'):
            return redirect('student')
        
    elif (data.branch == 'CE'):
        data2 = HOD_CE.objects.get(user_id=userid)
        lib = library.objects.get(user_id=userid)
        exam = exams.objects.get(user_id=userid)
        account = accounts.objects.get(user_id=userid)
        transport_ = transport.objects.get(user_id=userid)
        hostel_ = hostel.objects.get(user_id=userid)

        data2.approval_library = lib.approval_status
        data2.approval_exams = exams.approval_status
        data2.approval_accounts = accounts.approval_status
        data2.approval_transport = transport_.approval_status
        data2.approval_hostel = hostel_.approval_status
        data2.save() 
        if request.POST.get('save'):
            return redirect('student')
        
    elif (data.branch == 'Auto'):
        data2 = HOD_AUTO.objects.get(user_id=userid)
        lib = library.objects.get(user_id=userid)
        exam = exams.objects.get(user_id=userid)
        account = accounts.objects.get(user_id=userid)
        transport_ = transport.objects.get(user_id=userid)
        hostel_ = hostel.objects.get(user_id=userid)

        data2.approval_library = lib.approval_status
        data2.approval_exams = exams.approval_status
        data2.approval_accounts = accounts.approval_status
        data2.approval_transport = transport_.approval_status
        data2.approval_hostel = hostel_.approval_status
        data2.save() 
        if request.POST.get('save'):
            return redirect('student')
        
    elif (data.branch == 'BBA' or data.branch == 'MBA'):
        data2 = HOD_MANAGEMENT.objects.get(user_id=userid)
        lib = library.objects.get(user_id=userid)
        exam = exams.objects.get(user_id=userid)
        account = accounts.objects.get(user_id=userid)
        transport_ = transport.objects.get(user_id=userid)
        hostel_ = hostel.objects.get(user_id=userid)

        data2.approval_library = lib.approval_status
        data2.approval_exams = exams.approval_status
        data2.approval_accounts = accounts.approval_status
        data2.approval_transport = transport_.approval_status
        data2.approval_hostel = hostel_.approval_status
        data2.save() 
        if request.POST.get('save'):
            return redirect('student')
        
    return render(request, 'main/hod.html', {'data':data2})

def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if auth.authenticate(username=username, password=password):
            user = auth.authenticate(username=username, password=password)
            auth.login(request, user)
            if (username =='library'):
                return redirect('/admin_library/')
            elif(username == 'exams'):
                return redirect('/admin_exams/')
            elif(username == 'accounts'):
                return redirect('/admin_accounts/')
            elif(username == 'transport'):
                return redirect('/admin_transport/')
            elif(username == 'hostel'):
                return redirect('/admin_hostel/')
            elif(username == 'hod'):
                return redirect('/admin_hod/')
            elif(username == 'ritesh'):
                return redirect('/admin/')

        
        messages.error(request, "Invalid Credentials")
        return redirect('/admin_login/')

    return render(request, 'main/admin_login.html')

@login_required(login_url='/admin_login/')
def admin_library(request):
    data = library.objects.all() 

    if request.POST.get('logout'):
        auth.logout(request)
        return redirect('/admin_login/')

    elif request.POST.get('submit'):
        course = request.POST.get('course')
        branch = request.POST.get('branch')
        semester = request.POST.get('semester')

        data2 = library.objects.filter(course=course, branch=branch, sem=semester)
        return render(request, 'main/admin_library.html', {'data':data2})

    elif request.POST.get('save'):
        course = request.POST.get('course')
        branch = request.POST.get('branch')
        semester = request.POST.get('semester')
        rollno = request.POST.get('rollno')
        status = request.POST.get('status')
        amount = request.POST.get('amount')

        for x in library.objects.filter(rollno=rollno):
            library.objects.filter(rollno=rollno).update(status=status, amount_to_be_paid=amount)

        data3 = library.objects.all()
        return render(request, 'main/admin_library.html', {'data':data3})

    return render(request, 'main/admin_library.html', {'data':data})

@login_required(login_url='/admin_login/')
def admin_exams(request):
    data = exams.objects.all() 

    if request.POST.get('logout'):
        auth.logout(request)
        return redirect('/admin_login/')

    elif request.POST.get('submit'):
        course = request.POST.get('course')
        branch = request.POST.get('branch')
        semester = request.POST.get('semester')

        data2 = exams.objects.filter(course=course, branch=branch, sem=semester)
        return render(request, 'main/admin_exams.html', {'data':data2})

    elif request.POST.get('save'):
        course = request.POST.get('course')
        branch = request.POST.get('branch')
        semester = request.POST.get('semester')
        rollno = request.POST.get('rollno')
        status = request.POST.get('status')
        amount = request.POST.get('amount')

        for x in exams.objects.filter(rollno=rollno):
            exams.objects.filter(rollno=rollno).update(status=status, amount_to_be_paid=amount)

        data3 = exams.objects.all()
        return render(request, 'main/admin_exams.html', {'data':data3})

    return render(request, 'main/admin_exams.html', {'data':data})

@login_required(login_url='/admin_login/')
def admin_accounts(request):

    data = accounts.objects.filter() 

    if request.POST.get('logout'):
        auth.logout(request)
        return redirect('/admin_login/')

    elif request.POST.get('submit'):
        course = request.POST.get('course')
        branch = request.POST.get('branch')
        semester = request.POST.get('semester')

        data2 = accounts.objects.filter(course=course, branch=branch, sem=semester)
        return render(request, 'main/admin_accounts.html', {'data':data2})

    elif request.POST.get('save'):
        row = request.POST.get('rollno')
        course = request.POST.get('course')
        branch = request.POST.get('branch')
        semester = request.POST.get('semester')
        rollno = request.POST.get('rollno')
        status = request.POST.get('status')
        amount = request.POST.get('amount')

        data3 = accounts.objects.all()
        return render(request, 'main/admin_accounts.html', {'data':data3})

    return render(request, 'main/admin_accounts.html', {'data':data})

@login_required(login_url='/admin_login/')
def admin_transport(request):
    data = transport.objects.all() 

    if request.POST.get('logout'):
        auth.logout(request)
        return redirect('/admin_login/')

    elif request.POST.get('submit'):
        course = request.POST.get('course')
        branch = request.POST.get('branch')
        semester = request.POST.get('semester')

        data2 = transport.objects.filter(course=course, branch=branch, sem=semester)
        return render(request, 'main/admin_transport.html', {'data':data2})

    elif request.POST.get('save'):
        course = request.POST.get('course')
        branch = request.POST.get('branch')
        semester = request.POST.get('semester')
        rollno = request.POST.get('rollno')
        status = request.POST.get('status')
        amount = request.POST.get('amount')

        for x in transport.objects.filter(rollno=rollno):
            transport.objects.filter(rollno=rollno).update(status=status, amount_to_be_paid=amount)

        data3 = transport.objects.all()
        return render(request, 'main/admin_transport.html', {'data':data3})

    return render(request, 'main/admin_transport.html', {'data':data})

@login_required(login_url='/admin_login/')
def admin_hostel(request):
    data = hostel.objects.all() 

    if request.POST.get('logout'):
        auth.logout(request)
        return redirect('/admin_login/')

    elif request.POST.get('submit'):
        course = request.POST.get('course')
        branch = request.POST.get('branch')
        semester = request.POST.get('semester')

        data2 = hostel.objects.filter(course=course, branch=branch, sem=semester)
        return render(request, 'main/admin_hostel.html', {'data':data2})

    elif request.POST.get('save'):
        course = request.POST.get('course')
        branch = request.POST.get('branch')
        semester = request.POST.get('semester')
        rollno = request.POST.get('rollno')
        status = request.POST.get('status')
        amount = request.POST.get('amount')

        for x in hostel.objects.filter(rollno=rollno):
            hostel.objects.filter(rollno=rollno).update(status=status, amount_to_be_paid=amount)

        data3 = hostel.objects.all()
        return render(request, 'main/admin_hostel.html', {'data':data3})

    return render(request, 'main/admin_hostel.html', {'data':data})

@login_required(login_url='/admin_login/')
def admin_hod(request):
    data = HOD.objects.all() 

    if request.POST.get('logout'):
        auth.logout(request)
        return redirect('/admin_login/')

    elif request.POST.get('submit'):
        course = request.POST.get('course')
        branch = request.POST.get('branch')
        semester = request.POST.get('semester')

        data2 = HOD.objects.filter(course=course, branch=branch, sem=semester)
        return render(request, 'main/admin_hod.html', {'data':data2})

    elif request.POST.get('save'):
        course = request.POST.get('course')
        branch = request.POST.get('branch')
        semester = request.POST.get('semester')
        rollno = request.POST.get('rollno')
        status = request.POST.get('status')
        amount = request.POST.get('amount')

        for x in HOD.objects.filter(rollno=rollno):
            HOD.objects.filter(rollno=rollno).update(status=status, amount_to_be_paid=amount)

        data3 = HOD.objects.all()
        return render(request, 'main/admin_hod.html', {'data':data3})

    return render(request, 'main/admin_hod.html', {'data':data})

def hod2(request):
    user = request.user
    userid = user.id

    data = studentdata.objects.get(user_id=userid)

    if (data.sem == '1st' or data.sem == '2nd'):
        data2 = HOD_1ST_YEAR.objects.get(user_id=userid)
        lib = library.objects.get(user_id=userid)
        exam = exams.objects.get(user_id=userid)
        account = accounts.objects.get(user_id=userid)
        transport_ = transport.objects.get(user_id=userid)
        hostel_ = hostel.objects.get(user_id=userid)

        data2.approval_library = lib.approval_status
        data2.approval_exams = exam.approval_status
        data2.approval_accounts = account.approval_status
        data2.approval_transport = transport_.approval_status
        data2.approval_hostel = hostel_.approval_status
        data2.save() 

    elif (data.branch == 'CSE' or data.branch == 'BCA'):
        data2 = HOD_CSE.objects.get(user_id=userid)
        lib = library.objects.get(user_id=userid)
        exam = exams.objects.get(user_id=userid)
        account = accounts.objects.get(user_id=userid)
        transport_ = transport.objects.get(user_id=userid)
        hostel_ = hostel.objects.get(user_id=userid)

        data2.approval_library = lib.approval_status
        data2.approval_exams = exams.approval_status
        data2.approval_accounts = accounts.approval_status
        data2.approval_transport = transport_.approval_status
        data2.approval_hostel = hostel_.approval_status
        data2.save() 
    
    elif (data.branch == 'ECE' or data.branch == 'EE' or data.branch == 'EPS'):
        data2 = HOD_ECE.objects.get(user_id=userid)
        lib = library.objects.get(user_id=userid)
        exam = exams.objects.get(user_id=userid)
        account = accounts.objects.get(user_id=userid)
        transport_ = transport.objects.get(user_id=userid)
        hostel_ = hostel.objects.get(user_id=userid)

        data2.approval_library = lib.approval_status
        data2.approval_exams = exams.approval_status
        data2.approval_accounts = accounts.approval_status
        data2.approval_transport = transport_.approval_status
        data2.approval_hostel = hostel_.approval_status
        data2.save() 

    elif (data.branch == 'M&A' or data.branch == 'ME'):
        data2 = HOD_ME.objects.get(user_id=userid)
        lib = library.objects.get(user_id=userid)
        exam = exams.objects.get(user_id=userid)
        account = accounts.objects.get(user_id=userid)
        transport_ = transport.objects.get(user_id=userid)
        hostel_ = hostel.objects.get(user_id=userid)

        data2.approval_library = lib.approval_status
        data2.approval_exams = exams.approval_status
        data2.approval_accounts = accounts.approval_status
        data2.approval_transport = transport_.approval_status
        data2.approval_hostel = hostel_.approval_status
        data2.save() 
        
    elif (data.branch == 'CE'):
        data2 = HOD_CE.objects.get(user_id=userid)
        lib = library.objects.get(user_id=userid)
        exam = exams.objects.get(user_id=userid)
        account = accounts.objects.get(user_id=userid)
        transport_ = transport.objects.get(user_id=userid)
        hostel_ = hostel.objects.get(user_id=userid)

        data2.approval_library = lib.approval_status
        data2.approval_exams = exams.approval_status
        data2.approval_accounts = accounts.approval_status
        data2.approval_transport = transport_.approval_status
        data2.approval_hostel = hostel_.approval_status
        data2.save() 
        
    elif (data.branch == 'Auto'):
        data2 = HOD_AUTO.objects.get(user_id=userid)
        lib = library.objects.get(user_id=userid)
        exam = exams.objects.get(user_id=userid)
        account = accounts.objects.get(user_id=userid)
        transport_ = transport.objects.get(user_id=userid)
        hostel_ = hostel.objects.get(user_id=userid)

        data2.approval_library = lib.approval_status
        data2.approval_exams = exams.approval_status
        data2.approval_accounts = accounts.approval_status
        data2.approval_transport = transport_.approval_status
        data2.approval_hostel = hostel_.approval_status
        data2.save() 
        
    elif (data.branch == 'BBA' or data.branch == 'MBA'):
        data2 = HOD_MANAGEMENT.objects.get(user_id=userid)
        lib = library.objects.get(user_id=userid)
        exam = exams.objects.get(user_id=userid)
        account = accounts.objects.get(user_id=userid)
        transport_ = transport.objects.get(user_id=userid)
        hostel_ = hostel.objects.get(user_id=userid)

        data2.approval_library = lib.approval_status
        data2.approval_exams = exams.approval_status
        data2.approval_accounts = accounts.approval_status
        data2.approval_transport = transport_.approval_status
        data2.approval_hostel = hostel_.approval_status
        data2.save() 