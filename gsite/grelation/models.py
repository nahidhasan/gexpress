from django.db import models

class Gene(models.Model):
	name = models.TextField()
	gid = models.BigIntegerField()
	is_symbol = models.BooleanField()
	is_gname = models.BooleanField()
	
	def __unicode__(self):
		return self.name
	is_symbol.boolean = True
	is_gname.boolean = True
	gid.short_description = "Gene ID"
	is_symbol.short_description = "Symbol?"
	is_gname.short_description = "Original Gene Name?"

