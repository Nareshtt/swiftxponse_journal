from django.contrib import admin
from .models import (
    Player, Serve, ServePlacement, Receive, ReceivePlacement, Rally, RallyPlacement,
    PrePractice, Drill, Stroke, PostPractice, PlayerProfile, MatchDetail, CheckList,
    ServeMatch, ServePlacementMatch, ReceiveMatch, ReceivePlacementMatch, RallyMatch,
    RallyPlacementMatch, OthersMatch, OtherPlacementMatch, PreMatch, SetScore, PostMatch
)

# Registering models in the admin site
admin.site.register(Player)
admin.site.register(Serve)
admin.site.register(ServePlacement)
admin.site.register(Receive)
admin.site.register(ReceivePlacement)
admin.site.register(Rally)
admin.site.register(RallyPlacement)
admin.site.register(PrePractice)
admin.site.register(Drill)
admin.site.register(Stroke)
admin.site.register(PostPractice)
admin.site.register(PlayerProfile)
admin.site.register(MatchDetail)
admin.site.register(CheckList)
admin.site.register(ServeMatch)
admin.site.register(ServePlacementMatch)
admin.site.register(ReceiveMatch)
admin.site.register(ReceivePlacementMatch)
admin.site.register(RallyMatch)
admin.site.register(RallyPlacementMatch)
admin.site.register(OthersMatch)
admin.site.register(OtherPlacementMatch)
admin.site.register(PreMatch)
admin.site.register(SetScore)
admin.site.register(PostMatch)
