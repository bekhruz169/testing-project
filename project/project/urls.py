from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from testing_app.views import StudentViewSet, TestViewSet, TestResultViewSet

router = DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'tests', TestViewSet)
router.register(r'results', TestResultViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
