from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'myapp.views.main'),
    url(r'^add/', 'myapp.views.form_add'),
)
