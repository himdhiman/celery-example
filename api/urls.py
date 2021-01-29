from django.urls import path
from api import views

urlpatterns = [
    path('<int:id>/', views.index)
]