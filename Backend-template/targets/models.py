from django.db import models

class Target(models.Model):
    name = models.CharField(max_length=70)
    attack_priority = models.IntegerField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    enemy_organization = models.CharField(max_length=60)
    target_goal = models.CharField(max_length=50)
    target_id = models.IntegerField(primary_key=True)
    was_target_destroyed = models.BooleanField()


def __str__(self):
        return f"target name:{self.target_name}, prioritize: {self.prioritize}, target_coordinates_width: {self.target_coordinates_width},  target_coordinates_length: {self.target_coordinates_length}, enemy_organization: {self.enemy_organization}, purpose_designation: {self.purpose_designation},target_attacked: {self.target_attacked}, id_target: {self.id_target}"
