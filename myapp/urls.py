from django.conf.urls import patterns, include, url

urlpatterns = patterns('myapp.views',
    url(r'^$', 'main'),
    url(r'^add/', 'form_add'),
)
