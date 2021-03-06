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
    url(r'^customers/$', views.all_customers),
    url(r'^new-customer/$', views.new_customer),
    url(r'^tickets/(?P<fbid>[_.%&+0-9a-zA-Z ]+)/$', views.find_tickets),
)
