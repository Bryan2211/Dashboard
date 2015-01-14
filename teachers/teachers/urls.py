from django.conf.urls import patterns, include, url
from django.contrib import admin
from teachers import views

#pas compris

urlpatterns = patterns('',


    url(r'^admin/', include(admin.site.urls)),
)
