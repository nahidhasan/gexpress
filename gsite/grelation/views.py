from grelation.models import Gene
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.core.files import File
import os
import pdb

def load_gene(file_path_index, file_path_duplicate):
	#this loads genes from 'gene_index.txt' and 'only_duplicate_complete_list.txt' file
	file_duplicate = open(file_path_duplicate, 'r')
	dup_list = []
	for line in file_duplicate:
		dup_list.append(line[:-1])
	file_duplicate.close()
	file_index = open(file_path_index,'r')
	for line in file_index:
		geneid = line[:15]
		genelist = line[15:].strip().split('|')
		geneid = int(geneid.strip())

		# loading in database
		for i in range(0,len(genelist)):
			if genelist[i] in dup_list:
				pass
			else:			
				# previous of last element is symbol
				if i == len(genelist)-2:
					gene = Gene(name = genelist[i], gid = geneid, is_symbol = True, is_gname = False)
					
				# last element is gene name
				elif i == len(genelist)-1:
					gene = Gene(name = genelist[i], gid = geneid, is_symbol = False, is_gname = True)
					
				else:
					gene = Gene(name = genelist[i], gid = geneid, is_symbol = False, is_gname = False)
				
				
				gene.save()
				#except:
					#print 'oops! id:', str(geneid), ' name:', genelist[i], ' can not be saved'

	print 'Loading Data Completed'
	
def fileManager():
	base = os.path.normpath(os.path.join(settings.PROJECT_DIR,'..'))
	fs = FileSystemStorage(location = os.path.join(base,'data/'))
	print fs.location
	
def queryAnalyzer(query):
	print 'here'
	if '+' in query:
		print query
		single_query_list = query.split('+')
		queryset_list = []
		for i in single_query_list:
			set = Gene.objects.filter(name=i)
			queryset_list.append(set)
		
		id_list = []
		file_list = []
		for i in range(0,len(queryset_list)):
			id_list.append(queryset_list[i].values_list('gid','name')[0][0])
		print id_list
		id_list.sort()
		print id_list
		i = 0
		j = 0
		for i in range(0,len(id_list)-1):
			for j in range(i+1,len(id_list)):
				file_list.append(str(id_list[i])+'&&'+str(id_list[j]))
		
		print file_list
		
		base = os.path.normpath(os.path.join(settings.PROJECT_DIR,'..'))
		
		file_contents = []
		for item in file_list:
			f = open(base+'/data/'+item+'.txt', 'r')
			myfile = File(f)
			fdata = myfile.read()
			file_contents.append(fdata)
		
		
		print file_contents
			
		p = queryset_list[1].values_list('gid','name')[0][0]
		print p
		print type(p)
		return file_contents
	else:
		temp = Gene.objects.filter(name__icontains = query)
		return temp

def home(request):

	return render_to_response(
		'grln/home.html',
		context_instance = RequestContext(request),
		)
		
def search(request):
	
	if 'q' in request.GET and request.GET['q']:
		search_query = request.GET['q']
		file_contents = queryAnalyzer(search_query)
		# print ids
		# pdb.set_trace()
		
		message = 'You searched for: %r' %request.GET['q']
	else:
		message = 'You submitted an empty form.'
	return render_to_response('grln/search_result.html',{'file_list':file_contents, 'query':search_query},context_instance = RequestContext(request),)