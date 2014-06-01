from django.conf.urls import patterns, include, url
from django.contrib import admin
from config import settings
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'login.views.start', name='start'),
    url(r'^login$', 'login.views.login', name='login'),
    url(r'^logout$', 'login.views.logout', name='logout'),
    url(r'^home$', 'login.views.home', name='home'),
    url(r'^edit$', 'login.views.editUser', name='edit'),
    url(r'^delete$', 'login.views.deleteUser', name='delete'),
    url(r'^error$', 'login.views.error', name='error'),
    url(r'^admin/', include(admin.site.urls)),
)
