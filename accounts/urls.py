from django.urls import path
from . import views

urlpatterns = [
    path('', views.accountsOverview, name="account-overview"),
    path('user-list/', views.userList, name="user-list"),
    path('user-list/<int:pk>/', views.userDetail, name="user-detail"),
    path('user-create/', views.userCreate, name="user-create"),
]
