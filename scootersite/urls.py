from django.conf.urls import patterns, include, url
from django.contrib import admin
from scootersite.views import home_page

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'scootersite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home_page, name='home'),
)


