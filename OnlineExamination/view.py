from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def main(request):
    # context = {}
    # context['hello'] = 'Hello World!'
    return render(request, 'main.html')

def loginpage(request):
    ctx ={}
    if request.method=='GET':
        ctx['error']=0
        return render(request,'login.html',ctx)
    if request.method=='POST' and 'login' in request.POST:
        
        if request.POST:
            username= request.POST['inputUsername']
            pwd=request.POST['inputPassword']
            userid=request.POST['selectid']
        if username=='111' and pwd=='111' and userid=='Administrator':
            ctx['username']=username
            return render(request,'admin-main.html', ctx)
        else:
            ctx['error']=1
            return render(request,'login.html',ctx)   
    

def admin_main(request):
    return render(request,'admin-main.html')

# @login_required(login_url="/login/") 
# def verify(request):
#     ctx ={}
#     if request.POST:
#         username= request.POST['inputUsername']
#         pwd=request.POST['inputPassword']
#         userid=request.POST['selectid']
#     if username=='111' and pwd=='111' and userid=='Administrator':
#         ctx['username']=username
#         return render(request,'admin-main.html', ctx)
#     else:
#         return render(request,'login.html')                    
