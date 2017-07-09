from django.http import HttpResponse
from django.shortcuts import render,redirect,render_to_response
from django.contrib.auth.decorators import login_required
from django.db.models import Count,Sum

from onlinetest import models
from django.http import JsonResponse
import json
from . import functions 


def student_main(request):
    ctx={}
    username=request.COOKIES['userid']
    print(username)
    userinfo=functions.getstudentinfo(username)
    ctx['username']=userinfo.username
    ctx['name']=userinfo.name
    ctx['pwd']=userinfo.pwd
    ctx['mail']=userinfo.mail        
    print(userinfo.name)
    response=render_to_response('student-main.html',ctx)
    return response

def testui(request):
    ctx={}
    username=request.COOKIES['userid']
    print(username)
    userinfo=functions.getstudentinfo(username)
    ctx['username']=userinfo.username
    ctx['name']=userinfo.name
    ctx['pwd']=userinfo.pwd
    ctx['mail']=userinfo.mail        
    response=render_to_response('testui.html',ctx)
    return response

def personalgrade(request):
    ctx={}
    username=request.COOKIES['userid']
    print(username)
    userinfo=functions.getstudentinfo(username)
    ctx['username']=userinfo.username
    ctx['name']=userinfo.name
    ctx['pwd']=userinfo.pwd
    ctx['mail']=userinfo.mail        
    response=render_to_response('personalgrade.html',ctx)
    return response

def studentinfo(request):
    ctx={}
    username=request.COOKIES['userid']
    print(username)
    userinfo=functions.getstudentinfo(username)
    ctx['username']=userinfo.username
    ctx['name']=userinfo.name
    ctx['pwd']=userinfo.pwd
    ctx['mail']=userinfo.mail        
    response=render_to_response('studentinfo.html',ctx)
    return response