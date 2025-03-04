from django.urls import path,include
from .views import (
    PrePracticeListCreateView,
    DrillListCreateView,
    PostPracticeListCreateView,
    PreMatchListCreateView,
    PostMatchListCreateView,
    SkillListCreateView,
    MatchListCreateView,
    GameListCreateView,
    PlayerProfileListCreateView,  # Player profile related endpoints
    CreateUserView,
    StrokeListCreateView
)
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView


urlpatterns = [
   #user profile
    path("user/register",CreateUserView.as_view(),name="register"),
    path("token/",TokenObtainPairView.as_view(),name="get_token"),
    path("refresh/",TokenRefreshView.as_view(),name="refresh"),
    path("auth/",include("rest_framework.urls")),
    # Practice-related endpoints
    path("pre-practice/", PrePracticeListCreateView.as_view(), name="pre-practice-list-create"),
    path("post-practice/", PostPracticeListCreateView.as_view(), name="post-practice-list-create"),

    # Match-related endpoints
    path("pre-match/", PreMatchListCreateView.as_view(), name="pre-match-list-create"),
    path("post-match/", PostMatchListCreateView.as_view(), name="post-match-list-create"),
    path("matches/", MatchListCreateView.as_view(), name="match-list-create"),
    path("games/", GameListCreateView.as_view(), name="game-list-create"),

    # Skills and Drills
    path("drills/", DrillListCreateView.as_view(), name="drill-list-create"),
    path("skills/", SkillListCreateView.as_view(), name="skill-list-create"),
    path("strokes/",StrokeListCreateView.as_view(), name="stroke-list-create"),

    #Player Profile
    path("player/", PlayerProfileListCreateView.as_view(), name="player-profile-create"),
]

