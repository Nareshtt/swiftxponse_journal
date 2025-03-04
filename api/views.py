from rest_framework.generics import ListCreateAPIView,CreateAPIView
from .models import PrePractice, Drill,PostPractice,PreMatch,Skill,Match,Game,PostMatch,PlayerProfile
from django.contrib.auth.models import User
from .serializers import UserSerializer,PrePracticeSerializer, DrillSerializer,PostPracticeSerializer,PreMatchSerializer,SkillSerializer,MatchSerializer,GameSerializer,PostMatchSerializer,PlayerProfileSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny

class CreateUserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
class PrePracticeListCreateView(ListCreateAPIView):
    queryset = PrePractice.objects.all()
    serializer_class = PrePracticeSerializer

class PostPracticeListCreateView(ListCreateAPIView):
    queryset = PostPractice.objects.all()
    serializer_class = PostPracticeSerializer

class PreMatchListCreateView(ListCreateAPIView):
    queryset =PreMatch.objects.all()
    serializer_class =PreMatchSerializer

class PostMatchListCreateView(ListCreateAPIView):
    queryset =PostMatch.objects.all()
    serializer_class = PostMatchSerializer

class PlayerProfileListCreateView(ListCreateAPIView):
    queryset =PlayerProfile.objects.all()
    serializer_class = PlayerProfileSerializer

class DrillListCreateView(ListCreateAPIView):
    queryset = Drill.objects.all()
    serializer_class = DrillSerializer

class SkillListCreateView(ListCreateAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class MatchListCreateView(ListCreateAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer

class GameListCreateView(ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
