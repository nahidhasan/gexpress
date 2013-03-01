from grelation.models import Gene
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.http import HttpResponse

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
	
def queryAnalyzer(query):
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
		ids = queryAnalyzer(search_query)
		message = 'You searched for: %r' %request.GET['q']
	else:
		message = 'You submitted an empty form.'
	return render_to_response('grln/search_result.html',{'gene_id':ids, 'query':search_query},context_instance = RequestContext(request),)