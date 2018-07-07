from django.shortcuts import render,redirect,reverse
from .forms import LoginForm,RegisterForm
from .models import User
def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username =  form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                u = User.objects.get(username=username)
                if u.password == password:
                    request.session['username'] = username
                    return redirect("weibo:showuser",id=u.pk)
                else:
                    msg="密码错误"
                    return render(request,'login/login.html',{'form':form,'msg':msg})
            except:
                msg="用户名错误"
                return render(request,'login/login.html',{'form':form,'msg':msg})
    else:
        form = LoginForm()
    return render(request, 'login/login.html', {'form': form, 'msg': ""})


def success(request):
    return render(request,"login/success.html")

def handle_uploaded_file(f,pic_name):
    with open('login/static/login/pic/'+pic_name,'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
def register(request):
    if request.method=="POST":
        form = RegisterForm(request.POST,request.FILES)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            try:
                pic_name = request.FILES['file'].name
                pic_url = "/static/login/pic/"+pic_name
                # pic_url = 'static/pic/'+
                handle_uploaded_file(request.FILES['file'],pic_name)
            except:
                pic_url = ""
            if username=="":
                msg = "注册用户名不能为空"
                return render(request, 'login/register.html', {'form': form,'msg':msg})
            elif password == "":
                msg = "注册密码不能为空"
                return render(request, 'login/register.html', {'form': form, 'msg': msg})
            else:

                u = User(imageurl=pic_url,username=username, password=password)
                u.save()
                return redirect('login:index')
    else:
        form = RegisterForm()

    return render(request,'login/register.html',{'form':form,'msg':''})
def index(request):
    return render(request,"login/index.html")



