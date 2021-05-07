from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import*
from  math import  ceil
from .resource import PersonResource
from tablib import Dataset
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout
import csv
from django.utils.encoding import smart_str
from django.contrib import messages
import xlwt

def index(request):
    p = product.objects.all()
    c = Cart.objects.all()
    # print(p)
    ni = len(p)
    ns = ni // 4 + ceil((ni / 4) - (ni // 4))
    n = len(c)
   # print(ni)

    params = {'ns': ns, 'range': range(1,ns), 'xv': p,'n':n}

    return render(request,'shop/index.html',params)


def info(request):
    return render(request, 'shop/info.html')

def track(request):
    return render(request,'shop/index.html')
def Contact(request):
    if request.method=="POST":

        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        Contact=contact(cname=name,email=email,phone=phone,desc=desc)
        Contact.save()
    return render(request,'shop/Contact.html')
def quickview(request,myid):
    p = product.objects.filter(id=myid)
    c = Cart.objects.all()
    n = len(c)
    pa={'xv':p[0],'n':n}

    if request.method=="POST":
       desc = request.POST.get('id', '')

       c=Cart(cartid=myid,cartname=p[0].pname,cartdecs=p[0].decs,cartimage=p[0].image,cartprice=p[0].price)
       c.save()


    return render( request,'shop/quickview.html',pa )

def search(request):
    return render(request,'shop/index.html')
def checkout(request):
    return render(request,'shop/index.html')
def cart(request):
    c = Cart.objects.all()
    n = len(c)
    pa = {'xv': c, 'n': n}

    return render(request,'shop/cart.html',pa)


def adress(request):
    return render(request,'shop/adress.html')

def about(request):
    return render(request,'shop/adress.html')

def payment(request):
    return render(request,'shop/payment.html')

def review(request):
    c = Cart.objects.all()
    n = len(c)
    pa = {'xv': c, 'n': n}
    return render(request,'shop/review.html',pa)


def login(request):
    if request.method == "POST":

        phone = request.POST.get('phone', '')
        password = request.POST.get('password', '')
        log = Login.objects.filter(loginid=phone)
        if len(log)==0:
            messages.info(request,'User not registered')
            return render(request, 'shop/login.html')
        if log[0].password==password:
            return redirect('index')
        else:
            messages.info(request, 'Incorrect password')
            return render(request, 'shop/login.html')

    return render(request, 'shop/login.html')


def createacc(request):

    if request.method == "POST":
        name = request.POST.get('name', '')
        username = request.POST.get('phone', '')
        password = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')

        log = Login.objects.filter(loginid=username)
        if len(log)==1:
            messages.info(request,'User already registered')
            return render(request, 'shop/createacc.html')

        if password!=password2:
            messages.info(request, 'password not match')
            return render(request, 'shop/createacc.html')
        log=Login(loginid=username,loginname=name,password=password)
        log.save()
        messages.success(request, " sucessfully ")
        return redirect('index')
    else:
       return render(request,'shop/createacc.html')



def su(request):
    if request.method == 'POST':
        person_resource = PersonResource()
        dataset = Dataset()
        new_persons = request.FILES['login']

        imported_data = dataset.load(new_persons.read(), format='xls')
        # print(imported_data)
        for data in imported_data:
            print(data)

            value = Login(
                id=int(data[0]),
                loginid=int(data[1]),
                loginname=data[2],
                password=int(data[3]),

            )
            value.save()
        person_resource = PersonResource()
        dataset = Dataset()
        new_persons = request.FILES['product']

        imported_data = dataset.load(new_persons.read(), format='xls')
        # print(imported_data)
        for data in imported_data:
            print(data)

            value = product(

            id=int(data[0]),
            pname = data[1],
            decs = data[2],
            date = data[3],
            ca = data[4],
            sca = data[5],
            price = int(data[6]),
            image = data[7]

            )
            value.save()


    return render(request, 'shop/su.html')
def loginfo(request):
    response = HttpResponse(content_type='login/csv')
    w = csv.writer(response)
    print('updated')
    w.writerow(['id','loginid','loginname','password'])
    for l in Login.objects.all().values_list('id','loginid','loginname','password'):
        w.writerow(l)
        print(l)
    response['Content-Disposition'] = 'attachment;filename="login.csv'
    return response


def productinfo(request):
    response = HttpResponse(content_type='product/csv')
    w = csv.writer(response)
    print('updated')
    w.writerow(['id','pname','decs','date','ca','sca','price','image'])
    for l in product.objects.all().values_list('id','pname','decs','date','ca','sca','price','image'):
        w.writerow(l)
        print(l)
    response['Content-Disposition'] = 'attachment;filename="product.csv'
    return response