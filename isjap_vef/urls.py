from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sidur.urls')),
    path('fletta/', include('fletta.urls')),
    path('leit/', include('leit.urls')),
    path('hafa_samband/', include('hafa_samband.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
