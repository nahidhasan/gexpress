from grelation.models import Gene

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