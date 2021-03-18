from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', views.UserRegisterViewSet)

urlpatterns = [
    path('signup/', include(router.urls)),
    # path('', views.accountsOverview, name="account-overview"),
    # path('user-list/', views.userList, name="user-list"),
    # path('user-list/<int:pk>/', views.userDetail, name="user-detail"),
    # path('user-create/', views.userCreate, name="user-create"),
    # path('user-update/<int:pk>/', views.userUpdate, name="user-update"),
    # path('user-delete/<int:pk>/', views.userDelete, name="user-delete"),
    # path('userdetail/<int:pk>/', views.userDetail, name="user-Detail"),
    # path('userlist/', views.userDetail, name="user-Detail"),
    # path('user/', views.UserListMixins.as_view()),
    # path('userdetail/<int:pk>/', views.UserDetailMixins.as_view()),
]


# from django.urls import path, include
# from . import views

# urlpatterns = [
#     # FBV
#     path('user/', views.UserListAPIView.as_view()),
#     path('user/<int:pk>/',views.UserDetailAPIView.as_view()),
# ]
