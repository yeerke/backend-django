from django.urls import path
from . import views

urlpatterns = [
    path('main-page/', views.main_page)
]