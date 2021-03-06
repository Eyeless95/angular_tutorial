from django.conf.urls import include, url
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'account', views.AccountViewSet)


app_name = 'core'
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^accounts/$', views.accounts_list),
    url(r'^accounts/(?P<pk>[0-9]+)$', views.account_detail),
]
