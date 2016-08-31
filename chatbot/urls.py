from django.conf.urls import patterns, include, url
from django.contrib import admin
from fb_chatbot import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'chatbot.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    #url(r'^hello/', include('fb_chatbot.urls')),
    url(r'', include('fb_chatbot.urls')),
    url(r'^new-ticket/$', views.new_ticket),
    url(r'^tickets/$', views.tickets),
)
