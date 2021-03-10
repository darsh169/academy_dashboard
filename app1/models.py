from django.db import models

# Create your models here.

class Academy(models.Model):
	name=models.CharField(max_length=30)
	status=models.BooleanField(default=False)
	price=models.IntegerField()
	players_per_court=models.IntegerField()

	
