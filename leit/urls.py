from django.urls import path
from . import views

app_name = 'leit'

urlpatterns = [
    path('', views.SearchResultView.as_view(), name='nidurstada'),
]
