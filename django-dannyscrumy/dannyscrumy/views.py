from django.shortcuts import render
from django.http import HttpResponse
from . models import Task,GoalStatus,Scrumyuser,ScrumyGoal

# Create your views here.
def index(request):
    all_users = Scrumyuser.objects.all()
    all_tasks = Task.objects.all()
    html = ''
    for task in all_tasks:
        url= '/task/' + task.id + '/'
        html += '<a href= "' + url + '">' + task.description + '</a><br>'

    for user in all_users:
        url = '/user/' + str(user.id) + '/'
        html += '<a href= "' + url + '">' + user.fullname +  '</a><br>'

    return HttpResponse(html)
    # return render(request, 'dannyscrumy/post.html')

def move_goal(request,task_id):
    return HttpResponse("<h2>tasks to carry out: " + str(task_id) + "</h2>")


def add_user(request):
    return  HttpResponse("<h3>username :" + str(add_user) + "</h2?")
