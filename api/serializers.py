from rest_framework import serializers
from .models import PrePractice, Stroke, Drill,PostPractice,PreMatch,Skill,Match,Game,PostMatch,PlayerProfile
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
   class Meta:
    model = User
    fields = ('id', 'username', 'password')
    extra_kwargs = {'password':{'write_only':True}}

   def create(self, validated_data):
    user = User.objects.create_user(**validated_data)
    return user


class PrePracticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrePractice
        fields = '__all__'

class PostPracticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostPractice
        fields = '__all__'

class PreMatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreMatch
        fields = '__all__'

class PlayerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerProfile
        fields = '__all__'


class StrokeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stroke
        fields = '__all__'

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'


class DrillSerializer(serializers.ModelSerializer):
    strokes = serializers.PrimaryKeyRelatedField(many=True, queryset=Stroke.objects.all())

    class Meta:
        model = Drill
        fields = '__all__'

    def create(self, validated_data):
        strokes = validated_data.pop('strokes', [])
        drill = Drill.objects.create(**validated_data)
        drill.strokes.set(strokes)  # Use `.set()` to assign ManyToMany relationships
        return drill


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ["id", "set_number", "player1_score", "player2_score"]

class MatchSerializer(serializers.ModelSerializer):
    games = GameSerializer(many=True, read_only=True)  # Nested serializer to include all game scores

    class Meta:
        model = Match
        fields = ["match_id", "num_sets", "created_at", "games"]  # Use match_id instead of id


class PostMatchSerializer(serializers.ModelSerializer):
    match_id = serializers.PrimaryKeyRelatedField(
        queryset=Match.objects.all(), source="match"
    )  # Allows linking to an existing match

    class Meta:
        model = PostMatch
        fields = [
            "id", "match_id", "plans", "feed_physical", "feed_mental",
            "feed_technical", "feed_tactical", "improve_physical",
            "improve_mental", "improve_technical", "improve_tactical",
            "done_better", "lessons", "notes", "player1", "player2", "created_at"
        ]
