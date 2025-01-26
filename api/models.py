from django.db import models

# Player Information
class Player(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)  # E.g., U-18, Senior
    academy_name = models.CharField(max_length=100)
    dist_or_state = models.CharField(max_length=100)
    forehand_rubber = models.CharField(max_length=1000)  # Forehand equipment details
    backhand_rubber = models.CharField(max_length=1000)  # Backhand equipment details
    blade = models.CharField(max_length=1000)  # Blade details

    def __str__(self):
        return f"Player: {self.name}"


# Serve Model
class Serve(models.Model):
    player = models.ForeignKey(Player, related_name="serves", on_delete=models.CASCADE)
    serve_type = models.CharField(max_length=100)  # E.g., Pendulum backspin
    description = models.TextField(null=True, blank=True)  # Optional notes

    def __str__(self):
        return f"Serve: {self.serve_type}"


# Serve Placement Model
class ServePlacement(models.Model):
    serve = models.ForeignKey(Serve, related_name="placements", on_delete=models.CASCADE)
    start_x = models.FloatField()  # X coordinate of serve initiation
    start_y = models.FloatField()  # Y coordinate of serve initiation
    end_x = models.FloatField()  # X coordinate of serve placement
    end_y = models.FloatField()  # Y coordinate of serve placement
    placement_type = models.CharField(max_length=100, null=True, blank=True)  # E.g., Forehand short, Middle deep

    def __str__(self):
        return f"ServePlacement: ({self.start_x}, {self.start_y}) → ({self.end_x}, {self.end_y})"


# Receive Model
class Receive(models.Model):
    player = models.ForeignKey(Player, related_name="receives", on_delete=models.CASCADE)
    receive_type = models.CharField(max_length=100)  # E.g., Flick
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Receive: {self.receive_type}"


# Receive Placement Model
class ReceivePlacement(models.Model):
    receive = models.ForeignKey(Receive, related_name="placements", on_delete=models.CASCADE)
    start_x = models.FloatField()  # X coordinate of receive initiation
    start_y = models.FloatField()  # Y coordinate of receive initiation
    end_x = models.FloatField()  # X coordinate of receive placement
    end_y = models.FloatField()  # Y coordinate of receive placement
    placement_type = models.CharField(max_length=100, null=True, blank=True)  # E.g., Forehand deep, Middle short

    def __str__(self):
        return f"ReceivePlacement: ({self.start_x}, {self.start_y}) → ({self.end_x}, {self.end_y})"


# Rally Model
class Rally(models.Model):
    player = models.ForeignKey(Player, related_name="rallies", on_delete=models.CASCADE)
    rally_type = models.CharField(max_length=100)  # E.g., Offensive, Defensive
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Rally: {self.rally_type}"


# Rally Placement Model
class RallyPlacement(models.Model):
    rally = models.ForeignKey(Rally, related_name="placements", on_delete=models.CASCADE)
    start_x = models.FloatField()  # X coordinate of rally initiation
    start_y = models.FloatField()  # Y coordinate of rally initiation
    end_x = models.FloatField()  # X coordinate of rally placement
    end_y = models.FloatField()  # Y coordinate of rally placement

    def __str__(self):
        return f"RallyPlacement: ({self.start_x}, {self.start_y}) → ({self.end_x}, {self.end_y})"


# Pre-Practice Model
class PrePractice(models.Model):
    obj = models.TextField()  # Objective for the day
    goals = models.TextField()  # Goals for the session
    yesterdays_nutrition_level = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    energy_level = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    sleep_quality = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    stress_level = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    motivation_level = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])


# Drill Model
class Drill(models.Model):
    pre_practice = models.ForeignKey(PrePractice, related_name="drills", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)  # Name or description of the drill
    description = models.TextField(null=True, blank=True)  # Optional overview of the drill

    def __str__(self):
        return f"Drill: {self.name}"


# Stroke Model for Drill
class Stroke(models.Model):
    drill = models.ForeignKey(Drill, related_name="strokes", on_delete=models.CASCADE)
    start_x = models.FloatField()  # X coordinate of the starting point
    start_y = models.FloatField()  # Y coordinate of the starting point
    end_x = models.FloatField()  # X coordinate of the ending point
    end_y = models.FloatField()  # Y coordinate of the ending point
    action = models.CharField(max_length=100)  # Type of stroke (e.g., serve, flick, winner)
    description = models.TextField(null=True, blank=True)  # Optional notes about the stroke

    def __str__(self):
        return f"Stroke: {self.action} ({self.start_x}, {self.start_y}) → ({self.end_x}, {self.end_y})"


# Post-Practice Model
class PostPractice(models.Model):
    emotions_and_reason = models.TextField()
    focus_level = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    motivation_level = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    managing_emotion = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    satisfaction_level = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    improvement_level = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    areas_of_happy = models.TextField()
    things_happened = models.TextField()
    skills_learnt = models.TextField()
    what_couldve_done_better = models.TextField()




class PlayerProfile(models.Model):
    player = models.ForeignKey(Player,related_name='player',on_delete=models.CASCADE)
    tactical_strength = models.TextField()
    technical_strength = models.TextField()
    mental_strength = models.TextField()
    tactical_weakness = models.TextField()
    technical_weakness = models.TextField()
    mental_weakness = models.TextField()
    general_match_strategy = models.TextField()

class MatchDetail(models.Model):
    tournament = models.CharField(max_length=1000)
    venue = models.CharField(max_length=1000)
    date = models.DateField()
    event = models.CharField(max_length=1000)
    round = models.CharField(max_length=1000)
    opponent = models.CharField(max_length=100)
    academy = models.CharField(max_length=100)
    playing_hand = models.CharField(max_length=10,choices=[('right', 'Right'), ('left', 'Left')],default='right')
    dist_or_state = models.CharField(max_length=100)
    forehand_rubber = models.CharField(max_length=1000)  # Forehand equipment details
    backhand_rubber = models.CharField(max_length=1000)  # Backhand equipment details
    blade = models.CharField(max_length=1000)  # Blade details
    strength = models.TextField()
    weakness = models.TextField()

class CheckList(models.Model):
    warmup_physical = models.BooleanField(default=False)
    warmup_mental = models.BooleanField(default=False)
    pmr = models.BooleanField(default=False)
    visualization = models.BooleanField(default=False)
    breathing = models.BooleanField(default=False)
    self_talk = models.BooleanField(default=False)

# Serve Data for Pre-Match
class ServeMatch(models.Model):
    match_detail = models.ForeignKey(MatchDetail, related_name="serves", on_delete=models.CASCADE)  # Link to specific match
    serve_type = models.CharField(max_length=100)  # Type of serve (e.g., Pendulum backspin)
    description = models.TextField(null=True, blank=True)  # Description of the serve, e.g., "serve to forehand deep"

    def __str__(self):
        return f"Serve: {self.serve_type}"
    
class ServePlacementMatch(models.Model):
    serve = models.ForeignKey(ServeMatch, related_name="placements", on_delete=models.CASCADE)
    start_x = models.FloatField()  # X coordinate of serve initiation
    start_y = models.FloatField()  # Y coordinate of serve initiation
    end_x = models.FloatField()  # X coordinate of serve placement
    end_y = models.FloatField()  # Y coordinate of serve placement
    placement_type = models.CharField(max_length=100, null=True, blank=True)  # E.g., Forehand short, Middle deep

    def __str__(self):
        return f"ServePlacement: ({self.start_x}, {self.start_y}) → ({self.end_x}, {self.end_y})"

# Receive Data for Pre-Match
class ReceiveMatch(models.Model):
    match_detail = models.ForeignKey(MatchDetail, related_name="receives", on_delete=models.CASCADE)  # Link to specific match
    receive_type = models.CharField(max_length=100)  # Type of receive (e.g., Flick)
    description = models.TextField(null=True, blank=True)  # Description of the receive, e.g., "flick to forehand deep"

    def __str__(self):
        return f"Receive: {self.receive_type}"
    
class ReceivePlacementMatch(models.Model):
    receive = models.ForeignKey(ReceiveMatch, related_name="placements", on_delete=models.CASCADE)
    start_x = models.FloatField()  # X coordinate of receive initiation
    start_y = models.FloatField()  # Y coordinate of receive initiation
    end_x = models.FloatField()  # X coordinate of receive placement
    end_y = models.FloatField()  # Y coordinate of receive placement
    placement_type = models.CharField(max_length=100, null=True, blank=True)  # E.g., Forehand deep, Middle short

    def __str__(self):
        return f"ReceivePlacement: ({self.start_x}, {self.start_y}) → ({self.end_x}, {self.end_y})"

# Rally Data for Pre-Match
class RallyMatch(models.Model):
    match_detail = models.ForeignKey(MatchDetail, related_name="rallies", on_delete=models.CASCADE)  # Link to specific match
    rally_type = models.CharField(max_length=100)  # Type of rally (e.g., Offensive, Defensive)
    description = models.TextField(null=True, blank=True)  # Description of the rally, e.g., "long rally with fast pace"

    def __str__(self):
        return f"Rally: {self.rally_type}"
    
class RallyPlacementMatch(models.Model):
    rally = models.ForeignKey(RallyMatch, related_name="placements", on_delete=models.CASCADE)
    start_x = models.FloatField()  # X coordinate of rally initiation
    start_y = models.FloatField()  # Y coordinate of rally initiation
    end_x = models.FloatField()  # X coordinate of rally placement
    end_y = models.FloatField()  # Y coordinate of rally placement

    def __str__(self):
        return f"RallyPlacement: ({self.start_x}, {self.start_y}) → ({self.end_x}, {self.end_y})"
    
class OthersMatch(models.Model):
    match_detail = models.ForeignKey(MatchDetail, related_name="others", on_delete=models.CASCADE)  # Link to specific match
    other_type = models.CharField(max_length=100)  # Type of other action (e.g., Pass, Block, Deflect)
    description = models.TextField(null=True, blank=True)  # Description of the other action, e.g., "pass to opponent's left"

    def __str__(self):
        return f"Other: {self.other_type}"
    
class OtherPlacementMatch(models.Model):
    other = models.ForeignKey(OthersMatch, related_name="placements", on_delete=models.CASCADE)
    start_x = models.FloatField()  # X coordinate of rally initiation
    start_y = models.FloatField()  # Y coordinate of rally initiation
    end_x = models.FloatField()  # X coordinate of rally placement
    end_y = models.FloatField()

    def __str__(self):
        return f"OtherPlacement: ({self.start_x}, {self.start_y}) → ({self.end_x}, {self.end_y})"

class PreMatch(models.Model):
    match_details = models.ForeignKey(MatchDetail,on_delete=models.CASCADE)
    match_progress_goals = models.TextField()
    strategies_and_tactics = models.TextField()
    pre_match_checklist = models.ForeignKey(CheckList, on_delete=models.CASCADE)
    keywords = models.TextField()
    serves = models.ManyToManyField(ServeMatch, related_name="pre_matches", blank=True)
    receives = models.ManyToManyField(ReceiveMatch, related_name="pre_matches", blank=True)
    rallies = models.ManyToManyField(RallyMatch, related_name="pre_matches", blank=True)
    others = models.ManyToManyField(OthersMatch, related_name="pre_matches", blank=True)

class SetScore(models.Model):
    set_number = models.IntegerField()
    player_1_points = models.IntegerField()
    player_2_points = models.IntegerField()

class PostMatch(models.Model):
    score = models.ForeignKey(SetScore, on_delete=models.CASCADE)
    won = models.BooleanField(default=False)
    execution_of_plan = models.TextField()
    positive_technical = models.TextField()
    positive_tactical = models.TextField()
    positive_mental = models.TextField()
    positive_physical = models.TextField()
    to_be_improved = models.TextField()
    different_approach = models.TextField()
    lessons = models.TextField()
    Notes = models.TextField()