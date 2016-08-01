from django.conf.urls import url
urlpatterns = [
    url(r'^login/', 'loginsys.views.login'),
    url(r'^logout/', 'loginsys.views.logout'),
    url(r'^register/', 'loginsys.views.register'),
    url(r'^lk/', 'loginsys.views.lk'),
    url(r'^', 'loginsys.views.lk'),
]