from django.conf.urls import url

from . import views


urlpatterns = [
  url(r'Step1/$', views.get_login, name='get_login'),
  url(r'general_page/[0-9]+/$', views.send_message, name ='send_message'),
  url(r'general_page/Create_room/', views.CreateRoom, name = 'CreateRoom'),
  url(r'messages/', views.Messages, name = "m"),
  url(r'^logout/$',views.logout, name = "logout"),

]