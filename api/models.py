

# Player Information
from django.db import models


class PrePractice(models.Model):
    objective = models.TextField()
    motivation = models.IntegerField()
    energy_level = models.IntegerField()
    nutrition = models.IntegerField()
    sleep_quality = models.IntegerField()
    stress = models.IntegerField()
    technical = models.TextField()
    tactical = models.TextField()
    physical = models.TextField()
    mental = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class PostPractice(models.Model):
    emotions = models.TextField()
    motivation = models.IntegerField()
    focus = models.IntegerField()
    managing_emotions = models.IntegerField()
    satisfaction = models.IntegerField()
    improvement = models.IntegerField()
    happy = models.TextField()
    experiences = models.TextField()
    skills = models.TextField()
    done_better = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class PreMatch(models.Model):
    class PlayingHand(models.IntegerChoices):
        RIGHT = 0, "Right-Handed"
        LEFT = 1, "Left-Handed"
    tournament =  models.TextField()
    venue = models.TextField()
    date = models.DateTimeField()
    event =  models.TextField()
    rounds =  models.TextField()
    opponent_name =  models.TextField()
    academy =  models.TextField()
    playing_hand = models.IntegerField(choices=PlayingHand.choices)  # ✅ Corrected
    fh_rubber =  models.TextField()
    bh_rubber =  models.TextField()
    blade =  models.TextField()
    strengths =  models.TextField()
    weaknesses =  models.TextField()
    goals =  models.TextField()
    plan =  models.TextField()
    warm_up_physical = models.BooleanField(default=False)
    warm_up_mental = models.BooleanField(default=False)
    pmr = models.BooleanField(default=False)
    visualization = models.BooleanField(default=False)
    breathing = models.BooleanField(default=False)
    self_talk = models.BooleanField(default=False)
    keywords =  models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Stroke(models.Model):
    stroke_name = models.CharField(max_length=255)
    response = models.CharField(max_length=50)
    response_from = models.CharField(max_length=50)
    response_length = models.CharField(max_length=50)
    placement = models.CharField(max_length=50)
    placement_length = models.CharField(max_length=50)

class Drill(models.Model):
    drill_name = models.CharField(max_length=255)
    strokes = models.ManyToManyField(Stroke)
    created_at = models.DateTimeField(auto_now_add=True)

class Skill(models.Model):
    player = models.CharField(max_length=50)
    skill_name = models.CharField(max_length=50)
    stroke_type = models.CharField(max_length=255)
    placement_from = models.CharField(max_length=50)
    placement_length = models.CharField(max_length=50)
    target_placements = models.JSONField(default=list)  # Stores list of placements
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.skill_name} - {self.stroke_type}"
    from django.db import models

class Match(models.Model):
    SET_CHOICES = [(1, "Best of 1"), (3, "Best of 3"), (5, "Best of 5"), (7, "Best of 7")]

    match_id = models.AutoField(primary_key=True)
    num_sets = models.IntegerField(choices=SET_CHOICES)  # Set count (1, 3, 5, 7)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Match {self.match_id} - Best of {self.num_sets}"

class Game(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE, related_name="games")
    set_number = models.IntegerField()  # Set index (0, 1, 2, etc.)
    player1_score = models.IntegerField()
    player2_score = models.IntegerField()

    def __str__(self):
        return f"Match {self.match.match_id} - Set {self.set_number}: {self.player1_score}-{self.player2_score}"

class PostMatch(models.Model):
    plans = models.TextField()
    feed_physical = models.TextField()
    feed_mental = models.TextField()
    feed_technical = models.TextField()
    feed_tactical = models.TextField()
    improve_physical = models.TextField()
    improve_mental = models.TextField()
    improve_technical = models.TextField()
    improve_tactical = models.TextField()
    done_better = models.TextField()
    lessons = models.TextField()
    notes = models.TextField()
    player1 = models.CharField(max_length=50)
    player2 = models.CharField(max_length=50)
    match = models.OneToOneField("Match", on_delete=models.CASCADE, related_name="post_match")
    created_at = models.DateTimeField(auto_now_add=True)

class PlayerProfile(models.Model):
    class PlayingHand(models.IntegerChoices):
        RIGHT = 0, "Right-Handed"
        LEFT = 1, "Left-Handed"
    player_name = models.CharField(max_length=50)
    academy = models.CharField(max_length=50)
    playing_hand = models.IntegerField(choices=PlayingHand.choices)  # ✅ Corrected
    fh_rubber = models.CharField(max_length=50)
    bh_rubber = models.CharField(max_length=50)
    blade = models.CharField(max_length=50)
    strength_technical = models.TextField()
    strength_tactical = models.TextField()
    strength_mental = models.TextField()
    weakness_technical = models.TextField()
    weakness_tactical = models.TextField()
    weakness_mental = models.TextField()
    tactics = models.TextField()
    points_scoring = models.TextField()
    points_losing = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

