from django.http import HttpResponse
from django.shortcuts import render,redirect,render_to_response
from django.contrib.auth.decorators import login_required
from django.db.models import Count,Sum

from onlinetest import models
from django.http import JsonResponse
import json
from . import functions 

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
            useridentity=request.POST['selectid']
        print(useridentity)
        flag,errormsg=functions.searchmatchuser(username,pwd,useridentity)

        if flag:
            if useridentity=="Administrator":
                userinfo=functions.getadmininfo(username)
                # print(userinfo.name,userinfo.mail)
                ctx['username']=userinfo.username
                ctx['name']=userinfo.name
                ctx['pwd']=userinfo.pwd
                ctx['mail']=userinfo.mail
                response=render_to_response('admin-main.html',ctx)
                response.set_cookie("userid",username)
                return response
            elif useridentity=="Student":
                userinfo=functions.getstudentinfo(username)
                # print(userinfo.name,userinfo.mail)
                ctx['username']=userinfo.username
                ctx['name']=userinfo.name
                ctx['pwd']=userinfo.pwd
                ctx['mail']=userinfo.mail
                response=render_to_response('student-main.html',ctx)
                response.set_cookie("userid",username)
                return response
            elif useridentity=="Teacher":
                userinfo=functions.getteacherinfo(username)
                # print(userinfo.name,userinfo.mail)
                ctx['username']=userinfo.username
                ctx['name']=userinfo.name
                ctx['pwd']=userinfo.pwd
                ctx['mail']=userinfo.mail
                response=render_to_response('teacher-main.html',ctx)
                response.set_cookie("userid",username)
                return response
            else:
                ctx['error']=1
                ctx['errormsg']="Unknown Error"
                return render(request,'login.html',ctx)
                
        else:
            ctx['error']=1
            ctx['errormsg']=errormsg
            return render(request,'login.html',ctx)
    else:
        ctx['error']=1
        ctx['errormsg']="Unknown Error"
        return render(request,'login.html',ctx)
    

def logout(request):
    ctx={}
    ctx['success']=1
    response=render_to_response('main.html',ctx)
    response.delete_cookie('userid')
    return response




def aothertableview(request):
    qs = models.Admin.objects.all()  # Use the Pandas Manager
    df = qs
    template = 'infoeditor.html'
    #Format the column headers for the Bootstrap table, they're just a list of field names, 
    #duplicated and turned into dicts like this: {'field': 'foo', 'title: 'foo'}
    columns = [{'field': "username", 'title': "username"},{'field': "name", 'title': "name"},{'field': "pwd", 'title': "pwd"},{'field': "mail", 'title': "mail"}]
    #Write the DataFrame to JSON (as easy as can be)
    json = df # output just the records (no fieldnames) as a collection of tuples
    #Proceed to create your context object containing the columns and the data
    context = {
                'data': json,
                'columns': columns
                }
    #And render it!
    # print(context)
    return render(request, template, context)

def show_table_student(request):

    if request.method == "GET":
        print(request.GET)
        limit = request.GET.get('limit')   # how many items per page
        offset = request.GET.get('offset')  # how many items in total in the DB
        search = request.GET.get('search')
        sort_column = request.GET.get('sort')   # which column need to sort
        order = request.GET.get('order')      # ascending or descending
        if search:    #    
            all_records = models.Admin.objects.filter(usrename=search)
        else:
            all_records = models.Admin.objects.all()   # must be wirte the line code here

        all_records_count=all_records.count()

        if not offset:
            offset = 0
        if not limit:
            limit = 20    
        # pageinator = Paginator(all_records, limit) 

        page = int(int(offset) / int(limit) + 1)    
        response_data = {'total':all_records_count,'rows':[]}   

        # response_data['rows']=all_records
        for asset in all_records:    
            # ram_disk = get_ram_sum_size(asset.id)    
            response_data['rows'].append({
                "username": asset.username,   
                "name" : asset.name,
                "pwd":asset.pwd,
                "mail":asset.mail,
                # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            })
        # total=all_records_count
        # rows = all_records.Skip(offset).Take(limit).ToList();
        # return Json(new { total = total, rows = rows }, JsonRequestBehavior.AllowGet);
        return JsonResponse(response_data)
        # return  HttpResponse(json.dumps(response_data))    # json



def show_table_teacher(request):
    
    if request.method == "GET":
        print(request.GET)
        limit = request.GET.get('limit')   # how many items per page
        offset = request.GET.get('offset')  # how many items in total in the DB
        search = request.GET.get('search')
        sort_column = request.GET.get('sort')   # which column need to sort
        order = request.GET.get('order')      # ascending or descending
        if search:    #    
            all_records = models.Teacher.objects.filter(usrename=search)
        else:
            all_records = models.Teacher.objects.all()   # must be wirte the line code here

        all_records_count=all_records.count()

        if not offset:
            offset = 0
        if not limit:
            limit = 20    

        page = int(int(offset) / int(limit) + 1)    
        response_data = {'total':all_records_count,'rows':[]}   
        for asset in all_records:    
            response_data['rows'].append({
                "username": asset.username,   
                "name" : asset.name,
                "pwd":asset.pwd,
                "mail":asset.mail,
            })

        return JsonResponse(response_data)

def show_table_grade(request):
    
    if request.method == "GET":
        print(request.GET)
        limit = request.GET.get('limit')   # how many items per page
        offset = request.GET.get('offset')  # how many items in total in the DB
        search = request.GET.get('search')
        sort_column = request.GET.get('sort')   # which column need to sort
        order = request.GET.get('order')      # ascending or descending
        # paperinfo=models.PaperInfo.objects.filter(studentid_id=search)

        # papers = models.Paper_Content.objects.filter(paperid=search)


        # all_records = models.Teacher.objects.all() 

        # all_records_count=all_records.count()

        # if not offset:
        #     offset = 0
        # if not limit:
        #     limit = 20    
            
        # page = int(int(offset) / int(limit) + 1)    
        # response_data = {'total':all_records_count,'rows':[]}   
        # for asset in all_records:    
        #     response_data['rows'].append({
        #         "username": asset.username,   
        #         "name" : asset.name,
        #         "paperid":asset.paperid,
        #         "grade":asset.grade,
        #     })
        all_records_count=1
        response_data = {'total':all_records_count,'rows':[]} 
        response_data['rows'].append({ "username": "tenmp","name" : "tenmp","paperid":"tenmp","grade":"tenmp"})
        return JsonResponse(response_data)



def asset_show_table_questionbank(request):
    if request.method == "GET":
        print(request.GET)
        limit = request.GET.get('limit')   # how many items per page
        offset = request.GET.get('offset')  # how many items in total in the DB
        search = request.GET.get('search')
        sort_column = request.GET.get('sort')   # which column need to sort
        order = request.GET.get('order')      # ascending or descending

        all_records = models.QuestionBank.objects.all()   # must be wirte the line code here

        all_records_count=all_records.count()

        if not offset:
            offset = 0
        if not limit:
            limit = 20    

        page = int(int(offset) / int(limit) + 1)    
        response_data = {'total':all_records_count,'rows':[]}   
        for asset in all_records:    
            response_data['rows'].append({
                "questionid": asset.questionid,   
                "content" : asset.content,
                "choice":asset.choice,
                "answer":asset.answer,
                "score":asset.score,
                "subjectid_id":asset.subjectid_id,
            })
        return JsonResponse(response_data)

