from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^admin/', admin.site.urls), 
    url(r'^', include('Step1.urls')),
  #  url(r'^$', RedirectView.as_view(url='/Step1/', permanent=True)),

]
