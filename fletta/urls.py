from django.urls import path
from . import views

app_name = 'fletta'

urlpatterns = [
    path('<int:pk>/', views.FlettaDetailView.as_view(), name='fletta'),
]
