from django.contrib import admin
from .models import PlayerDB, SimpleGame, GamersDB, RoundsDB

# Register your models here.
admin.site.register(PlayerDB)
admin.site.register(SimpleGame)
admin.site.register(GamersDB)
admin.site.register(RoundsDB)
