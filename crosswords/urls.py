from django.conf.urls import patterns, include, url
from django.contrib import admin
import main.views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'crosswords.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^index', main.views.index, name='index'),
)
