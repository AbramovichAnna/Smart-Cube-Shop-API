from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include("smartcube_api.urls")),
    path('token/',TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/',TokenObtainPairView.as_view(), name='token_refresh'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

