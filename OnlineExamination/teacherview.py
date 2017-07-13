from django.http import HttpResponse
from django.shortcuts import render,redirect,render_to_response
from django.contrib.auth.decorators import login_required
from django.db.models import Count,Sum

from onlinetest import models
from django.http import JsonResponse
import json
from . import functions 



def teacher_main(request):
    ctx={}
    username=request.COOKIES['userid']
    print(username)
    userinfo=functions.getteacherinfo(username)
    ctx['username']=userinfo.username
    ctx['name']=userinfo.name
    ctx['pwd']=userinfo.pwd
    ctx['mail']=userinfo.mail        
    response=render_to_response('teacher-main.html',ctx)
    return response


def tgradetable(request):
    ctx={}
    username=request.COOKIES['userid']
    print(username)
    userinfo=functions.getteacherinfo(username)
    ctx['username']=userinfo.username
    ctx['name']=userinfo.name
    ctx['pwd']=userinfo.pwd
    ctx['mail']=userinfo.mail        
    response=render_to_response('tgradetable.html',ctx)
    return response


def teachersubjects(request):
    ctx={}
    username=request.COOKIES['userid']
    print(username)
    userinfo=functions.getteacherinfo(username)
    ctx['username']=userinfo.username
    ctx['name']=userinfo.name
    ctx['pwd']=userinfo.pwd
    ctx['mail']=userinfo.mail        
    response=render_to_response('teachersubjects.html',ctx)
    return response


def judgepaper(request):
    
    ctx={}
    username=request.COOKIES['userid']
    print(username)
    userinfo=functions.getteacherinfo(username)
    ctx['username']=userinfo.username
    ctx['name']=userinfo.name
    ctx['pwd']=userinfo.pwd
    ctx['mail']=userinfo.mail
    
    
    result=list()
    questionelement=dict()
    questionelement['num']=1
    questionelement['questionid']="this is id"
    questionelement['content']="this is a ui preview"
    questionelement['answer']='example'
    result.append(questionelement)
    ctx['questionlist']=result


    response=render_to_response('judgepaper.html',ctx)
    return response

def teacherinfo(request):
    ctx={}
    username=request.COOKIES['userid']
    print(username)
    userinfo=functions.getteacherinfo(username)
    ctx['username']=userinfo.username
    ctx['name']=userinfo.name
    ctx['pwd']=userinfo.pwd
    ctx['mail']=userinfo.mail        
    response=render_to_response('teacherinfo.html',ctx)
    return response