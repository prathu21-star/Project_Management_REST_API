from django.urls import path
from User.views import UserBase

urlpatterns = [
    path('', UserBase.as_view(), name='get/createuser'),
    path('<int:pk>/', UserBase.as_view(), name='getspecificuser'),
]
