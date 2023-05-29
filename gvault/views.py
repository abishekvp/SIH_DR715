from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User,auth
from gvault.models import regextend,projects,lst
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login,logout
import os,json
from datetime import datetime,date
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.cache import cache_control
# Create your views here.
def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData

def rreg(request):
    if request.method == "POST":
        name = request.POST['name']
        acc_type = "researcher"
        desc = "Welcome this is the place where you can tell about yourself to the world out there. Feel free to connect with the world"
        avatar = convertToBinaryData(os.path.join(settings.BASE_DIR,"static","images","default_profile.jpg"))
        email = request.POST['email']
        university = request.POST['unv']
        uname = request.POST['username']
        password = request.POST['pass']
        user = User.objects.create_user(username = uname,password = password,first_name = name,email = email)
        user.save()
        userinfo = regextend.objects.create(acc_type = acc_type,orgname = university,description = desc,profile_pic = avatar,username = uname)
        userinfo.save()
        return HttpResponse("done")
    else:
        return render(request,"./register.html")

def fetchdata(uname):
    res = regextend.objects.get(username=uname)
    desc = res.description
    file = open('static\images\profile_pics\profile.jpg', 'wb')
    file.write(res.profile_pic)
    return desc,res.acc_type
def loginuser(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        password = request.POST['password']
        user = authenticate(request, username = uname, password = password)
        if user is not None:
            form = login(request,user)
            return redirect('profile')
        else:
            return render(request,"./login.html",{'status':'Bad Cred if you are the new user Register First'})
    else:
        return render(request,"./login.html")

@login_required(login_url='login')
def profile(request):
    if request.method == "POST":
        title = request.POST['title']
        file = request.FILES.get('files')
        l = "static\images\profile_pics\\"+file.name
        handle_uploaded_file(file,l)
        file = convertToBinaryData(l)
        os.remove(l)
        keywords = request.POST['keywords'].split(",")
        desc = request.POST['des']
        user = projects.objects.create(project_title = title,username = request.user.username,paper_details = file,description = desc,keywords = {"keywords":keywords})
        user.save()
    desc,type = fetchdata(request.user.username)
    return render(request,"./profile.html",{'name':request.user.first_name,'desc':desc,'type':type})
@login_required(login_url='login')
def logoutuser(request):
    logout(request)
    return redirect("/")
@cache_control(must_revalidate=True)
@login_required(login_url='login')
def repository(request):
    res = []
    for project in projects.objects.all().filter(username = request.user.username):
        val = {"id":project.id,"name":project.project_title,"desc":project.description}
        res.append(val)
    desc = regextend.objects.get(username = request.user.username)
    return render(request,"./repository.html",{'type':desc.acc_type,'name':request.user.first_name,'desc':desc.description,'val':res})
def handle_uploaded_file(f,link):  
    with open(link, 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk)  
def createjson(username,list):
    dictionary = {username:list}
    json_object = json.dumps(dictionary, indent=4)
    with open("areaofInterest.json", "w") as outfile:
        outfile.write(json_object)
@login_required(login_url='login')

def edit(request):
    changedprofilepic = True
    if request.method == "POST":
        name = request.POST['name'].strip()
        unv = request.POST['unv'].strip()
        description = request.POST['desc'].strip()
        keywords = request.POST['areaofInterests'].replace(" ","").split(",")
        createjson(request.user.username,keywords)
        try:
            handle_uploaded_file(request.FILES['file'],"static\images\profile_pics\profile.jpg") 
        except:
            changedprofilepic = False
        if name != '':
            user = User.objects.get(username = request.user.username)
            user.first_name = name
            user.save()
        change = regextend.objects.get(username = request.user.username)
        if unv != '':
            change.orgname = unv  
        if description != '':
            change.description = description
        if changedprofilepic == True:
            change.profile_pic = convertToBinaryData("static\images\profile_pics\profile.jpg")
        change.save()
        return redirect('profile')
    else:
        return render(request,"./edit.html")

def investor(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        org = request.POST['org']
        username = request.POST['uname']
        password = request.POST['password']
        user = User.objects.create_user(username = username,password = password,first_name = name,email = email)
        user.save()
        acc_type = "investor"
        avatar = convertToBinaryData(os.path.join(settings.BASE_DIR,"static","images","default_profile.jpg"))
        desc = "Welcome this is the place where you can tell about yourself to the world out there. Feel free to connect with the world"
        userinfo = regextend.objects.create(acc_type = acc_type,orgname = org,description = desc,profile_pic = avatar,username = username)
        userinfo.save()
        return redirect("login")
    else:
        return render(request,"./invester.html")

def index(request):
    a = []
    page = request.GET.get('page', 1)
    dta = request.GET.get('keywords')
    if dta != None:
        dta = dta.split()
        for keyword in dta:
            for i in lst.objects.filter(name__iregex=keyword):
                s = "color:white;"
                try:
                    b = datetime.strptime(i.To_Date, '%d/%m/%Y').date()
                    if (b - date.today()).days <= 7 and (b - date.today()).days > 0:
                        s = "color:red;"
                    else:
                        s = "color:white;"
                except:
                    pass
                a.append({"invest":i.investment,"name":i.name,"From_Date":i.From_Date,"To_Date":i.To_Date,"lst":i.doc_list,"style":s})
    else:
        for i in lst.objects.all():
            s = "color:white;"
            try:
                b = datetime.strptime(i.To_Date, '%d/%m/%Y').date()
                if (b - date.today()).days <= 7 and (b - date.today()).days > 0:
                    s = "color:red;"
                else:
                    s = "color:white;"
            except:
                pass
            a.append({"invest":i.investment,"name":i.name,"From_Date":i.From_Date,"To_Date":i.To_Date,"lst":i.doc_list,"style":s})
    paginator = Paginator(a, 5)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    return render(request,"home.html",{'data': users})
def abstract(request):
    dta = request.GET.get('id')
    val = projects.objects.get(id = dta).paper_details
    with open("test.txt", 'wb') as f:
        f.write(val)
    f = open("test.txt","r")
    data = f.read()
    f.close()
    os.remove("test.txt")
    desc = regextend.objects.get(username = request.user.username)
    return render(request,"abstract.html",{'name':request.user.first_name,'desc':desc.description,'val':data,'id':dta})
def delete(request):
    dta = request.GET.get('id')
    a = projects.objects.get(id=dta)
    a.delete()
    return redirect("repository")
def abtus(request):
    return render(request,"aboutus.html")
def contact(request):
    return render(request,"contact.html")
def tnc(request):
    return render(request,"tnc.html")

