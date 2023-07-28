from django.urls import path
from e_commerce_store.accounts.views import *

urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', LogoutUser.as_view(), name='logout'),
    path('profile/details/<int:pk>/', DetailsProfile.as_view(), name='profile'),
    path('profile/edit/<int:pk>/', EditUser.as_view(), name='profile-edit'),
    path('profile/delete/<int:pk>/', DeleteUser.as_view(), name='profile-delete'),
]
