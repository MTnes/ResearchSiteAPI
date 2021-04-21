from django.contrib import admin
from django.urls import path, include
from main_app import views
from rest_framework import routers
from django.conf import settings

router = routers.DefaultRouter()
router.register(r'research', views.ResearchViewSet)
router.register(r'member', views.MemberViewSet)
router.register(r'contact', views.ContactViewSet)
router.register(r'publication', views.PublicationViewSet)
router.register(r'people', views.PeopleViewSet)
router.register(r'faculty', views.FacultyViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
