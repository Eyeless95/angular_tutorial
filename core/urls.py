from django.conf.urls import include, url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


app_name = 'core'
urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^accounts/$', views.AccountList.as_view()),
    url(r'^accounts/(?P<pk>[0-9]+)/$', views.AccountDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
