from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'', include('{{cookiecutter.app_name}}.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
