from django.urls import path
from ProjectBoard.views import ProjectBoardBase
from . import views

urlpatterns = [
    path('', ProjectBoardBase.as_view(), name='get/createteam'),
    path('<int:pk>/', ProjectBoardBase.as_view(), name='getspecificteam'),
    path('export_board/', views.export_board, name='export_board'),
]
