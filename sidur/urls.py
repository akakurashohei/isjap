from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.heima, name='heima'),
    path('um_isjap', views.um_isjap, name='um_isjap'),
    path('hafa_samband', views.hafa_samband, name='hafa_samband'),
    path('leit', views.leit, name='leit'),
    ]
