from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls import include

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('snippets.urls')),
]

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]
