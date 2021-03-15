from django.urls import path
from . import views

urlpatterns = [
    path('', views.accountsOverview, name="account-overview"),
    path('user-list/', views.userList, name="user-list"),
    # path('user-list/<int:pk>/', views.userDetail, name="user-detail"),
    path('user-create/', views.userCreate, name="user-create"),
    # path('user-update/<int:pk>/', views.userUpdate, name="user-update"),
    # path('user-delete/<int:pk>/', views.userDelete, name="user-delete"),
    path('userdetail/<int:pk>/', views.userDetail, name="user-Detail")
]


# from django.urls import path, include
# from . import views

# urlpatterns = [
#     # FBV
#     path('user/', views.UserListAPIView.as_view()),
#     path('user/<int:pk>/',views.UserDetailAPIView.as_view()),
# ]
