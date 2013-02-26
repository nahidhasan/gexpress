from django.db import models

class Gene(models.Model):
	name = models.TextField()
	gid = models.BigIntegerField()
	is_symbol = models.BooleanField()
	is_gname = models.BooleanField()
	is_duplicate = models.BooleanField()
	
	def __unicode__(self):
		return self.name
