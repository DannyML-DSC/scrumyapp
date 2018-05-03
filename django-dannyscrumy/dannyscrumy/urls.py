from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name ='index'),
    url(r'^(?P<task_id>[0-9]+)/$', views.move_goal, name='move_goal'),
    url(r'^(?P<users_id>[0-9]+)/$', views.add_user, name='add_user'),
];

