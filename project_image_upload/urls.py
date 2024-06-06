from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
  TokenObtainPairView,
  TokenRefreshView,
)
from app_image_upload.views import *
from django.conf import settings
from rest_framework import routers
from app_image_upload.views import *

router = routers.DefaultRouter()

router.register(r'images', ImageViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create-image/', create_image),
    path('get-images/', get_images),
    path('profile/', get_profile),
    path('create-user/', create_user),
    path('refresh/', TokenRefreshView.as_view()),
    path('token/', TokenObtainPairView.as_view()),
    path('get-images/<int:pk>/delete/', delete_post, name='delete_post'),
    path('user/post/<int:pk>/', user_posts),
    path('', include(router.urls))
]


if settings.DEBUG:
  from django.conf.urls.static import static
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

