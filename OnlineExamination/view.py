from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Count,Sum
import json
from onlinetest import models
from django.http import JsonResponse


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


# def get_ram_sum_size(asset_id):
#     '''
#     get the size of RAM and disk in total
#     :param asset_id:  asset's id
#     :return:   the size of RAM in total
#     '''
#     all_ram_slot = models.RAM.objects.filter(asset__id=asset_id)
#     all_disk_slot = models.Disk.objects.filter(asset__id=asset_id)
#     ram=0
#     for slot in all_ram_slot:
#         ram=ram+slot.capacity

#     disk = 0
#     for slot in all_disk_slot:
#         disk = disk+slot.capacity
#     return ram,disk

def table(request):
    return render(request,'infoeditor.html')

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

def show_asset_in_table(request):

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


    