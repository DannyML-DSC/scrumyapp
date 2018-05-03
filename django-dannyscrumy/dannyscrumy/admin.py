from django.contrib import admin

# Register your models here.
from .models import Task, Role, ScrumyGoal, Scrumyuser, GoalStatus


admin.site.register(Task)
admin.site.register(Role)
admin.site.register(Scrumyuser)
admin.site.register(ScrumyGoal)
admin.site.register(GoalStatus)

