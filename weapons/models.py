from django.db import models

class Weapon(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    faction = models.IntegerField()
    category_id = models.IntegerField()
    muzzle_velocity = models.IntegerField()
    refire_ms = models.IntegerField()
    max_damage = models.IntegerField()
    min_damage = models.IntegerField()
    damage_max_range = models.IntegerField()
    damage_min_range = models.IntegerField()

    def __str__(self):
        return self.name