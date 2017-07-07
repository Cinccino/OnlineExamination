from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Count,Sum
import json
from onlinetest import models


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


def get_ram_sum_size(asset_id):
    '''
    get the size of RAM and disk in total
    :param asset_id:  asset's id
    :return:   the size of RAM in total
    '''
    all_ram_slot = models.RAM.objects.filter(asset__id=asset_id)
    all_disk_slot = models.Disk.objects.filter(asset__id=asset_id)
    ram=0
    for slot in all_ram_slot:
        ram=ram+slot.capacity

    disk = 0
    for slot in all_disk_slot:
        disk = disk+slot.capacity
    return ram,disk


def show_asset_in_table(request):
    '''
    专门处理在服务器资产列表里面的表格信息的方法
    :param request: 
    :return: 
    '''
    if request.method == "GET":
        print(request.GET)
        limit = request.GET.get('limit')   # how many items per page
        offset = request.GET.get('offset')  # how many items in total in the DB
        search = request.GET.get('search')
        sort_column = request.GET.get('sort')   # which column need to sort
        order = request.GET.get('order')      # ascending or descending
        if search:    #    判断是否有搜索字
            all_records = models.Asset.objects.filter(id=search,asset_type=search,business_unit=search,idc=search)
        else:
            all_records = models.Asset.objects.all()   # must be wirte the line code here

        if sort_column:   # 判断是否有排序需求
            sort_column = sort_column.replace('asset_', '')    
            if sort_column in ['id','asset_type','sn','name','management_ip','manufactory','type']:   # 如果排序的列表在这些内容里面
                if order == 'desc':   # 如果排序是反向
                    sort_column = '-%s' % (sort_column)
                all_records = models.Asset.objects.all().order_by(sort_column)
            elif sort_column in ['salt_minion_id','os_release',]:
                # server__ 表示asset下的外键关联的表server下面的os_release或者其他的字段进行排序
                sort_column = "server__%s" % (sort_column)
                if order == 'desc':
                    sort_column = '-%s'%(sort_column)
                all_records = models.Asset.objects.all().order_by(sort_column)
            elif sort_column in ['cpu_model','cpu_count','cpu_core_count']:
                sort_column = "cpu__%s" %(sort_column)
                if order == 'desc':
                    sort_column = '-%s'%(sort_column)
                all_records = models.Asset.objects.all().order_by(sort_column)
            elif sort_column in ['rams_size',]:
                if order == 'desc':
                    sort_column = '-rams_size'
                else:
                    sort_column = 'rams_size'
                all_records = models.Asset.objects.all().annotate(rams_size = Sum('ram__capacity')).order_by(sort_column)
            elif sort_column in ['localdisks_size',]:  # using variable of localdisks_size because there have a annotation below of this line
                if order == "desc":
                    sort_column = '-localdisks_size'
                else:
                    sort_column = 'localdisks_size'
                #     annotate 是注释的功能,localdisks_size前端传过来的是这个值，后端也必须这样写，Sum方法是django里面的，不是小写的sum方法，
                # 两者的区别需要注意，Sum（'disk__capacity‘）表示对disk表下面的capacity进行加法计算，返回一个总值.
                all_records = models.Asset.objects.all().annotate(localdisks_size=Sum('disk__capacity')).order_by(sort_column)   

            elif sort_column in ['idc',]:
                sort_column = "idc__%s" % (sort_column)
                if order == 'desc':
                    sort_column = '-%s'%(sort_column)
                all_records = models.Asset.objects.all().order_by(sort_column)

            elif sort_column in ['trade_date','create_date']:
                if order == 'desc':
                    sort_column = '-%s'%sort_column
                all_records = models.Asset.objects.all().order_by(sort_column)


        all_records_count=all_records.count()

        if not offset:
            offset = 0
        if not limit:
            limit = 20    # 默认是每页20行的内容，与前端默认行数一致
        pageinator = Paginator(all_records, limit)   # 开始做分页

        page = int(int(offset) / int(limit) + 1)    
        response_data = {'total':all_records_count,'rows':[]}   # 必须带有rows和total这2个key，total表示总页数，rows表示每行的内容


        for asset in pageinator.page(page):    
            ram_disk = get_ram_sum_size(asset.id)    # 获取磁盘和内存的大小
            # 下面这些asset_开头的key，都是我们在前端定义好了的，前后端必须一致，前端才能接受到数据并且请求.
            response_data['rows'].append({
                "asset_id": '<a href="/asset/asset_list/%d" target="_blank">%d</a>' %(asset.id,asset.id),   
                "asset_sn" : asset.sn if asset.sn else "",
                # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            })
            
        return  HttpResponse(json.dumps(response_data))    # 需要json处理下数据格式   