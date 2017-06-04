from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^create/$', 'products.views.create_view', name='create_view'),
    url(r'^detail/(?P<object_id>\d+)/$', 'products.views.detail_view', name='detail_view'),
    url(r'^detail/(?P<slug>[\w-]+)/$', 'products.views.detail_slug_view', name='detail_slug_view'),
    url(r'^list/$', 'products.views.list_view', name='list_view'),
]
