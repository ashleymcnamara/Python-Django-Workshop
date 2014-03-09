from django.conf.urls import patterns, include, url

from django.contrib import admin
from polls import views

admin.autodiscover()

urlpatterns = patterns('',
    #The idea behind include() is to make 
    # it easy to plug-and-play URLs
    url(r'^$', views.index, name='index'),
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

