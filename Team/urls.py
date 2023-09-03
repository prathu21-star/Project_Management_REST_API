from django.urls import path
from Team.views import TeamBase
from .views import update_team_members

urlpatterns = [
    path('', TeamBase.as_view(), name='get/createTeam'),
    path('<int:pk>/', TeamBase.as_view(), name='getspecificTeam'),
     path('teams/<int:team_id>/update-members/', update_team_members),
]
