from django.conf.urls import url, include
from rest_framework import routers
from base import views
from django.contrib import admin

router = routers.DefaultRouter()
router.register(r'courses', views.CourseViewSet)
router.register(r'assessments', views.AssessmentViewSet)
router.register(r'iterations', views.IterationViewSet)
router.register(r'results', views.ResultViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
