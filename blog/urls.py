from . import views
from django.urls import path

urlpatterns = [
    path('home/', views.PostList.as_view(), name='home'),
]