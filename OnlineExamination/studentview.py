# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render,redirect,render_to_response
from django.contrib.auth.decorators import login_required
from django.db.models import Count,Sum
from django.core.exceptions import ObjectDoesNotExist
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
    subjectlist=[]
    sql=''' select onlinetest_subject.name
    from onlinetest_subject,onlinetest_student_class
    where onlinetest_subject.subjectid=onlinetest_student_class.subjectid_id
    and   onlinetest_student_class.flag=1
    and   onlinetest_subject.flag=1
    and   onlinetest_student_class.studentid_id=
    '''
    sql=sql+'\''+userinfo.username+'\''
    result=functions.runsql(sql)
    for item in result:
        subjectlist.append(item[0])  # direct sql item has no attribute in tables
    ctx['subjectlist']=subjectlist
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

def starttest(request):
    ctx={}
    username=request.COOKIES['userid']
    print(username)
    userinfo=functions.getstudentinfo(username)
    ctx['username']=userinfo.username
    ctx['name']=userinfo.name
    ctx['pwd']=userinfo.pwd
    ctx['mail']=userinfo.mail     



    response=render_to_response('test.html',ctx)
    return response 



def makepapertest(request):
    paperinfo=functions.makepaper("E11414026","E01")
    
    ctx={}
    username=request.COOKIES['userid']
    print(username)
    userinfo=functions.getstudentinfo(username)
    ctx['username']=userinfo.username
    ctx['name']=userinfo.name
    ctx['pwd']=userinfo.pwd
    ctx['mail']=userinfo.mail

    sql='''select onlinetest_questionbank.content,onlinetest_questionbank.choice
    from onlinetest_questionbank,onlinetest_paper_content
    where onlinetest_paper_content.questionid_id=onlinetest_questionbank.questionid
    and   onlinetest_paper_content.paperid_id=
    '''
    sql=sql+str(paperinfo.paperid)
    questionlist=functions.runsql(sql)
    result=list()
    i=1
    for item in questionlist:
        questionelement=dict()
        questionelement['num']=i
        questionelement['content']=item[0]
        if item[1]:
            templist=item[1].split(';')
            choicelist={}
            for x in range(0,4):
                choicelist[str(x)]=templist[x]
            questionelement['choice']=choicelist
        else:
            questionelement['choice']=''
        
        result.append(questionelement)
        i=i+1

    ctx['questionlist']=result
    response=render_to_response('test.html',ctx)
    return response 