import spacy
import os

nlp			= spacy.load('en_core_web_lg')
result = []

def spacy_nlp_match(features):

	doc_file = os.path.abspath(os.curdir) + "\\resources\\doc_types.txt"

	match			= ''
	max_similarity 	= 0

	with open(doc_file) as f:
		for line in f:
			for feature in features:
				# replace function ensures that there is no \n in line
				line_nlp	= nlp(line.replace("\n",""))
				similarity 	= line_nlp.similarity(nlp(feature[0]))

				if (similarity>max_similarity):
					match 		   = line_nlp
					max_similarity = similarity	
					confidence 	   = feature[1] * round(max_similarity,2)


	result.append((str(match), confidence))

	return result