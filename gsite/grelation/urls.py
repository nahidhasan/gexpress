from django.conf.urls import *
from grelation import views


urlpatterns = patterns('',
	url(r'^home/$', views.home, name = 'gr_home'),
)