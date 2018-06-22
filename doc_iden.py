from lib.gvision_extract_features 	import extract_features
from lib.direct_matcher 			import direct_match
from lib.spacy_nlp 					import spacy_nlp_match
import sys
import os

from lib.doc_category               import find_best_doc_category
from lib.training_data				import save_for_training

def main_doc_iden(file_name):
	features 			 = extract_features(file_name)
	gvision_direct_match = direct_match    (features)
	#gvision_nlp_match    = spacy_nlp_match (features)

	predictions 		 = gvision_direct_match #+ gvision_nlp_match

	result 				 = find_best_doc_category(predictions)

	if result:
		print('File identified as {} with {:.2f}% confidence\n'.format(result[0], result[1]*100))
		return (result[0])
	else :
		print('File not matched with any predefined categories\n')
		return ("No_Match")




#save_for_training(image_name = sys.argv[1] + ".jpg")


