import os
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token

urlpatterns = [
    url(os.environ.get('DJANGO_URL_PREFIX', ''), include([
        url(r'', include('{{cookiecutter.app_name}}.urls')),
        url(r'^admin/', admin.site.urls),
        url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
        url(r'^api-token-auth/', obtain_jwt_token),
        url(r'^api-token-verify/', verify_jwt_token),
    ])),
]
