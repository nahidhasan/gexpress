from django.contrib import admin
from grelation.models import Gene

class GeneAdmin(admin.ModelAdmin):

	# using https://docs.djangoproject.com/en/dev/intro/tutorial02/
	fieldsets = [
        ('Gene',    {'fields': ['name']}),
        ('Gene ID', {'fields': ['gid']}),
		('Symbol?', {'fields': ['is_symbol'], 'classes': ['collapse']}),
		('Full Gene Name?', {'fields': ['is_gname'], 'classes': ['collapse']}),
    ]
	list_display = ('name','gid','is_symbol','is_gname') 
	# list_filter = ['gid']
	search_fields = ['name']
	#search_fields = ['gid']

admin.site.register(Gene, GeneAdmin)