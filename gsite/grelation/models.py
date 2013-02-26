from django.db import models

class Gene(models.Model):
	name = models.TextField()
	gid = models.IntegerField()
	duplicate = models.BooleanField()
	
	def __unicode__(self):
		return self.name, self.gid
