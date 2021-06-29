from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Register

# Create your views here.

def home(request):
	return HttpResponse("Hi Good Evening to All...")

def htmltag(y):
	return HttpResponse("<h2>Hi Welcome to APSSDC programs</h2>")

def usernameprint(request,uname):
	return HttpResponse("<h2>Hi Welcome <span style='color:blue'>{}</span></h2>".format(uname))

def usernameage(request,un,ag):
	return HttpResponse("<h3>style='text-align:center;background-color:pink;padding:23px'>Hi User <span style='color:blue'>{}</span> and your age is: <span style='color:red'>{}</span></h3>".format(un,ag))

def empdetails(request,eid,ename,eage):
	return HttpResponse("<script>alert('Hi Welcome {}')</script><h3>Hi Welcome {} and your age is: {} and your id is: {}</h3>".format(ename,ename,eage,eid))

def htm(request):
	return render(request,'html/sample.html')

def ytname(request,name):
	return render(request,'html/ytname.html',{'n':name})

def empname(request,id,ename):
	k = {'i':id,'n':ename}
	return render(request,'html/ehtml.html',k)

def studentdetails(request):
	return render(request,'html/std.html')

def internalJS(request):
	return render(request,'html/internalJS.html')

def myform(req):
	if req.method=="POST":
		#print(req.POST)
		uname = req.POST['uname']
		rollno = req.POST['rollno']
		email = req.POST.get('email')
		#print(uname,rollno,email)
		data = {'username':uname,'rno':rollno,'emailID':email}
		return render(req,'html/display.html',data)
	return render(req,'html/myform.html')

def register(request):
	if request.method=="POST":
		fname = request.POST['fname']
		lname = request.POST['lname']
		email = request.POST.get('email')
		phnno = request.POST['phnno']
		gender = request.POST['gender']
		address = request.POST['address']
		Languages = request.POST.getlist('Languages')
		data = {'firstname':fname,'lastname':lname,'email':email,'phnno':phnno,'gender':gender,'address':address,'Languages':Languages}
		return render(request,'html/register1.html',data)
	return render(request,'html/register.html')

def login(req):
	return render(req,'html/login.html')

def btstrpregister(request):
	if request.method=="POST":
		firstname = request.POST['firstname']
		lastname = request.POST['lastname']
		address = request.POST['address']
		email  = request.POST.get('email')
		phnno = request.POST.get('phnno')
		gender = request.POST['gender']
		Languages = request.POST.getlist('Languages')
		d = {'firstname':firstname,'lastname':lastname,'address':address,'email':email,'phnno':phnno,'gender':gender,Languages:'Languages'}
		return render(request,'html/bootregister.html',d)
	return render(request,'html/btstrpregister.html')

def bootstrapfun(request):
	return render(request,'html/sampleboot.html')

def btregi(request):
	return render(request,'html/btregst.html')

def register2(request):
	# name = "siva"
	# email = "siva@gmail.com"
	reg = Register(name = "siva",email="siva@gmail.com")
	reg.save()
	return HttpResponse("row inserted successfully")

def register3(request):
	if request.method == 'POST':
		name = request.POST['name']
		email = request.POST['email']
		reg = Register(name = name,email = email)
		reg.save()
		return HttpResponse("Record inserted successfully")
	return render(request,"html/register3.html")

def display(request):
	data = Register.objects.all()
	return render(request,'html/display1.html',{'data':data})

def sview(request,y):
	w = Register.objects.get(id=y)
	return render(request,'html/sview.html',{'y':w})
	# return HttpResponse("Your Name is: {} and Your Email Id is: {}".format(w.name,w.email))

def supt(request,q):
	t = Register.objects.get(id=q)
	if request.method == "POST":
		na = request.POST['n']
		em = request.POST['e']
		ry = Register()
		t.name = na
		t.email = em
		t.save()
		return redirect('/display')
	return render(request,'html/supdate.html',{'p':t})

def sudl(request,p):
	b = Register.objects.get(id=p)
	if request.method == "POST":
		b.delete()
		return redirect('/display')
	return render(request,'html/sndlt.html',{'z':b})