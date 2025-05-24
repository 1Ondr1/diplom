from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.services, name='services'),
    path('new_listing/', views.create_ad, name='new_listing'),
    path('advertisement/<int:ad_id>/', views.ad_detail, name='ad_detail'),
    path('advertisement/<int:ad_id>/edit/', views.edit_ad, name='edit_ad'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)