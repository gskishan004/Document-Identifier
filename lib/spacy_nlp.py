import spacy

def spacy_nlp_match():

	doc_file = os.path.abspath(os.curdir) + "\\resources\\doc_types.txt"

	match			= ''
	max_similarity 	= 0

	with open(doc_file) as f:
		for line in f:
			for feature in features:
				similarity = line.similarity(feature)

				if (similarity>max_similarity):
					match 		   = line
					max_similarity = similarity	

	return (match, max_similarity)