from rest_framework.generics import ListCreateAPIView
from .models import (
    Player, Serve, ServePlacement, Receive, ReceivePlacement, Rally, RallyPlacement,
    PrePractice, Drill, Stroke, PostPractice, PlayerProfile, MatchDetail, CheckList,
    ServeMatch, ServePlacementMatch, ReceiveMatch, ReceivePlacementMatch, RallyMatch,
    RallyPlacementMatch, OthersMatch, OtherPlacementMatch, PreMatch, SetScore, PostMatch
)
from .serializers import (
    PlayerSerializer, ServeSerializer, ServePlacementSerializer, ReceiveSerializer,
    ReceivePlacementSerializer, RallySerializer, RallyPlacementSerializer, PrePracticeSerializer,
    DrillSerializer, StrokeSerializer, PostPracticeSerializer, PlayerProfileSerializer, MatchDetailSerializer,
    CheckListSerializer, ServeMatchSerializer, ServePlacementMatchSerializer, ReceiveMatchSerializer,
    ReceivePlacementMatchSerializer, RallyMatchSerializer, RallyPlacementMatchSerializer,
    OthersMatchSerializer, OtherPlacementMatchSerializer, PreMatchSerializer, SetScoreSerializer,
    PostMatchSerializer
)


class PlayerListCreateAPIView(ListCreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class ServeListCreateAPIView(ListCreateAPIView):
    queryset = Serve.objects.all()
    serializer_class = ServeSerializer


class ServePlacementListCreateAPIView(ListCreateAPIView):
    queryset = ServePlacement.objects.all()
    serializer_class = ServePlacementSerializer


class ReceiveListCreateAPIView(ListCreateAPIView):
    queryset = Receive.objects.all()
    serializer_class = ReceiveSerializer


class ReceivePlacementListCreateAPIView(ListCreateAPIView):
    queryset = ReceivePlacement.objects.all()
    serializer_class = ReceivePlacementSerializer


class RallyListCreateAPIView(ListCreateAPIView):
    queryset = Rally.objects.all()
    serializer_class = RallySerializer


class RallyPlacementListCreateAPIView(ListCreateAPIView):
    queryset = RallyPlacement.objects.all()
    serializer_class = RallyPlacementSerializer


class PrePracticeListCreateAPIView(ListCreateAPIView):
    queryset = PrePractice.objects.all()
    serializer_class = PrePracticeSerializer


class DrillListCreateAPIView(ListCreateAPIView):
    queryset = Drill.objects.all()
    serializer_class = DrillSerializer


class StrokeListCreateAPIView(ListCreateAPIView):
    queryset = Stroke.objects.all()
    serializer_class = StrokeSerializer


class PostPracticeListCreateAPIView(ListCreateAPIView):
    queryset = PostPractice.objects.all()
    serializer_class = PostPracticeSerializer


class PlayerProfileListCreateAPIView(ListCreateAPIView):
    queryset = PlayerProfile.objects.all()
    serializer_class = PlayerProfileSerializer


class MatchDetailListCreateAPIView(ListCreateAPIView):
    queryset = MatchDetail.objects.all()
    serializer_class = MatchDetailSerializer


class CheckListListCreateAPIView(ListCreateAPIView):
    queryset = CheckList.objects.all()
    serializer_class = CheckListSerializer


class ServeMatchListCreateAPIView(ListCreateAPIView):
    queryset = ServeMatch.objects.all()
    serializer_class = ServeMatchSerializer


class ServePlacementMatchListCreateAPIView(ListCreateAPIView):
    queryset = ServePlacementMatch.objects.all()
    serializer_class = ServePlacementMatchSerializer


class ReceiveMatchListCreateAPIView(ListCreateAPIView):
    queryset = ReceiveMatch.objects.all()
    serializer_class = ReceiveMatchSerializer


class ReceivePlacementMatchListCreateAPIView(ListCreateAPIView):
    queryset = ReceivePlacementMatch.objects.all()
    serializer_class = ReceivePlacementMatchSerializer


class RallyMatchListCreateAPIView(ListCreateAPIView):
    queryset = RallyMatch.objects.all()
    serializer_class = RallyMatchSerializer


class RallyPlacementMatchListCreateAPIView(ListCreateAPIView):
    queryset = RallyPlacementMatch.objects.all()
    serializer_class = RallyPlacementMatchSerializer


class OthersMatchListCreateAPIView(ListCreateAPIView):
    queryset = OthersMatch.objects.all()
    serializer_class = OthersMatchSerializer


class OtherPlacementMatchListCreateAPIView(ListCreateAPIView):
    queryset = OtherPlacementMatch.objects.all()
    serializer_class = OtherPlacementMatchSerializer


class PreMatchListCreateAPIView(ListCreateAPIView):
    queryset = PreMatch.objects.all()
    serializer_class = PreMatchSerializer


class SetScoreListCreateAPIView(ListCreateAPIView):
    queryset = SetScore.objects.all()
    serializer_class = SetScoreSerializer


class PostMatchListCreateAPIView(ListCreateAPIView):
    queryset = PostMatch.objects.all()
    serializer_class = PostMatchSerializer
