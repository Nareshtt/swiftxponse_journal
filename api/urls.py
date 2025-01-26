from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import (
    PlayerListCreateAPIView,
    ServeListCreateAPIView,
    ServePlacementListCreateAPIView,
    ReceiveListCreateAPIView,
    ReceivePlacementListCreateAPIView,
    RallyListCreateAPIView,
    RallyPlacementListCreateAPIView,
    PrePracticeListCreateAPIView,
    DrillListCreateAPIView,
    StrokeListCreateAPIView,
    PostPracticeListCreateAPIView,
    PlayerProfileListCreateAPIView,
    MatchDetailListCreateAPIView,
    CheckListListCreateAPIView,
    ServeMatchListCreateAPIView,
    ServePlacementMatchListCreateAPIView,
    ReceiveMatchListCreateAPIView,
    ReceivePlacementMatchListCreateAPIView,
    RallyMatchListCreateAPIView,
    RallyPlacementMatchListCreateAPIView,
    OthersMatchListCreateAPIView,
    OtherPlacementMatchListCreateAPIView,
    PreMatchListCreateAPIView,
    SetScoreListCreateAPIView,
    PostMatchListCreateAPIView
)

urlpatterns = [
    path('players/', PlayerListCreateAPIView.as_view(), name='player-list-create'),
    path('serves/', ServeListCreateAPIView.as_view(), name='serve-list-create'),
    path('serve-placements/', ServePlacementListCreateAPIView.as_view(), name='serve-placement-list-create'),
    path('receives/', ReceiveListCreateAPIView.as_view(), name='receive-list-create'),
    path('receive-placements/', ReceivePlacementListCreateAPIView.as_view(), name='receive-placement-list-create'),
    path('rallies/', RallyListCreateAPIView.as_view(), name='rally-list-create'),
    path('rally-placements/', RallyPlacementListCreateAPIView.as_view(), name='rally-placement-list-create'),
    path('pre-practices/', PrePracticeListCreateAPIView.as_view(), name='pre-practice-list-create'),
    path('drills/', DrillListCreateAPIView.as_view(), name='drill-list-create'),
    path('strokes/', StrokeListCreateAPIView.as_view(), name='stroke-list-create'),
    path('post-practices/', PostPracticeListCreateAPIView.as_view(), name='post-practice-list-create'),
    path('player-profiles/', PlayerProfileListCreateAPIView.as_view(), name='player-profile-list-create'),
    path('match-details/', MatchDetailListCreateAPIView.as_view(), name='match-detail-list-create'),
    path('checklists/', CheckListListCreateAPIView.as_view(), name='checklist-list-create'),
    path('serve-matches/', ServeMatchListCreateAPIView.as_view(), name='serve-match-list-create'),
    path('serve-placement-matches/', ServePlacementMatchListCreateAPIView.as_view(), name='serve-placement-match-list-create'),
    path('receive-matches/', ReceiveMatchListCreateAPIView.as_view(), name='receive-match-list-create'),
    path('receive-placement-matches/', ReceivePlacementMatchListCreateAPIView.as_view(), name='receive-placement-match-list-create'),
    path('rally-matches/', RallyMatchListCreateAPIView.as_view(), name='rally-match-list-create'),
    path('rally-placement-matches/', RallyPlacementMatchListCreateAPIView.as_view(), name='rally-placement-match-list-create'),
    path('others-matches/', OthersMatchListCreateAPIView.as_view(), name='others-match-list-create'),
    path('other-placement-matches/', OtherPlacementMatchListCreateAPIView.as_view(), name='other-placement-match-list-create'),
    path('pre-matches/', PreMatchListCreateAPIView.as_view(), name='pre-match-list-create'),
    path('set-scores/', SetScoreListCreateAPIView.as_view(), name='set-score-list-create'),
    path('post-matches/', PostMatchListCreateAPIView.as_view(), name='post-match-list-create'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
