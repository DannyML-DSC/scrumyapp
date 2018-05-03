from django.db import models
import datetime
from django.utils import timezone


# Create your models here.


class GoalStatus(models.Model):
    status = models.TextField(null=False)
    created_on = models.DateTimeField(null=False)

    class Meta:
        verbose_name_plural = 'GoalStatus'

    def __str__(self):
        return self.status

    def was_created_recently(self):
        return self.created_on >= timezone.now() - datetime.timedelta(days=1)





class Role(models.Model):
    description = models.TextField()


    def __str__(self):
        return self.description



class Scrumyuser(models.Model):

    fullname = models.CharField(max_length=200)
    email = models.EmailField(max_length=20)
    password = models.TextField(null=False)
    Developer = models.CharField(name='Developer', max_length=200,default='Developer')
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    class Meta:

        verbose_name = 'Scrumyuser'
    def __str__(self):
        return self.fullname

    def __email__(self):
        return self.email

    def __password__(self):
        return self.password

    def __Developer__(self):
        return self.Developer
    





class Task(models.Model):

    description = models.TextField()
    created_by = models.ForeignKey(Scrumyuser, on_delete=models.CASCADE)

    class Meta:
        verbose_name ='Task'

    def __str__(self):
        return self.description


class ScrumyGoal(models.Model):
    user_id = models.ForeignKey(Scrumyuser, on_delete=models.CASCADE)
    status_id = models.ForeignKey(GoalStatus, on_delete=models.CASCADE)
    description = models.TextField()

    task_id = models.ForeignKey(Task, on_delete=models.CASCADE)

    created_on = models.DateTimeField()
    updated_on = models.DateTimeField(null=True)



    class Meta:
        verbose_name_plural = 'ScrumyGoal'


    def __str__(self):
        return  self.description

    def is_created_on(self):
        return self.created_on >= timezone.now() - datetime.timedelta(days=1)

    def was_updated_recently(self):
        return self.updated_on >= timezone.now() - datetime.timedelta(days=1)


