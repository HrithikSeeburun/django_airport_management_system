from django.shortcuts import render
from .models import airport, airline_company, flight, employee, passenger, immigration, runway, store, runway1, runway2, runway3, runway4
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
# Create your views here.
def home(req):
    return render(req, 'login.html')
def login_page(req):
    return render(req, 'login.html')
def loadin(req):
    if req.method == 'POST':
        username = req.POST['username']
        password = req.POST['password']
        user = authenticate(username=username, password=password)
        print(user)
        if user is None:
            messages.info(req, "You Have Entered Wrong Credentials")
            return render(req, 'login.html')
        else:
            login(req, user)
            return render(req, 'airport.html')

def employee_registration(req):
    return render(req, 'employee_registration.html')

def employee_register(req):
    if req.method == "POST":
        first_name = req.POST['fname']
        last_name = req.POST['lname']
        e_id = req.POST['e_id']
        username = req.POST['username']
        password = req.POST['password']
        cpassword = req.POST['cpassword']
        pno = req.POST['pno']
        address = req.POST['address']
        salary = req.POST['salary']
        designation = req.POST['designation']
        department = req.POST['department']
        age = req.POST['age']
        gender = req.POST['gender']
        email = req.POST['email']
        if User.objects.filter(username=username).exists():
            messages.info(req, "User Already Exists.Kindly Go For Login Page")
            return render(req, 'airport.html')
        else:
            if (password == cpassword):
                u = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                u.save()
                user = User.objects.get(username=username)
                e = employee(user=user, E_id=e_id, E_name=first_name, E_password=password, E_c_password=cpassword,
                              E_pno=pno, E_address=address, E_salary=salary,
                              E_designation=designation, E_department=department, E_age=age, E_gender=gender,
                              E_email=email, user_type='emp')
                e.save()
                return render(req, 'airport.html')
    else:

        return render(req, 'employee_registration.html')


def manager_registration(req):
    return render(req, 'manager_registration.html')

def manager_register(req):
    if req.method == "POST":
        first_name = req.POST['fname']
        last_name = req.POST['lname']
        username = req.POST['username']
        password = req.POST['password']
        cpassword = req.POST['cpassword']
        email = req.POST['email']
        a_id = req.POST['a_id']
        a_name = req.POST['a_name']
        a_country = req.POST['a_country']

        if User.objects.filter(username=username).exists():
            messages.info(req, "User Already Exists, Kindly Go For Login Page")
            return render(req, 'login.html')
        else:
            if (password == cpassword):
                u = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                u.save()
                user = User.objects.get(username=username)
                return render(req, 'login.html')
            else:
                messages.info(req, "Password Did Not Match, Please Enter Correct Password")
                return render(req, 'login.html')
    else:
        return render(req,'manager_registration.html')

def load_airport(req):
    return render(req, 'airport.html')
def add_airline(req):
    if req.method == 'POST':
        flight_id = req.POST['flight_id']
        a_name = req.POST['a_name']
        u = req.user
        print("the current user id", u)
        x = airline_company(flight_id=flight_id, airline_name=a_name)
        x.save()
        return render(req, 'airport.html')


def load_airlineadd(req):
    return render(req, 'add_airline.html')

def load_airline_company(req):
    A = airline_company.objects.all()
    return render(req, 'airline_company.html', {'ac': A})

def load_employee(req):
    E = employee.objects.all()
    return render(req, 'employee.html', {'em': E})

def add_immigration(req):
    if req.method == 'POST':
        E_id = req.POST['E_id']
        a = employee.objects.get(E_id=E_id)
        p_name = req.POST['p_name']
        b = passenger.objects.get(P_name=p_name)
        E_name = req.POST['E_name']
        u = req.user
        print("the current user is ", u)
        x = immigration(E_id=a, P_name=b, E_name=E_name)
        x.save()
        return render(req, 'airport.html')

def load_immigrationadd(req):
    return render(req, 'add_immigration.html')

def load_immigration(req):
    IM = immigration.objects.all()
    return render(req, 'immigration.html', {'im': IM})

def load_flight(req):
    if flight.objects.filter(status='departure').exists():
        D = flight.objects.filter(status='departure')
        if flight.objects.filter(status='arrival').exists():
            A = flight.objects.filter(status='arrival')
            return render(req, 'flight.html', {'d': D, 'a': A})
        else:
            return render(req, 'flight.html')



def add_flight(req):
    if req.method == 'POST':
        fid = req.POST['flight_id']
        y = airline_company.objects.get(flight_id=fid)
        f_time = req.POST['f_time']
        f_date = req.POST['f_date']
        f_from = req.POST['f_from']
        f_to = req.POST['f_to']
        f_status = req.POST['f_status']
        status = req.POST['status']
        u = req.user
        print("the current user is ", u)
        x = flight(f_id=y, f_time=f_time, f_date=f_date, f_from=f_from, f_to=f_to, f_status=f_status,
                   status=status)
        x.save()
        return render(req, 'airport.html')

def load_flightadd(req):
    return render(req, 'add_flight.html')

def add_passenger(req):
    if req.method == 'POST':
        fid = req.POST['flight_id']
        y = airline_company.objects.get(flight_id=fid)
        p_id = req.POST['p_id']
        p_status = req.POST['p_status']
        p_age = req.POST['p_age']
        p_name = req.POST['p_name']
        p_gender = req.POST['p_gender']
        u = req.user
        print("the current user is ", u)
        x = passenger(flight_id=y, P_id=p_id, P_status=p_status, P_age=p_age, P_name=p_name, P_gender=p_gender)
        x.save()
        return render(req, 'airport.html')

def load_passengeradd(req):
    return render(req, 'add_passenger.html')

def load_runway(req):
    date=datetime.today()
    R1 = runway.objects.filter(date=date)
    R2 = runway1.objects.filter(date=date)
    R3 = runway2.objects.filter(date=date)
    R4 = runway3.objects.filter(date=date)
    R5 = runway4.objects.filter(date=date)
    return render(req, 'runway.html', {'r1': R1, 'r2': R2, 'r3': R3, 'r4': R4, 'r5': R5})

from datetime import datetime
date2 = datetime.now().date()
def add_runway(req):
    if req.method == 'POST':
        f_id = req.POST['f_id']
        y = airline_company.objects.get(flight_id=f_id)
        r_id = req.POST['r_id']
        status_of_terminal = req.POST['status_of_terminal']

        date1 = req.POST['date']
        print("the date is", date1)
        print("today's date is", date2)
        import datetime as dt
        d = dt.datetime.strptime(date1, "%Y-%m-%d")
        d = d.date()
        if d < date2:
            messages.info(req, "Enter an appropriate date")
            return render(req, "add_runway.html")
        if r_id == "1":
            lock_time = req.POST['lock_time']
            lock_time1 = datetime.strptime(lock_time, '%H:%M').time()
            release_time = req.POST['release_time']
            x1 = runway.objects.filter(status_of_terminal='Busy')
            for i in x1:
                print('lock times are', i.lock_time, " ", lock_time, " ", lock_time1, " ", i.release_time)
                if i.lock_time <= lock_time1 and lock_time1<= i.release_time:
                    messages.info(req, "Time slot already exists")
                    return render(req, 'add_runway.html')
            if flight.objects.filter(f_time=lock_time).exists():
                run = runway(flight_id=y, status_of_terminal=status_of_terminal, date=date1, lock_time=lock_time,
                             release_time=release_time, R_id=r_id)
                run.save()
                messages.info(req, "Registration Successful")
                return render(req, 'airport.html')

            else:
                messages.info(req, "Inconsistent Timing, please view runway 1 table")
                return render(req, 'add_runway.html')
        elif r_id =="2":
            lock_time = req.POST['lock_time']
            lock_time1 = datetime.strptime(lock_time, '%H:%M').time()
            release_time = req.POST['release_time']
            x1 = runway1.objects.filter(status_of_terminal='Busy')
            for i in x1:
                print('lock times are', i.lock_time, " ", lock_time, " ", lock_time1, " ", i.release_time)
                if i.lock_time <= lock_time1 and lock_time1 <= i.release_time:
                    messages.info(req, "Time slot already exists")
                    return render(req, 'add_runway.html')
            if flight.objects.filter(f_time=lock_time).exists():
                run = runway1(flight_id=y, status_of_terminal=status_of_terminal, date=date1, lock_time=lock_time,
                             release_time=release_time, R_id=r_id)
                run.save()
                messages.info(req, "Registration Successful")
                return render(req, 'airport.html')
            else:
                messages.info(req, "Inconsistent Timing, please view runway 2 table")
                return render(req, 'add_runway.html')
        elif r_id == "3":
            lock_time = req.POST['lock_time']
            lock_time1 = datetime.strptime(lock_time, '%H:%M').time()
            release_time = req.POST['release_time']
            x1 = runway2.objects.filter(status_of_terminal='Busy')
            for i in x1:
                print('lock times are', i.lock_time, " ", lock_time, " ", lock_time1, " ", i.release_time)
                if i.lock_time <= lock_time1 and lock_time1 <= i.release_time:
                    messages.info(req, "Time slot already exists")
                    return render(req, 'add_runway.html')
            if flight.objects.filter(f_time=lock_time).exists():
                run = runway2(flight_id=y, status_of_terminal=status_of_terminal, date=date1, lock_time=lock_time,
                             release_time=release_time, R_id=r_id)
                run.save()
                messages.info(req, "Registration Successful")
                return render(req, 'airport.html')
            else:
                messages.info(req, "Inconsistent Timing, please view runway 3 table")
                return render(req, 'add_runway.html')
        elif r_id == "4":
            lock_time = req.POST['lock_time']
            lock_time1 = datetime.strptime(lock_time, '%H:%M').time()
            release_time = req.POST['release_time']
            x1 = runway3.objects.filter(status_of_terminal='Busy')
            for i in x1:
                print('lock times are', i.lock_time, " ", lock_time, " ", lock_time1, " ", i.release_time)
                if i.lock_time <= lock_time1 and lock_time1 <= i.release_time:
                    messages.info(req, "Time slot already exists")
                    return render(req, 'add_runway.html')
            if flight.objects.filter(f_time=lock_time).exists():
                run = runway3(flight_id=y, status_of_terminal=status_of_terminal, date=date1, lock_time=lock_time,
                             release_time=release_time, R_id=r_id)
                run.save()
                messages.info(req, "Registration Successful")
                return render(req, 'airport.html')
            else:
                messages.info(req, "Inconsistent Timing, please view runway 4 table")
                return render(req, 'add_runway.html')
        elif r_id == "5":
            lock_time = req.POST['lock_time']
            lock_time1 = datetime.strptime(lock_time, '%H:%M').time()
            release_time = req.POST['release_time']
            x1 = runway4.objects.filter(status_of_terminal='Busy')
            for i in x1:
                print('lock times are', i.lock_time, " ", lock_time, " ", lock_time1, " ", i.release_time)
                if i.lock_time <= lock_time1 and lock_time1 <= i.release_time:
                    messages.info(req, "Time slot already exists")
                    return render(req, 'add_runway.html')
            if flight.objects.filter(f_time=lock_time).exists():
                run = runway4(flight_id=y, status_of_terminal=status_of_terminal, date=date1, lock_time=lock_time,
                             release_time=release_time, R_id=r_id)
                run.save()
                messages.info(req, "Registration Successful")
                return render(req, 'airport.html')
            else:
                messages.info(req, "Inconsistent Timing, please view runway 5 table")
                return render(req, 'add_runway.html')








def load_add_runway(req):
    return render(req, 'add_runway.html')

def load_shop(req):
    S = store.objects.all()
    return render(req, 'shop.html', {'s': S})
def add_item(req):
    if req.method == "POST":
        s_id = req.POST['s_id']
        s_equipment = req.POST['s_equipment']
        s_price = req.POST['s_price']
        s_quantity = req.POST['s_quantity']
        image = req.FILES['image']
        u = req.user
        print("the current user is", u)
        x = store(S_id=s_id, S_equipment=s_equipment, S_price=s_price, S_quantity=s_quantity, image=image)
        x.save()
        return render(req, 'airport.html')

def load_add_item(req):
    return render(req, 'add_items.html')

def load_passenger(req):
    P = passenger.objects.all()
    return render(req, 'passenger.html', {'p': P})
def load_return(req):
    return render(req, 'airport.html')

