from django.conf.urls import url, include

urlpatterns = [
    url(r'', include('{{cookiecutter.app_name}}.urls')),
]
