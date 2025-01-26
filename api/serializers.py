from rest_framework import serializers
from .models import (
    Player,
    Serve,
    ServePlacement,
    Receive,
    ReceivePlacement,
    Rally,
    RallyPlacement,
    PrePractice,
    Drill,
    Stroke,
    PostPractice,
    PlayerProfile,
    MatchDetail,
    CheckList,
    ServeMatch,
    ServePlacementMatch,
    ReceiveMatch,
    ReceivePlacementMatch,
    RallyMatch,
    RallyPlacementMatch,
    OthersMatch,
    OtherPlacementMatch,
    PreMatch,
    SetScore,
    PostMatch
)


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = "__all__"


class ServeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Serve
        fields = "__all__"


class ServePlacementSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServePlacement
        fields = "__all__"


class ReceiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receive
        fields = "__all__"


class ReceivePlacementSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReceivePlacement
        fields = "__all__"


class RallySerializer(serializers.ModelSerializer):
    class Meta:
        model = Rally
        fields = "__all__"


class RallyPlacementSerializer(serializers.ModelSerializer):
    class Meta:
        model = RallyPlacement
        fields = "__all__"


class PrePracticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrePractice
        fields = "__all__"


class DrillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drill
        fields = "__all__"


class StrokeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stroke
        fields = "__all__"


class PostPracticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostPractice
        fields = "__all__"


class PlayerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerProfile
        fields = "__all__"


class MatchDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = MatchDetail
        fields = "__all__"


class CheckListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckList
        fields = "__all__"


class ServeMatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServeMatch
        fields = "__all__"


class ServePlacementMatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServePlacementMatch
        fields = "__all__"


class ReceiveMatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReceiveMatch
        fields = "__all__"


class ReceivePlacementMatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReceivePlacementMatch
        fields = "__all__"


class RallyMatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = RallyMatch
        fields = "__all__"


class RallyPlacementMatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = RallyPlacementMatch
        fields = "__all__"


class OthersMatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = OthersMatch
        fields = "__all__"


class OtherPlacementMatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtherPlacementMatch
        fields = "__all__"


class PreMatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreMatch
        fields = "__all__"


class SetScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = SetScore
        fields = "__all__"


class PostMatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostMatch
        fields = "__all__"
