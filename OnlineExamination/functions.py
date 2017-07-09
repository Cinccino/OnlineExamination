from django.db.models import Count, Sum
from onlinetest import models


def searchmatchuser(username,pwd,useridentity):
    errormsg=""
    if useridentity=="admin" or useridentity=="Admin" or useridentity=="Administrator":
        if models.Admin.objects.filter(username=username).exists():
            userset=models.Admin.objects.get(username=username)
            if userset.pwd==pwd:
                return True,errormsg
            else:
                errormsg="Password wrong!"
                return False,errormsg
        else:
            errormsg="No such user!"
            return False,errormsg

    elif useridentity=="Student" or useridentity=="student":
        if models.Studnet.objects.filter(username=username).exists():
            userset=models.Studnet.objects.get(username=username)
            if userset.pwd==pwd:
                return True,errormsg
            else:
                errormsg="Password wrong!"
                return False,errormsg
        else:
            errormsg="No such user!"
            return False,errormsg

    elif useridentity=="Teacher" or useridentity=="teacher":
        if models.Teacher.objects.filter(username=username).exists():
            userset=models.Teacher.objects.get(username=username)
            if userset.pwd==pwd:
                return True,errormsg
            else:
                errormsg="Password wrong!"
                return False,errormsg
        else:
            errormsg="No such user!"
            return False,errormsg

    else:
        errormsg="Unknown Error"
        return False,errormsg

def getadmininfo(username):
    userset=models.Admin.objects.get(username=username)
    return userset

def getstudentinfo(username):
    userset=models.Studnet.objects.get(username=username)
    return userset

def getteacherinfo(username):
    userset=models.Teacher.objects.get(username=username)
    return userset

def calpapergrade(paperid):
    scores=0
    papercontent=models.Paper_Content.objects.filter(paperid_id=paperid)
    for item in papercontent:
        scores=scores+item.score
    return scores