from django.conf.urls import patterns, include, url

urlpatterns = patterns('myapp.views',
    url(r'^$', 'main'),
    url(r'^1/', 'form_1'),
    url(r'^2/', 'form_2'),
    url(r'^add/', 'form_add'),
)
